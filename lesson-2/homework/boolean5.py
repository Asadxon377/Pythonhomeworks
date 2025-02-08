a=input("Enter a string: ")
b=input("Enter another string: ")
if(bool(len(a.replace(" ",""))==len(b.replace(" ","")))):
    print("They have the same length(Spaces ignored)")
else:
    print("They don't have the same length(Spaces ignored)")