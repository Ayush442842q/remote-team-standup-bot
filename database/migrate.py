import sqlite3
from sqlite3 import Error

class DatabaseMigration:
    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connection to SQLite database {self.db_name} established.")
            return self.conn
        except Error as e:
            print(e)

    def drop_tables(self):
        tables = [
            'Assignments',
            'Comments',
            'Updates',
            'Standups',
            'Tasks',
            'Teams',
            'Users',
            'Migrations'
        ]

        for table in tables:
            query = f"DROP TABLE IF EXISTS {table}"
            try:
                self.conn.execute(query)
                print(f"Table {table} dropped if existed.")
            except Error as e:
                print(e)

    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                CHECK (role IN ('user', 'admin'))
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                leader_id INTEGER NOT NULL,
                FOREIGN KEY (leader_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                assignee_id INTEGER,
                team_id INTEGER NOT NULL,
                status TEXT,
                FOREIGN KEY (assignee_id) REFERENCES Users (id) ON DELETE SET NULL ON UPDATE CASCADE,
                FOREIGN KEY (team_id) REFERENCES Teams (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Standups (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                team_id INTEGER NOT NULL,
                date DATE NOT NULL,
                time TIME NOT NULL,
                FOREIGN KEY (team_id) REFERENCES Teams (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Updates (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INTEGER NOT NULL,
                standup_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (standup_id) REFERENCES Standups (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                update_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (update_id) REFERENCES Updates (id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                assigned_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (task_id) REFERENCES Tasks (id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL UNIQUE,
                applied_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]

        for query in queries:
            try:
                self.conn.execute(query)
                print("Table created if not existed.")
            except Error as e:
                print(e)

    def create_indexes(self):
        queries = [
            "CREATE INDEX IF NOT EXISTS idx_Users_username ON Users (username)",
            "CREATE INDEX IF NOT EXISTS idx_Users_email ON Users (email)",
            "CREATE INDEX IF NOT EXISTS idx_Teams_name ON Teams (name)",
            "CREATE INDEX IF NOT EXISTS idx_Tasks_title ON Tasks (title)",
            "CREATE INDEX IF NOT EXISTS idx_Tasks_team_id ON Tasks (team_id)",
            "CREATE INDEX IF NOT EXISTS idx_Standups_team_id ON Standups (team_id)",
            "CREATE INDEX IF NOT EXISTS idx_Standups_date ON Standups (date)",
            "CREATE INDEX IF NOT EXISTS idx_Updates_user_id ON Updates (user_id)",
            "CREATE INDEX IF NOT EXISTS idx_Updates_standup_id ON Updates (standup_id)",
            "CREATE INDEX IF NOT EXISTS idx_Comments_update_id ON Comments (update_id)",
            "CREATE INDEX IF NOT EXISTS idx_Comments_user_id ON Comments (user_id)",
            "CREATE INDEX IF NOT EXISTS idx_Assignments_task_id ON Assignments (task_id)",
            "CREATE INDEX IF NOT EXISTS idx_Assignments_user_id ON Assignments (user_id)"
        ]

        for query in queries:
            try:
                self.conn.execute(query)
                print("Index created if not existed.")
            except Error as e:
                print(e)

    def up(self):
        self.drop_tables()
        self.create_tables()
        self.create_indexes()
        self.conn.commit()
        print("Migration applied.")

    def down(self):
        self.drop_tables()
        self.conn.commit()
        print("Migration rolled back.")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection to SQLite database closed.")


def main():
    db_name = "database.db"
    migration = DatabaseMigration(db_name)
    migration.create_connection()
    while True:
        print("\n1. Apply migration")
        print("2. Rollback migration")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            migration.up()
        elif choice == "2":
            migration.down()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")
    migration.close_connection()


if __name__ == "__main__":
    main()