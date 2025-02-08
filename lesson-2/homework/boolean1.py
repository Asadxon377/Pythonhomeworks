a=input("Username:")
b=input("Password:")

if bool(len(a.split())==0) and bool(len(b.split())==0):
    print("Empty password")
else:
    print("Not empty")