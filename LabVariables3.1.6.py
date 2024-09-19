#----------- 3.1.6 Lab Variables -----------
#answer = int(input("Input a number: "))
#print(answer >= 100)


#----------- 3.1.8 Analyzing code samples -----------
#number1 = int(input("Enter a number: "))
#number2 = int(input("Enter a number again: "))
#number3 = int(input("Enter a number for the last time: "))

#largest_number = number1;

#if number2 > largest_number:
#   largest_number = number2

#if number3 > largest_number:
#    largest_number = number3
#print("The largest number of", number1, number2, number3, "is", largest_number)


#----------- 3.1.10 LAB Comparison operators and conditional execution -----------
#answer = input("Enter a string:")

#if (answer == "Spathiphyllum"):
#    print("Spathiphyllum is the best plant ever!")
#elif (answer == "spathiphyllum"):
#    print("No, I want a big Spathiphyllum!")
#else:
#    print("Spathiphyllum! Not",answer, "!")



#----------- 3.1.8 Analyzing code samples -----------

#thaler = float(input("Enter your income: "))

#if thaler <= 85528:
#    tax = round((18 * thaler / 100 - 556.02),0)
#else:
#    tax = round((14839.02 + ((thaler - 85528) * 32) /100),0)

#if tax < 0:
#    tax = 0.0

#print("You have to pay an amount of:",tax



#----------- 3.1.12   LAB   Essentials of the if-elif-else statement ----------- 
#year = int(input("Enter a year: "))

#if year < 1582:
#   print("Not within the Gregorian calendar period")
#elif year % 4 != 0:
#    print(year,"it's a common year")
#elif year % 100 != 0:
#    print(year,"it's a leap year")
#elif year % 400 != 0:
#    print(year,"it's a common year")
#else:
#    print(year,"it's a leap year")



#----------- 3.2.3 The while loop: more examples ----------- 
# Store the current largest number here.
#largest_number = -999999999

# Input the first value.
#number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
#while number != -1:
    # Is number larger than largest_number?
#    if number > largest_number:
        # Yes, update largest_number.
#        largest_number = number
    # Input the next number.
#    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
#print("The largest number is:", largest_number)



#----------- 3.2.3 The while loop: more examples ----------- 
#odd_numbers = 0
#even_numbers = 0

#number = int(input("Enter a number or type 0 to stop: "))

# ¡¡¡¡¡¡¡¡any non-zero remainder is considered "truthy"!!!!!!!!!
#while number:
#    if number % 2 == 0:
#        even_numbers += 1
#    else:
#        odd_numbers += 1

#    number = int(input("Enter a number or type 0 to stop"))

#print("Odd numbers count:",odd_numbers)
#print("Even numbers count:", even_numbers)



#----------- 3.2.4   LAB   Guess the secret number -----------
#secret_number = 777
#number = int(input(
#"""
#+================================+
#| Welcome to my game, muggle!    |
#| Enter an integer number        |
#| and guess what number I've     |
#| picked for you.                |
#| So, what is the secret number? |
#+================================+
#"""))

#while number != secret_number:
#    print("Ha ha! You're stuck in my loop!")
#    number = int(input("what is the secret number? "))

#print("Well done, muggle! You are free now.")



#----------- 3.2.5 Looping your code with for -----------
#for i in range(10):
#    print(i)

#print("")
#for j in range(2,8):
#    print(j)
#print("")
#for k in range(2,8,3):
#    print(k)
#print("")
#for l in range(1,1):
#    print(l)
#print("")



#----------- 3.2.7 LAB Essentials of the for loop – counting mississippily -----------
#import time
#for a in range(6):
#    print(a,"Mississippi")
#    time.sleep(1)
    
#print("Ready or not, here I come!")



#----------- 3.2.8 The break and continue statements -----------
#----------- break -----------
#largest_number = -99999999
#counter = 0

#while True:
#    number = int(input("Enter a number or type -1 to end the program: "))
#    if number == -1:
#        break
#    counter += 1
#    if number > largest_number:
#        largest_number = number

#if counter != 0:
#    print("The largest number is", largest_number)
#else:
#    print("You haven't entered any number.")


#----------- continue -----------
#largest_number2 = -99999999
#counter2 = 0

#number2 = int(input("Enter a number or type -1 to end program: "))

#while number2 != -1:
#    if number2 == -1:
#        continue
#    counter2 += 1

#    if number2 > largest_number2:
#        largest_number2 = number2
#    number2 = int(input("Enter a number or type -1 to end the program: "))

#if counter2:
#    print("The largest number is", largest_number2)
#else:
#    print("You haven't entered any number.")



#----------- 3.2.9   LAB   The break statement – Stuck in a loop -----------
#while True:
#    user_word = input("Enter a word:")

#    if(user_word == "chupacabra"):
#        print("You've successfully left the loop.")
#        break



#----------- 3.2.10   LAB   The continue statement – the Ugly Vowel Eater -----------
#user_word = input("Enter a word:")
#user_word = user_word.upper()
#for letter in user_word:
#    if letter == "A":
#        continue
#    elif letter == "E":
#        continue
#    elif letter == "I":
#        continue
#    elif letter == "O":
#        continue
#    elif letter == "U":
#         continue
#    else:
#        print(letter)



        
#----------- 3.2.14   LAB   Essentials of the while loop -----------

# total_blocks = int(input("enter a number:"))
# height = 0
# blocks_in_current_layer = 1
    
# # Loop through the possible layers
# while total_blocks >= blocks_in_current_layer:
#     total_blocks -= blocks_in_current_layer
#     height += 1
#     blocks_in_current_layer += 1

# print("The height of the pyramid:", height)

#----------- 3.2.15   LAB   Collatz's hypothesis -----------

# c0 = int(input("Enter a non-negative and a non-zero number:"))
# if c0 > 0:
# 	steps = 0
# 	while c0 != 1:
# 		if c0 % 2 == 0:
# 			c0 = c0 // 2
# 			print(c0)
# 			steps+= 1
# 		else:
# 			c0 = 3 * c0 + 1
# 			print(c0)
# 			steps+= 1
# 	print("steps =", steps)
# else:
# 	print("Invalid number")

#----------- Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. -----------
# for i in range(11):
#     if i % 2 == 1:
#         print(i)
# print()

#----------- Create a while loop that counts from 0 to 10, and prints odd numbers to the screen  -----------
# h = 0
# while h < 11:
#     if h % 2 != 0:
#         print(h)
#     h +=1

#----------- Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line.  -----------
# for letter in "john.smith@pythoninstitute.org":
#     if letter == '@':
#         break
#     print(letter,end="")

#----------- Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below -----------
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue    
#     print(digit,end="")

#----------- Single bits ----------- 
flag_register = 0x1234  # Valor inicial del registro de banderas
the_mask = 0b1000       # Máscara para aislar el tercer bit

# Reiniciar el tercer bit
flag_register &= ~the_mask
print("Después de reiniciar, flag_register:",bin(flag_register)[2:])
