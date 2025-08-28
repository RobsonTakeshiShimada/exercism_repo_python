def is_armstrong_number(number):
    number=str(number)
    lista=[]
    for i in number:
        power = int(i)**len(number)
        lista.append(power)
    if sum(lista) == int(number):
        return True
    else:
      return False

