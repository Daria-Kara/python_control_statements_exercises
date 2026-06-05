#Find All Divisors
#A Python program that finds all divisors of a given positive integer and stores them in a list. 
#For example, given 10, the resulting list should be [1, 2, 5, 10].

n = int(input("Enter a positive integer: "))

divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print("Divisors:", divisors)