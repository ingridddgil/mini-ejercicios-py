num = 1
sum = 0
while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        print(num)
        sum += num
    num += 1

print("sum:", sum)
