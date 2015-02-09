
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
        while cedula <= valor:
            valores[cedula] += 1
            valor -= cedula

    if valor == 0:
        eh_possivel = True

    if eh_possivel:
        return valores
    else:
        return None
