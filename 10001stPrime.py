""" suma = 0
valor = 2
set = []
i = 1

while bandera != True:
    if valor == 2 or (valor > 2 and valor % 2 != 0):
        set.append(valor)
        if suma == 10001:
            print(valor)
            break 
        suma += 1
        valor += 1
    else:
        valor += 1
   
# # for a in range(len(set)):
# #     print(set[a], end=" ")

# # print(set) """

suma = 0
valor = 2
set = []
bandera = False

# while not bandera:

#     # Solo procesar si 'valor' es primo
#     if valor == 2 or (valor > 2 and valor % 2 != 0):
#         es_primo = True
#         for i in range(2, int(valor ** 0.5) + 1):
#             if valor % i == 0:
#                 es_primo = False
#                 break

#         if es_primo:
#             set.append(valor)
#             suma += 1
#             if suma == 10001:
#                 print(f"El número primo 10,001 es: {valor}")
#                 bandera = True

#     valor += 1
