# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Enter a username: ")

if len(user_name) > 12:
    print("Username can not contain more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Username can not contain spaces")
elif not user_name.isalpha():
    print("Username can not contain numbers")
else:
    print(f"Welcome {user_name}")
