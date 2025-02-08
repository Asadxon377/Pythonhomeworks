string1=input("Enter a string: ")
string2=input("Enter another string: ")
if len(string1.replace(" ",""))==len(string2.replace(" ","")):
    print("They have the same length(Spaces ignored)")
else:
    print("They don't have the same length(Spaces ignored)")