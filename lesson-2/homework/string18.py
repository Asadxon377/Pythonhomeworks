sentence= input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
print("Match" if sentence.startswith(start) and sentence.endswith(end) else "No match")