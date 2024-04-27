qtd_dias = int(input('Informe sua idade em dias: '))

def calcular_anos_meses_dias (dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30

    print(f'Anos: {anos}, meses: {meses}, dias: {dias_finais}')

calcular_anos_meses_dias(qtd_dias)
