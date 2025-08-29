def is_pangram(sentence):
    if not bool(sentence):
        return False
    alfabeto='qwertyuiopasdfghjklzxcvbnm'
    pilha=''
    sentence = sentence.lower()
    for i in sentence:
      if i in alfabeto and i.isalpha():
        pilha +=i
        
    if len(set(pilha)) ==26:
      return True
    else:
        return False