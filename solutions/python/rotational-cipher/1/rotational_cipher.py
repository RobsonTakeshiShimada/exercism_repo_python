def rotate(text, key):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    i = 0
    while i < len(text):
        c = text[i]
        if c.lower() in alfabeto:  # só aplica em letras
            idx = alfabeto.index(c.lower())  # posição da letra
            novo_idx = (idx + key) % 26      # desloca com a chave
            nova_letra = alfabeto[novo_idx]
            if c.isupper():
                resultado += nova_letra.upper()
            else:
                resultado += nova_letra
        else:
            resultado += c  # mantém espaços, números, etc.
        i += 1

    return resultado
