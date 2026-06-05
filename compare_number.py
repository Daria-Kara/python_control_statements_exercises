##Compare Numbers
#A Python program that takes an integer, compares it to a predefined number, and tells the user to guess a larger or smaller number. 
#For example, suppose the predefined number is 10 and the user inputs 7. The program should print "7 is too small!".

target_number = 10
number = int(input("Enter an integer: "))

if number < target_number:
    print(f"{number} is too small!")
elif number > target_number:
    print(f"{number} is too large!")
else:
    print(f"{number} is correct!")