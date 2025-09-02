def score(x, y):
    d2 = x * x + y * y  # distância ao quadrado
    
    if d2 > 100:   # maior que 10^2
        return 0
    elif d2 > 25:  # entre 5^2 e 10^2
        return 1
    elif d2 > 1:   # entre 1^2 e 5^2
        return 5
    else:          # até 1^2 (bullseye)
        return 10
