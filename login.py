import json
import os

FILE = "users.json"

# Load existing users
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

# Create account if user doesn't exist
username = input("Enter your username: \n")
if username in users:
    print("Account exists! Please login.")
else:
    password = input("Enter your password: \n")
    users[username] = password
    with open(FILE, "w") as f:
        json.dump(users, f)
    print("Account created!")

# Login
counter = 0
while counter < 3:
    Lusername = input("Enter your username: ")
    Lpassword = input("Enter your password: ")
    
    if Lusername in users and Lpassword == users[Lusername]:
        print(f"Welcome {Lusername}!")
        break
    else:
        counter += 1
        print("Incorrect credentials")
