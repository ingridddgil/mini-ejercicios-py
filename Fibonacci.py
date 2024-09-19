i = 1
j = 2
sum = 0
while i < 4000000:  
    if i != 1 and i != 2:
        print(i)
        if i % 2 == 0:
            sum += i
        k = i
        i += j
        j = k
    else:
        print(i)
        if i % 2 == 0:
            sum += i
        i += 1

    
print("sum =", sum)
