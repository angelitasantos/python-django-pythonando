print('Olá Mundo!')

# Variáveis
'''
Tipos de Dados
int = inteiros = 10, 100, -1000
float = decimais = 10.5, -5.7
string = 'Nome', '10.5'
bool = boolean = True, False
'''

idade = 43
peso = 75.9
altura = 1.69
nome = 'Angelita'
mulher = True

print(f'Olá {nome}, você tem {idade} anos, pesa {peso} kilos e mede {altura} de altura.\nVocê é uma mulher feliz.')


nome = input('Digite seu nome... ')
print(f'Olá {nome}, tudo bem?')
print(type(nome))

###########################################################################################


nota1 = float(input('Digite a primeira nota... '))
nota2 = float(input('Digite a primeira nota... '))

soma = nota1 + nota2

print(f'A soma das suas notas é {soma}.')

###########################################################################################


media = soma / 2

if media >= 6:
    print(f'{nome}, sua média é {media} e você passou de ano.')
elif media >= 4 and media < 6:
    print(f'{nome}, sua média é {media} e você está de recuperação.')
else:
    print(f'Que pena, {nome}. Sua média é {media} e você não passou de ano.')
