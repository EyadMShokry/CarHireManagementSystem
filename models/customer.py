"""Customer Model Class."""


class Customer:
    """
    A class representing a customer.

    Attributes:
        id (int): The ID of the customer.
        name (str): The name of the customer.
        email (str): The email of the customer.
        phone (str): The phone number of the customer.
        address (str): The address of the customer.

    """

    def __init__(self, id=None, name=None, email=None, phone=None, address=None):
        """
        Initializes a new Customer object with the provided attributes.

        Args:
            id (int): The ID of the customer.
            name (str): The name of the customer.
            email (str): The email of the customer.
            phone (str): The phone number of the customer.
            address (str): The address of the customer.

        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
