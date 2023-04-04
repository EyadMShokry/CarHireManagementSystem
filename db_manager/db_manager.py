import mysql.connector


class DatabaseManager:
    """
    A class to manage connections to a MySQL database.

    Attributes:
        host (str): The host of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username for the MySQL server.
        password (str): The password for the MySQL server.
        database (str): The name of the MySQL database to use.
        conn (mysql.connector.connection): The active MySQL connection.
        cursor (mysql.connector.cursor): The cursor for the active MySQL connection.
    """

    def __init__(self, host, port, user, password, database):
        """
        Initializes a new instance of the DatabaseManager class.

        Args:
            host (str): The host of the MySQL server.
            port (int): The port number of the MySQL server.
            user (str): The username for the MySQL server.
            password (str): The password for the MySQL server.
            database (str): The name of the MySQL database to use.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Creates a new MySQL connection and cursor and returns the manager instance.

        Returns:
            DatabaseManager: The manager instance.
        """
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commits any pending changes and closes the MySQL connection and cursor.

        Args:
            exc_type (type): The type of any exception that occurred.
            exc_val (Exception): The exception that occurred.
            exc_tb (traceback): The traceback for the exception that occurred.
        """
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.cursor.close()
        self.conn.close()

    def execute(self, query: str, values: tuple = ()):
        """
        Executes a SQL query on the active connection and returns the result.

        Args:
            query (str): The SQL query to execute.
            values (tuple): Optional arguments to use with the query.

        Returns:
            list: A list of rows returned by the query.
        """
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def execute_and_commit(self, query: str, values: tuple = ()):
        """
        Executes a SQL query on the active connection and commits the changes.

        Args:
            query (str): The SQL query to execute.
            values (tuple): Optional arguments to use with the query.
        """
        self.cursor.execute(query, values)
        self.conn.commit()

    def execute_and_return_lastrowid(self, query: str, values: tuple = ()):
        """
        Executes a SQL query on the active connection and returns the last inserted row ID.

        Args:
            query (str): The SQL query to execute.
            values (tuple): Optional arguments to use with the query.

        Returns:
            int: The ID of the last inserted row.
        """
        self.cursor.execute(query, values)
        return self.cursor.lastrowid

    # def get_cursor(self):
    #     """Returns a cursor object for executing queries on the connected database.
    #
    #     Returns:
    #         mysql.connector.cursor_cext.Cursor: A cursor object for executing queries on the connected database.
    #     """
    #     return self.conn.cursor()
