# A program that allows the user to sign-up, or sign-in.

print("Greetings user")
print("Would you like to sign-up(1), or sign-in(2)?")
while True:  # A while loop for deciding if the user wants to make an account or login
    print("Please input 1 or 2")
    answer = input()
    if int(answer) == 1:
        break  # Means that the user wants to make a new account, and breaks the loop
    elif int(answer) == 2:
        break
    else:
        continue

usernames = []  # A list for current and future usernames
passwords = []  # A list for current and future passwords

# Making an account
while int(answer) == 1:
    print("Please enter a username")
    new_username = input()
    print("Please enter a password")
    new_password = input()
    usernames.append(new_username)
    passwords.append(new_password)
    answer = int(answer) + 1

# Logging into an existing account
while int(answer) == 2:
    print("Please enter your username")
    username_login = input()
    if username_login in usernames:
        print("hello " + username_login)
        answer = int(answer) + 1
    else:
        continue

# Inputting the password
while int(answer) == 3:
    print("Please enter your password")
    password_login = input()
    if password_login in passwords:
        print("You have succesfully logged in!")
        answer = int(answer) + 1
    else:
        print("Incorrect Password")
        continue

print("Welcome, " + username_login)
