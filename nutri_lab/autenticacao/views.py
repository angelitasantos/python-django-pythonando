from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from django.conf import settings
import os
from .utils import password_is_valid, fields_empty, email_html
from .models import Ativacao
from hashlib import sha256


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirme_password = request.POST.get('confirme_password')

        if not fields_empty(request, username, email):
            return redirect('/auth/register/')

        if not password_is_valid(request, password, confirme_password):
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            is_active=False)
            user.save()

            token = sha256(f'{username}{email}'.encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/ativar_cadastro.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=username, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")
            
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.DEBUG, 'Erro interno do sistema.')
            return redirect('/auth/register')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=password)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos!')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/pacientes')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')


def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Esse token já foi usado!')
        return redirect('/auth/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativada com sucesso!')
    return redirect('/auth/login')
