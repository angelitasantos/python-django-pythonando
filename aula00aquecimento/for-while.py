numero = 1

while numero < 11:
    resultado = numero * 5
    print(f'{numero} x 5 = {resultado}')
    numero += 1

for i in range(1, 11):
    for x in range(1, 11):
        resultado = i * x
        print(f'{i} x {x} = {resultado}')

