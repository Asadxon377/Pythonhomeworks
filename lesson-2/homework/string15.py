sentence=input("Enter a sentence: ")
b=sentence.split()
acronym="".join(word[0].upper() for word in b)
print("Acronym: ",acronym)