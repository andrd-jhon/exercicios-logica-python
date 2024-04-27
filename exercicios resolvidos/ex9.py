# volume=3.14159*pow(r,2)*altura
import math
raio = int(input('Informe o raio da lata de óleo(em centímetros): '))
altura = int(input('Informe a altura da lata de óleo(em centímetros): '))

volume = math.pi * pow(raio, 2) * altura
print(f'O volume da lata de óleo é: {volume:.2f}cm³')