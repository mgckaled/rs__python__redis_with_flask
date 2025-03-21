from sqlite3 import Connection as SqliteConnection


class ProductsRepository:
    def __init__(self, conn: SqliteConnection) -> None:
        """
        Initializes a new instance of the ProductsRepository class.

        Args:
            conn: A SQLite connection object.
        """

        self.__conn = conn

    def find_product_by_name(self, product_name: str) -> tuple:
        """
        Finds a product in the database by its name.

        Args:
            product_name (str): The name of the product to search for.

        Returns:
            tuple: A tuple containing the product details if found, otherwise None.
        """

        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (product_name,)
        )
        product = cursor.fetchone()
        return product

    def insert_product(self, name: str, price: float, quantity: int) -> None:
        """
        Inserts a product into the database.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO products
                    (name, price, quantity)
                VALUES
                (?, ?, ?)
                ''',
            (name, price, quantity,)
        )
        self.__conn.commit()
