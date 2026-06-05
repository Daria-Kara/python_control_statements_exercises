#Check 2 Numbers Are Dividable
#A Python program that takes 2 numbers and prints whether the first one is dividable by the second one or not. 
#For example, if the user inputs 10 and 5, the program should print "10 is dividable by 5".

def divisibility(x, y):
  if x % y == 0:
    print(f"{x} is dividable by {y}")
  else:
    print(f"{x} is not dividable by {y}")

x = float(input("Enter a number: "))
y = float(input("Enter a second number: "))

divisibility(x, y)