
def cheque_por_extenso(valor):

    numero_por_extenso = ''

    if valor == 0.01:
        numero_por_extenso = 'um centavo'
    elif valor == 0.02:
        numero_por_extenso = 'dois centavos'

    return numero_por_extenso
