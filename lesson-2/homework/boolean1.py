username=input("Username:")
password=input("Password:")

if len(username.split())==0 and len(password.split())==0:
    print("Empty password")
else:
    print("Valid password")