#Count the Frequency of List Elements
#A Python program that counts the frequency of each element in a given list and store them in a dictionary. 
#For example, given the list [111, "hello", 222, "hello", 111], the program should define a dictionary {111: 2, "hello": 2, 222: 1}.

items = [111, "hello", 222, "hello", 111]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)