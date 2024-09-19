sum = 0
square_sum = 0
for i in range(101):
    sum += i**2
    square_sum += i
square_sum **= 2
print(square_sum - sum)


