import bcrypt
import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "intelligence_platform.db"


def connect_database() -> sqlite3.Connection:
    """Connect to SQLite database and return connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(plain_text_password: str) -> str:
    """Return bcrypt hash (UTF-8 string) for the given plaintext password."""
    byte_password = plain_text_password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(byte_password, salt)
    return hashed_bytes.decode("utf-8")


def verify_password(plain_text_password: str, stored_hashed_string: str) -> bool:
    """Verify plaintext password against stored bcrypt hash (string)."""
    try:
        encoded_password = plain_text_password.encode("utf-8")
        encoded_hash = stored_hashed_string.encode("utf-8")
        return bcrypt.checkpw(encoded_password, encoded_hash)
    except Exception:
        return False


def user_exists(username: str) -> bool:
    """Return True if username exists in database."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists


def register_user(username: str, password: str, role: str = "user") -> tuple[bool, str]:
    """Register a new user. Returns (success: bool, message: str)."""
    # Validate inputs
    is_valid, error_msg = validate_username(username)
    if not is_valid:
        return False, error_msg
    
    is_valid, error_msg = validate_password(password)
    if not is_valid:
        return False, error_msg
    
    conn = connect_database()
    cursor = conn.cursor()
    
    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, f"Username '{username}' already exists."
    
    # Hash the password and insert new user
    password_hash = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role)
        )
        conn.commit()
        conn.close()
        return True, f"User '{username}' registered successfully!"
    except Exception as e:
        conn.close()
        return False, f"Registration error: {str(e)}"


def login_user(username: str, password: str) -> tuple[bool, str]:
    """Login user. Returns (success: bool, message: str)."""
    conn = connect_database()
    cursor = conn.cursor()
    
    # Find user
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        return False, "Username not found."
    
    # Verify password
    stored_hash = user[0]
    if verify_password(password, stored_hash):
        return True, f"Welcome, {username}!"
    else:
        return False, "Invalid password."


def validate_username(username: str) -> tuple[bool, str]:
    """Return (True, "") or (False, "error message")."""
    if not username:
        return False, "Username cannot be empty."
    if "," in username:
        return False, "Username cannot contain commas."
    if len(username) < 3 or len(username) > 30:
        return False, "Username must be 3-30 characters."
    if any(ch.isspace() for ch in username):
        return False, "Username cannot contain whitespace."
    return True, ""


def validate_password(password: str) -> tuple[bool, str]:
    """Return (True, "") or (False, "error message")."""
    if not password:
        return False, "Password cannot be empty."
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    if not (has_letter and has_digit):
        return False, "Password must contain letters and numbers."
    return True, ""


def display_menu() -> None:
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main() -> None:
    """Main program loop (console)."""
    print("\nWelcome to the Week 7 Authentication System!")
    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()
        if choice == "1":
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            success, message = register_user(username, password)
            print(f"{'✓' if success else '✗'} {message}")

        elif choice == "2":
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            success, message = login_user(username, password)
            if success:
                print(f"\n✓ {message}")
                input("\nPress Enter to return to main menu...")
            else:
                print(f"\n✗ {message}")
                input("\nPress Enter to return to main menu...")

        elif choice == "3":
            # Exit
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

