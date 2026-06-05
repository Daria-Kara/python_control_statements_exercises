#Remove Non-String List Elements
#A Python program that takes a list and create another list that only contains string elements of the first list. 
#For example, given the list [1, "hello", 4.3, True, "bye"], the program should define a list ["hello", "bye"].

def removal(a):
    return [item for item in a if isinstance(item, str)]

c = ["hello", 1, "bye", 4.3]
string = removal(c)

print(string)