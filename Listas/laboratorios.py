#LAB3.6.6
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
my_list = new_list
print("The list with unique elements only:")
print(my_list)
print("---------------------------------------------")

row = [i + 1 for i in range(10)]
print(row)
print("---------------------------------------------")
board = [[0 for i in range(8)] for j in range(8)]

for i in range(len(board)):
    board[i][i] = 1

for g in board:
    print(g)

