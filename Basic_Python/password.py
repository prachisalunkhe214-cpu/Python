# Authenticating a user
stored_password = "1234561213456"
input_password = input("Enter your password: ")

if input_password == stored_password:
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")