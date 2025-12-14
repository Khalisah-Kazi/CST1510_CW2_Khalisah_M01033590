import streamlit as st
from pathlib import Path
from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_services import register_user, login_user, migrate_users_from_file
from app.data.incidents import insert_incident, get_all_incidents
import sys

DATA_DIR = Path("data")


def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)
    
    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Setup database
    conn = None
    try:
        conn = connect_database()
        create_all_tables(conn)
    finally:
        if conn:
            conn.close()
    
    # 2. Migrate users from legacy file (if present)
    users_file = DATA_DIR / "users.txt"
    if not users_file.exists():
        print(f"Migration file not found: {users_file} — skipping migration.")
        return

    conn = None
    try:
        conn = connect_database()
        migrate_users_from_file(conn, users_file)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
