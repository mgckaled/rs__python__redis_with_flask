from redis import Redis


class RedisConnectioHanddler:
    def __init__(self) -> None:
        """
        Initializes a new instance of the RedisConnectionHandler class.

        Sets up an attribute to store the Redis connection.
        """

        self.__redis_conn = None

    def connect(self) -> Redis:
        """
        Establishes a connection to a Redis server and stores it in the instance.

        Returns:
            Redis: A Redis connection object.
        """

        redis_conn = Redis(host='localhost', port=6379, db=0)
        self.__redis_conn = redis_conn
        return redis_conn

    def get_connection(self) -> Redis:
        """
        Gets the Redis connection stored in the instance.

        Returns:
            Redis: A Redis connection object.
        """
        return self.__redis_conn
