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

    def create_customer(self, customer: Customer):
        """
        Create a new customer to the database.

        Args:
            customer (Customer): The customer object to create.

        Returns:
            int: The ID of the newly created customer record.
        """
        query = "INSERT INTO Customer (name, email, phone_number, address) VALUES (%s, %s, %s, %s)"
        with self.db_manager as manager:
            return manager.execute_and_return_lastrowid(query,
                                                        (customer.name, customer.email, customer.phone,
                                                         customer.address))

    def get_customer(self, id) -> Customer:
        """
        Retrieve a customer from the database.

        Args:
            id (int): The ID of the customer to retrieve.

        Returns:
            dict: A dictionary representation of the customer record.
        """
        query = 'SELECT * FROM Customer WHERE id=%s'
        with self.db_manager as manager:
            row = manager.execute(query, (id,))
            if not row:
                return None
            return Customer(*row[0])

    def update_customer(self, customer: Customer):
        """
        Update an existing customer in the database.

        Args:
            customer (Customer): The customer object to update.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        query = 'UPDATE Customer SET name=%s, email=%s, phone_number=%s, address=%s WHERE id=%s'
        with self.db_manager as manager:
            result = manager.execute(query, (customer.name, customer.email, customer.phone, customer.address, customer.id))
            return result

    def delete_customer(self, id):
        """
        Delete a customer from the database.

        Args:
            id (int): The ID of the customer to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        query = 'DELETE FROM Customer WHERE id=%s'
        with self.db_manager as manager:
            manager.execute(query, (id,))
