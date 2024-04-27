import math

numero_int_menor_32 = int(input('Informe um número entre 0 e 32, para converte-lo em binário: '))

valor_clonado = numero_int_menor_32

lista_zero_e_um = []
while valor_clonado != 0:
    lista_zero_e_um.append(valor_clonado % 2)
    valor_clonado = math.floor(valor_clonado / 2)

lista_invertida = reversed(lista_zero_e_um)
print(f'O número {numero_int_menor_32} em binário é igual a...')
print(*lista_invertida)