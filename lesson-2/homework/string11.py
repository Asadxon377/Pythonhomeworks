string=input("Enter something: ")
if any(char.isdigit() for char in string):
    print("digit found")
else:
    print("no digits")