from database.connection import create_connection


def insert_individual_customer(customer):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO individual_customers
        (name, cpf, birth_date, address)
        VALUES (?, ?, ?, ?)
        """,
        (
            customer.name,
            customer.cpf,
            customer.birth_date.strftime("%d-%m-%Y"),
            customer.address,
        ),
    )

    connection.commit()
    connection.close()