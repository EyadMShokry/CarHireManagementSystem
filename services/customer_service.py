from typing import List
from models.customer import Customer
from dao.customer_dao import CustomerDAO


class CustomerService:
    """
    This class represents the service layer for the Customer entity.

    Attributes:
        customer_dao (CustomerDAO): An instance of the CustomerDAO class to interact with the data layer.
    """

    def __init__(self, customer_dao: CustomerDAO):
        """
        Constructs a new instance of the CustomerService class.

        Args:
            customer_dao (CustomerDAO): An instance of the CustomerDAO class to interact with the data layer.
        """
        self.customer_dao = customer_dao

    def create_customer(self, name: str, email: str, phone: str, address: str):
        """
        Creates a new Customer object and saves it to the database.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.
            phone (str): The phone number of the customer.
            address (str): The address of the customer.

        Returns:
            Customer: The newly created Customer object.
        """
        customer = Customer(name=name, email=email, phone=phone, address=address)
        customer_id = self.customer_dao.create_customer(customer)
        return customer_id

    def get_customer(self, customer_id: int):
        """
        Retrieves a Customer object with the specified ID from the database.

        Args:
            customer_id (int): The ID of the customer to retrieve.

        Returns:
            Customer: The Customer object with the specified ID.
        """
        customer = self.customer_dao.get_customer(customer_id)
        if customer is None:
            return
        return customer

    def update_customer(self, customer_id: int, name: str = None, email: str = None,
                        phone: str = None, address: str = None) -> Customer:
        """
        Updates a Customer object with the specified ID in the database.

        Args:
            customer_id (int): The ID of the customer to update.
            name (str, optional): The updated name of the customer. Defaults to None.
            email (str, optional): The updated email of the customer. Defaults to None.
            phone (str, optional): The updated phone number of the customer. Defaults to None.
            address (str, optional): The updated address of the customer. Defaults to None.

        Returns:
            Customer: The updated Customer object.

        Raises:
            ValueError: If no customer is found with the specified ID.
        """
        customer = self.customer_dao.get_customer(customer_id)
        if customer is None:
            raise ValueError(f"No customer found with ID {customer_id}")

        if name is not None and name != "":
            customer.name = name
        if email is not None and email != "":
            customer.email = email
        if phone is not None and phone != "":
            customer.phone = phone
        if address is not None and address != "":
            customer.address = address

        self.customer_dao.update_customer(customer)

        return customer

    def delete_customer(self, customer_id: int):
        """
        Deletes a Customer object with the specified ID from the database.

        Args:
            customer_id (int): The ID of the customer to delete.

        Raises:
            ValueError: If no customer is found with the specified ID.
        """
        customer = self.customer_dao.get_customer(customer_id)
        if customer is None:
            return

        self.customer_dao.delete_customer(customer.id)
        return customer.id