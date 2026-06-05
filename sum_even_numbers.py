#Sum Even Numbers
#A Python program that computes the sum of even numbers in a given list of integers.

a = int(input("Enter a number: "))

def even(n):
    even_sum = 0
    for i in range(1, n + 1):  # use a different variable name
        if i % 2 == 0:
            even_sum += i
    return even_sum  # moved outside the loop

print("Sum of even numbers:", even(a))