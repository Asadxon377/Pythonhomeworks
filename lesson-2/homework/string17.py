string=input("Enter a string: ")
vowels="aeiouAEIOU"
b="".join("@" if char in vowels else char for char in string )
print("using @ instead of vowels: ",b)