from employees.request import update_employee
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animal_by_location
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location
from customers import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer, get_customer_by_email
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee


# Here's a class. It inherits from another class.
class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/animals` or `/animals/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed
            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                elif resource == "animals":
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers()}"
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed
            if key == "email" and resource == "customers":
                response = get_customer_by_email(value)
            if key == "location_id" and resource == "animals":
                response = get_animal_by_location(value)
        self.wfile.write(response.encode())

    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return ( resource, key, value )
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass
            return (resource, id)

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_thing = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            new_thing = create_animal(post_body)
        if resource == "locations":
            new_thing = create_location(post_body)
        if resource == "employees":
            new_thing = create_employee(post_body)
        if resource == "customers":
            new_thing = create_customer(post_body)

        # Encode the new animal and send in response
        self.wfile.write(f"{new_thing}".encode())
      

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
        if resource == "customers":
            update_customer(id, post_body)
        if resource == "employees":
            update_employee(id, post_body)
        if resource == "locations":
            update_location(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)
        if resource == "customers":
            delete_customer(id)
        if resource == "employees":
            delete_employee(id)
        if resource == "locations":
            delete_location(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()