def translate(text):
    vowels = ('a', 'e', 'i', 'o', 'u')

    def translate_word(word):
        # 1. Caso começa com vogal ou "xr"/"yt"
        if word[0] in vowels or word.startswith(("xr", "yt")):
            return word + "ay"

        # 2. Caso começa com consoantes seguidas de "qu"
        if "qu" in word:
            idx = word.find("qu")
            if idx != -1 and all(ch not in vowels for ch in word[:idx]):
                return word[idx+2:] + word[:idx+2] + "ay"

        # 3. Caso começa com consoantes seguidas de "y"
        if "y" in word[1:]:  # <<< NÃO pega o "y" da posição 0!
            idx = word.find("y")
            if idx != -1 and all(ch not in vowels for ch in word[:idx]):
                return word[idx:] + word[:idx] + "ay"

        # 4. Caso geral: começa com uma ou mais consoantes
        consonants = ""
        for ch in word:
            if ch not in vowels:
                consonants += ch
            else:
                break
        return word[len(consonants):] + consonants + "ay"

    # Divide em palavras, traduz e junta de novo
    return " ".join(translate_word(w) for w in text.split())
