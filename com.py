##Check a Website Address Has .com
#A Python program that takes a website address and prints out whether it ends with .com or not. 
#For example, given the string "www.google.com", the program should print "www.google.com ends with .com".  

def has_com(a):
  if a.endswith(".com"):
    print(f"{a} ends with .com")
  else:
    print(f"{a} doesn't end with .com")

x = str(input("Enter a website address: "))
has_com(x)