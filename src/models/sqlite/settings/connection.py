import sqlite3
from sqlite3 import Connection as SqliteConnection


class SqliteConnectionHandler:
    def __init__(self) -> None:
        """
        Initializes a new instance of the SqliteConnectionHandler class.

        Sets up an attribute to store the connection string and another
        attribute to store the connection object.
        """
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> SqliteConnection:
        """
        Establishes a connection to a SQLite database and stores it in the instance.

        Uses the connection string specified in the constructor to open a connection to
        the database. The connection is configured to not check for the same thread
        to avoid issues with Python's Global Interpreter Lock (GIL).

        Returns:
            SqliteConnection: A SQLite connection object.
        """
        conn = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False
        )
        self.__conn = conn
        return conn

    def get_connection(self) -> SqliteConnection:
        """
        Gets the SQLite connection stored in the instance.

        Returns:
            SqliteConnection: A SQLite connection object.
        """
        return self.__conn
