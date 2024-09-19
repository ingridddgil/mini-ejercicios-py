mayor_palindromo = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        producto = i * j
        b = str(producto)
        es_palindromo = True
        prueba = len(b)
        check = prueba // 2

        for num in range(check):
            if b[num] != b[prueba - num - 1]:
                es_palindromo = False
                break
        
        if es_palindromo and producto > mayor_palindromo:
            mayor_palindromo = producto

print("El mayor palíndromo hecho del producto de dos números de tres dígitos es:", mayor_palindromo)
