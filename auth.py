import bcrypt 
import os 
def hash_password(plain_text_password):
    byte_password = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(byte_password,salt)
    hashed_string = hashed_bytes.decode('utf-8')
    return hashed_string 

def verify_password():
# TODO: Encode both the plaintext password and the stored hash to byt
    encoded_hash = hashed_bytes.encode()
    encoded_password = plain_text_password.encode('utf-8')
# TODO: Use bcrypt.checkpw() to verify the password
    correct_password = bcrypt.checkpw(encoded_hash, encoded_password)
# This function extracts the salt from the hash and compares
    return 

# TEMPORARY TEST CODE - Remove after testing
test_password = "SecurePassword123"

# Test hashing
hashed = hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")

# Test verification with correct password
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")

# Test verification with incorrect password
is_invalid = verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")

USER_DATA_FILE = "users.txt"

def register_user(username, password):
# TODO: Check if the username already exists
    
# TODO: Hash the password
# TODO: Append the new user to the file
# Format: username,hashed_password
return True

def user_exists(username):
# TODO: Handle the case where the file doesn't exist yet
# TODO: Read the file and check each line for the username
return False

def login_user(username, password):
# TODO: Handle the case where no users are registered yet
# TODO: Search for the username in the file
# TODO: If username matches, verify the password
# TODO: If we reach here, the username was not found

def validate_username(username):
pass

def validate_password(password):
pass

def display_menu():
"""Displays the main menu options."""
print("\n" + "="*50)
print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
print(" Secure Authentication System")
print("="*50)
print("\n[1] Register a new user")
print("[2] Login")
print("[3] Exit")
print("-"*50)
def main():
"""Main program loop."""
print("\nWelcome to the Week 7 Authentication System!")
while True:
display_menu()
choice = input("\nPlease select an option (1-3): ").strip()
if choice == '1':
# Registration flow
print("\n--- USER REGISTRATION ---")
username = input("Enter a username: ").strip()
# Validate username
is_valid, error_msg = validate_username(username)
if not is_valid:
print(f"Error: {error_msg}")
continue
password = input("Enter a password: ").strip()# Validate password
is_valid, error_msg = validate_password(password)
if not is_valid:
print(f"Error: {error_msg}")
continue
# Confirm password
password_confirm = input("Confirm password: ").strip()
if password != password_confirm:
print("Error: Passwords do not match.")
continue
# Register the user
register_user(username, password)
elif choice == '2':
# Login flow
print("\n--- USER LOGIN ---")
username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()
# Attempt login
if login_user(username, password):
print("\nYou are now logged in.")
print("(In a real application, you would now access the d
# Optional: Ask if they want to logout or exit
input("\nPress Enter to return to main menu...")
elif choice == '3':
# Exit
print("\nThank you for using the authentication system.")
print("Exiting...")
break
else:
print("\nError: Invalid option. Please select 1, 2, or 3.")
if __name__ == "__main__":
main()

