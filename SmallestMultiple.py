smallest = False
numero = 1

while not smallest:
    sum = 0
    for i in range(1, 21):
        if numero % i == 0:
            sum += 1
        else:
            break

    if sum == 20:
        smallest = True
    else:
        numero += 1

print(numero)
