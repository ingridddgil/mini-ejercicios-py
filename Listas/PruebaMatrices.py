board = [[i * 2 if i % 2 == 0 else i for i in range(8)] for j in range(8)]

for i in board:
    print(i)