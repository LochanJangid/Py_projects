import sqlite3

class Database:
    """A simple, clean SQLite database wrapper."""

    def __init__(self, db_name: str):
        self.db_name = db_name

    def query(self, query: str, params: tuple = (), operation: str = "commit"):
        """
        Execute a database query.

        operations: "commit" | "fetchone" | "fetchall"

        Usage:
            db.query("INSERT INTO users VALUES (?)", ("Rahul",))
            db.query("SELECT * FROM users", operation="fetchall")
        """
        valid = ("commit", "fetchone", "fetchall")
        if operation not in valid:
            raise ValueError(f"Invalid operation '{operation}'. Choose from: {valid}")

        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)

                if operation == "commit":
                    conn.commit()
                    return True
                elif operation == "fetchone":
                    return cursor.fetchone()
                elif operation == "fetchall":
                    return cursor.fetchall()

        except sqlite3.Error as e:
            raise DatabaseError(f"{e}") from e

    def __repr__(self):
        return f"Database('{self.db_name}')"


class DatabaseError(Exception):
    """Raised when a database query fails."""
    pass