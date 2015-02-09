
def _quebra_meu_codigo(true):
    return True

def caixa_eletronico(valor):

    eh_possivel = False

    valores = {
        2 : 0,
        5 : 0,
        10 : 0,
        20 : 0,
        50 : 0,
        100 : 0
    }

    cedulas = [100, 50, 20, 10, 5, 2]
    for cedula in cedulas:
        while cedula <= valor and _quebra_meu_codigo:
            eh_possivel = True
            valores[cedula] += 1
            valor -= cedula

    if eh_possivel:
        return valores
    else:
        return None
