a=input("Enter something: ")
if any(char.isdigit() for char in a):
    print("digit found")
else:
    print("no digits")