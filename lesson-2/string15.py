a=input("Enter a sentence: ")
b=a.split()
acronym="".join(word[0].upper() for word in b)
print("Acronym: ",acronym)