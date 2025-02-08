num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter a third number: "))
if bool(num1!=num2 and num2!=num3 and num3!=num1):
    print("They are different")
else:
    print("Not all different")