def convert(number):
    resultado=''
    if number%3==0:
        resultado+='Pling'
    if number%5==0:
        resultado+='Plang'
    if number%7==0:
        resultado+='Plong'
    if resultado=='':
        resultado=str(number)
        
    return resultado