from pathlib import Path
from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_services import register_user, login_user, migrate_users_from_file
from app.data.incidents import insert_incident, get_all_incidents

DATA_DIR = Path("data")


def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)
    
    # 1. Setup database
    conn = connect_database()
    create_all_tables(conn)
    conn.close()
    
    # 2. Migrate users from legacy file
    conn = connect_database()
    migrate_users_from_file(conn, DATA_DIR / "users.txt")
    conn.close()


if __name__ == "__main__":
    main()
