import bcrypt
import sqlite3
from pathlib import Path
from app.data.db import connect_database
from app.data.users import get_user_by_username, insert_user
from app.data.schema import create_users_table

DATA_DIR = Path("data")


def register_user(username, password, role='user'):
    """Register new user with password hashing."""
    # Hash password
    password_hash = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')
    
    # Insert into database
    insert_user(username, password_hash, role)
    return True, f"User '{username}' registered successfully."


def login_user(username, password):
    """Authenticate user."""
    user = get_user_by_username(username)
    if not user:
        return False, "User not found."
    
    # Verify password
    stored_hash = user[2]  # password_hash column
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
        return True, f"Login successful!"
    return False, "Incorrect password."


def migrate_users_from_file(conn, filepath):
    """Migrate users from users.txt to the database."""
    if not filepath.exists():
        print(f"⚠️ File not found: {filepath}")
        print("   No users to migrate.")
        return 0

    cursor = conn.cursor()
    migrated_count = 0

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) >= 2:
                username = parts[0]
                password_hash = parts[1]
                role = parts[2] if len(parts) >= 3 else "user"

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO users (username, password_hash, role)
                    VALUES (?, ?, ?)
                    """,
                    (username, password_hash, role),
                )

                if cursor.rowcount > 0:
                    migrated_count += 1

    conn.commit()
    print(f"✅ Migrated {migrated_count} users from {filepath.name}")
    return migrated_count




def display_all_users():
    """Display all users in the database."""
    conn = connect_database()
    cursor = conn.cursor()

    # Query all users
    cursor.execute("SELECT id, username, role FROM users")
    users = cursor.fetchall()

    print("\n📋 Users in database:")
    print(f"{'ID':<5} {'Username':<15} {'Role':<10}")
    print("-" * 35)
    for user in users:
        print(f"{user[0]:<5} {user[1]:<15} {user[2]:<10}")

    print(f"\nTotal users: {len(users)}")
    conn.close()


if __name__ == "__main__":
    # Test: display all users
    display_all_users()