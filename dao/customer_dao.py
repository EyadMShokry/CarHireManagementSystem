from models.customer import Customer


class CustomerDAO:
    """Data Access Object for the Customer model."""

    def __init__(self, db_manager):
        """
        Constructor for CustomerDAO class.

        Args:
            db_manager (DatabaseManager): The database manager instance to use.
        """
        self.db_manager = db_manager

    def create_customer(self, name, email, phone, address):
        """
        Create a new customer to the database.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.
            phone (str): The phone number of the customer.
            address (str): The address of the customer.

        Returns:
            int: The ID of the newly created customer record.
        """
        query = 'INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)'
        values = (name, email, phone, address)
        self.db_manager.execute_query(query, values)
        return self.db_manager.get_cursor().lastrowid

    def get_customer(self, id) -> Customer:
        """
        Retrieve a customer from the database.

        Args:
            id (int): The ID of the customer to retrieve.

        Returns:
            dict: A dictionary representation of the customer record.
        """
        query = 'SELECT * FROM customers WHERE id=%s'
        values = (id)
        result = self.db_manager.execute_query(query, values)
        if result:
            customer = Customer(*result[0])
            return customer
        else:
            return None

    def update_customer(self, id, name, email, phone, address):
        """
        Update an existing customer in the database.

        Args:
            id (int): The ID of the customer to update.
            name (str): The updated name of the customer.
            email (str): The email of the customer.
            phone (str): The updated phone number of the customer.
            address (str): The updated address of the customer.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        query = 'UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s'
        values = (name, email, phone, address, id)
        result = self.db_manager.execute_query(query, values)
        return result > 0

    def delete_customer(self, id):
        """
        Delete a customer from the database.

        Args:
            id (int): The ID of the customer to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        query = 'DELETE FROM customers WHERE id=%s'
        values = (id)
        result = self.db_manager.execute_query(query, values)
        return result > 0
