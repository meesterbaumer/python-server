CUSTOMERS = [
    {
      "email": "meestercourtney@mac.com",
      "password": "1234",
      "name": "Courtney Baumer",
      "address": "2620 Wellesley Square Drive",
      "id": 4
    },
    {
      "email": "MeesterBaumer@mac.com",
      "password": "1234",
      "name": "Michael Baumer",
      "address": "2620 Wellesley Square Drive",
      "id": 5
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer