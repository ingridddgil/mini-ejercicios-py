lista_1 = [2, 4, 5, 1, 4, 3]
lista_2 = lista_1[3:6]
lista_2.append(89)
del lista_1[0]
print(lista_1, lista_2)

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2, list_1)


