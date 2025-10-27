"""
Build a program where users can 
register (username, password) and then 
log in. Use File writing for registration 
and reading for login validation
"""
# --- Function to register a new user ---
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    # Create file if not exist and read existing users
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",")
                users.append(stored_username)
    except FileNotFoundError:
        pass  # file doesn't exist yet, no users registered
    # Check if username already exists
    if username in users:
        print("\n Username already exists! Please choose a different one.\n")
        return
    # Save new user
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("\n Registration successful! You can now log in.\n")
#Function to login existing user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    print(f"\n Login successful! Welcome, {username}!\n")
                    return
        print("\n Invalid username or password. Please try again.\n")

    except FileNotFoundError:
        print("\n No users found. Please register first.\n")
#Main Program 
while True:
    print("===== USER SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("\n Goodbye!Thank you for using the system.\n")
        break
    else:
        print("\n Invalid choice. Please select 1, 2, or 3.\n")
