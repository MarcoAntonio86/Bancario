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

def find_individual_customer_by_cpf(cpf):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM individual_customers
        WHERE cpf = ?
        """,
        (cpf,),
    )

    customer = cursor.fetchone()

    connection.close()

    return customer

def insert_corporate_customer(customer):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO corporate_customers
        (company_name, cnpj, address)
        VALUES (?, ?, ?)
        """,
        (
            customer.company_name,
            customer.cnpj,
            customer.address,
        ),
    )

    connection.commit()
    connection.close()

def find_corporate_customer_by_cnpj(cnpj):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM corporate_customers
        WHERE cnpj = ?
        """,
        (cnpj,),
    )

    customer = cursor.fetchone()

    connection.close()

    return customer