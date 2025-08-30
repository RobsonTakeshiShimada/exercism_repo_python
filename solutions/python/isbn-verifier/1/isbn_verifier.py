def is_valid(isbn):
    lista = ''
    i = 0
    while i < len(isbn):
        if isbn[i].isdigit():
            lista += isbn[i]
        elif isbn[i] == "X" and i == len(isbn) - 1:  # só aceita X se for o último
            lista += "X"
        elif isbn[i] not in "- ":  # rejeita qualquer coisa que não seja dígito, X final, traço ou espaço
            return False
        i += 1

    # ISBN-10 precisa ter 10 caracteres
    if len(lista) != 10:
        return False

    soma = 0
    j = 0
    while j < 10:
        if lista[j] == "X":  # se último for X
            valor = 10
        else:
            valor = int(lista[j])
        soma += valor * (10 - j)
        j += 1

    return soma % 11 == 0
