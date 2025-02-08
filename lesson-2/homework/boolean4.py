a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if bool(a!=b and b!=c and c!=a):
    print("They are different")
else:
    print("Not correct one")