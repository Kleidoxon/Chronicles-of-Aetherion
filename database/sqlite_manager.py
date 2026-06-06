import sqlite3


class SQLiteManager:
    def __init__(self):
        self.connection = sqlite3.connect("aetherion.db")
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS players(
                id INTEGER PRIMARY KEY,
                name TEXT,
                level INTEGER,
                gold INTEGER
            )
            """
        )

        self.connection.commit()   