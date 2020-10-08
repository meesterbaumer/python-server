ANIMALS = [
    {
      "id": 1,
      "name": "Fern",
      "breed": "Mutt",
      "customerId": 4,
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Redd",
      "breed": "Red Tick Coonhound",
      "customerId": 5,
      "locationId": 1
    },
    {
      "name": "Maddie",
      "breed": "Cat",
      "locationId": 2,
      "customerId": 4,
      "id": 3
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal