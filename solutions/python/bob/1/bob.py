def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()  # remove espaços no início/fim

    if not hey_bob_stripped:
        return "Fine. Be that way!"  # string vazia ou só espaços
    elif hey_bob_stripped.isupper() and hey_bob_stripped.endswith('?'):
        return "Calm down, I know what I'm doing!"  # gritando e perguntando
    elif hey_bob_stripped.isupper():
        return "Whoa, chill out!"  # só gritando
    elif hey_bob_stripped.endswith('?'):
        return "Sure."  # pergunta normal
    else:
        return "Whatever."  # qualquer outra situação
