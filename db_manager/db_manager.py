import mysql.connector
from flask import g


class DatabaseManager:
    """
    A class to manage connections to a MySQL database using Flask.

    Attributes:
        host (str): The hostname of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password to connect to the MySQL server.
        database (str): The name of the database to connect to.

    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        """
        Initializes the DatabaseManager with the provided configuration.

        Args:
            host (str): The hostname of the MySQL server.
            port (int): The port number of the MySQL server.
            user (str): The username to connect to the MySQL server.
            password (str): The password to connect to the MySQL server.
            database (str): The name of the database to connect to.

        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def get_db(self):
        """
        Returns a connection to the MySQL database, creating a new one if necessary.

        Returns:
            mysql.connector.connection.MySQLConnection: A connection to the MySQL database.

        """
        if 'db' not in g:
            g.db = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return g.db

    def close_db(self, exception=None):
        """
        Closes the current connection to the MySQL database, if one exists.

        Args:
            exception: Any exception that occurred, if applicable.

        """
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def init_app(self, app):
        """
        Registers the DatabaseManager with the provided Flask application.

        Args:
            app: The Flask application to register with.

        """
        app.teardown_appcontext(self.close_db)
        app.config['DATABASE'] = self

    def execute_query(self, query: str, values: tuple = ()):
        """
        Executes the provided SQL query on the database and returns the result.

        Args:
            query (str): The SQL query to execute.
            values (tuple): The values to use in the query.

        Returns:
            List[Tuple]: The result of the query.

        """
        cursor = self.get_db().cursor()
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return result