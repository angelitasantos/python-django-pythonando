notas = []

while True:
    nota = float(input('Digite uma nota ou -1 para sair... '))
    if nota == -1:
        break

    notas.append(nota)

soma = 0
for i in notas:
    soma = soma + i

media = soma / len(notas)

print(f'Sua nota total foi {soma} e sua média foi {media}.')