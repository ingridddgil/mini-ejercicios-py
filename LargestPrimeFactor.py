number = int(input("Enter a number bigger than 0:\n"))

if number > 0:
    prime_number = 2

    while number > 1:
        if number % prime_number == 0:  
            number //= prime_number  
            print(prime_number)
        else:
            prime_number += 1
            if prime_number == 3:
                prime_number = 3
            elif prime_number % 2 == 0:
                prime_number += 1
            elif prime_number % 3 == 0:
                prime_number += 2

else:
    print("Try again.")
