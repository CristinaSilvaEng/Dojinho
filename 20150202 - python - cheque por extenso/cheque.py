
def cheque_por_extenso(valor):

    unidades = ['centavo','centavos']
    valores = ['um', 'dois']

    numero_por_extenso = ''

    if valor == 0.01:
        numero_por_extenso = valores[0] +' '+ unidades[0]
    elif valor == 0.02:
        numero_por_extenso = valores[1] +' '+ unidades[1]

    return numero_por_extenso
