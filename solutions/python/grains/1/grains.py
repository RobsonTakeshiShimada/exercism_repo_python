def square(number):
    if number <=0 or number>64:
        raise ValueError("square must be between 1 and 64")
    start = 1
    for i in range(1,number):
        start *= 2
    return start 


def total():
    start = 1
    lista=[]
    for i in range(64):
        lista.append(start)
        start *= 2
    return sum(lista)