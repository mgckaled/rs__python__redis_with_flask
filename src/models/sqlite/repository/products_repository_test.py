import pytest

from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.sqlite.settings.connection import SqliteConnectionHandler

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()


@pytest.mark.skip(reason="interação com o banco")
def test_insert_product() -> None:
    repo = ProductsRepository(conn)

    name = "algumaCoisa2"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)


pytest.mark.skip(reason="interação com o banco")


def test_find_product() -> None:
    repo = ProductsRepository(conn)

    name = "algumaCoisa2"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
