# The Repository
import atexit
import sqlite3

from DAO import _Hats, _Suppliers, _Orders


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('true_database.db')
        self.hats = _Hats(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.orders = _Orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats (
            id      INT         PRIMARY KEY,
            topping    TEXT        NOT NULL,
            supplier    INT,
            quantity INT        NOT NULL,
            FOREIGN KEY(supplier)     REFERENCES suppliers(id),     
        );

        CREATE TABLE suppliers (
            id                 INT     PRIMARY KEY,
            name     TEXT    NOT NULL
        );

        CREATE TABLE orders (
            id      INT     PRIMARY KEY,
            location  TEXT     NOT NULL,
            hat           INT,

            FOREIGN KEY(hat)     REFERENCES hats(id),
            
            );
    """)


# the repository singleton
repo = _Repository()
atexit.register(repo._close)