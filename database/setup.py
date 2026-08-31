from database.connection import create_connection


def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS individual_customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            birth_date TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()