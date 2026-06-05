#Find the Largest Word
#Write a Python program that finds the largest word in a given input string. 
#For example, given the string "hello how are you", the program should print "hello".

text = input("Enter a sentence: ")

words = text.split()

largest_word = words[0]

for word in words:
    if len(word) > len(largest_word):
        largest_word = word

print("Largest word:", largest_word)