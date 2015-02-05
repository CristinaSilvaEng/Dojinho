
def cheque_por_extenso(valor):

    valores = {
        '1' : 'um',
        '2' : 'dois',
        '3' : 'tres',
        '4' : 'quatro',
        '5' : 'cinco',
        '6' : 'seis',
        '7' : 'sete',
        '8' : 'oito',
        '9' : 'nove'
    }

    unidades = ['centavo','centavos']

    numero_por_extenso = ''
    singular = '1'
    s_valor = repr(valor)

    numero_por_extenso = valores[s_valor[-1]]

    if s_valor[-1] == singular:
        numero_por_extenso = numero_por_extenso +' '+ unidades[0]
    else:
        numero_por_extenso = numero_por_extenso +' '+ unidades[1]

    return numero_por_extenso
