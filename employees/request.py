from models import employee
import sqlite3
import json
from models import Employee


EMPLOYEES = [
    {
        "id": 1,
        "name": "Michael Baumer",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Courtney Baumer",
        "locationId": 2
    },
    {
        "name": "Ben Baumer",
        "locationId": 1,
        "animalId": 1,
        "id": 3
    },
    {
        "name": "Ella Baumer",
        "locationId": 2,
        "animalId": 2,
        "id": 4
    },
    {
        "name": "Test Bob",
        "locationId": 1,
        "animalId": 0,
        "id": 5
    }
]


def get_all_employees():
    with sqlite3.connect("kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.name,
          e.location_id
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)
    return json.dumps(employees)

# Function with a single parameter


def get_single_employee(id):
    with sqlite3.connect("kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.name,
          e.location_id
        FROM Employee e
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['location_id'])
        return json.dumps(employee.__dict__)


def get_employee_by_location(location):

    with sqlite3.connect("kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, (location))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break


def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
