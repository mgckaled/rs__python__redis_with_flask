from flask import Flask

from src.main.routes.products_routes import products_routes_bp
from src.models.redis.settings.connection import RedisConnectioHanddler
from src.models.sqlite.settings.connection import SqliteConnectionHandler

redis_connection_handle = RedisConnectioHanddler()
sqlite_connection_handle = SqliteConnectionHandler()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

app = Flask(__name__)


app.register_blueprint(products_routes_bp)
