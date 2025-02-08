a=input("Enter a word:")
a.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
b=0
c=0
for char in a:
    if char.isalpha():
        if char in vowels:
            b+=1
        else:
            c+=1

print("Vowels: ",b)
print("Consonants: ",c)