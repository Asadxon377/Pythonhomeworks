a=input("Enter a string: ")
vowels="aeiouAEIOU"
b="".join("@" if char in vowels else char for char in a )
print(b)