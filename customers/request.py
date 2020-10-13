import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 4,
        "name": "Courtney Baumer",
        "address": "2620 Wellesley Square Drive",
        "email": "meestercourtney@mac.com",
        "password": "1234"
    },
    {
        "id": 5,
        "name": "Michael Baumer",
        "address": "2620 Wellesley Square Drive",
        "email": "MeesterBaumer@mac.com",
        "password": "1234",
    }
]


def get_all_customers():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name,
            c.address
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['email'], row['password'],
                                row['name'], row['address'])
            customers.append(customer.__dict__)
    return json.dumps(customers)

# Function with a single parameter


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name,
            c.address
        FROM customer c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['email'],
                            data['password'], data['name'], data['address'],)

        return json.dumps(customer.__dict__)


def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break


def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
