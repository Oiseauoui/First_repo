from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class InvalidPhoneNumberError(Exception):
    def __init__(self, phone_number):
        super().__init__(f"Invalid phone number format: {phone_number}")

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        # Use regular expression to check for a valid phone number
        # The regex pattern matches a 10-digit number with optional plus sign at the beginning
        pattern = r'^\+?\d{10}$'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid phone number format: {value}")
        return True


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.fields = []

    def add_field(self, field):
        if isinstance(field, Field):
            self.fields.append(field)

    def remove_field(self, field_type):
        self.fields = [f for f in self.fields if not isinstance(f, field_type)]

    def edit_field(self, field_type, new_value):
        for field in self.fields:
            if isinstance(field, field_type):
                field.value = new_value

    def find_field(self, field_type):
        for field in self.fields:
            if isinstance(field, field_type):
                return field

    def add_phone(self, phone_number):
        try:
            new_phone = Phone(phone_number)
            self.add_field(new_phone)
        except InvalidPhoneNumberError as e:
            print(f"Error: {e}")

    def remove_phone(self, phone_number):
        self.fields = [f for f in self.fields if not (isinstance(f, Phone) and f.value == phone_number)]

    def edit_phone(self, old_phone_number, new_phone_number):
        phone_field = self.find_field(Phone)
        if phone_field and phone_field.value == old_phone_number:
            phone_field.value = new_phone_number
        else:
            raise ValueError("Phone number does not exist")

    def find_phone(self, phone_number):
        for field in self.fields:
            if isinstance(field, Phone) and field.value == phone_number:
                return field
        return None

class AddressBook(UserDict):
    def add_record(self, record):
        if isinstance(record, Record):
            self.data[record.name.value] = record

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]

    def search_records(self, criteria):
        results = []
        for record in self.values():
            criteria_matched = False
            for criteria_value in criteria:
                if (
                    str(record.name).lower() == criteria_value.lower()
                    or any(
                        str(field).lower() == criteria_value.lower()
                        for field in record.fields
                    )
                ):
                    criteria_matched = True
                    break

            if criteria_matched:
                results.append(record)

        return results

    # New method for finding a record by name
    def find(self, name):
        return self.data.get(name)

    # New method for deleting a record by name
    def delete(self, name):
        if name in self.data:
            del self.data[name]

def input_error(function):
    """
    A decorator to handle errors that may occur due to user input.
    :param function: User input function.
    :return: Either the operation of the function or the text with an error, to be re-entered.
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError:
            return None  # Return None instead of the error message
        except IndexError:
            return 'Please provide the required input'
        except TypeError:
            return 'Wrong command.'
    return wrapper

@input_error
def hello_func():
    return "How can I help you?"

@input_error
def exit_func():
    return "Goodbye! Have a nice day!"

@input_error
def add_func(data, name, phone):
    data[name.lower()] = phone
    return f"Added {name} with phone number {phone}."

@input_error
def change_func(data, name, phone):
    if name.lower() in data:
        data[name.lower()] = phone
        return f"Contact information updated for {name}."
    else:
        return "Contact not found."

@input_error
def show_func(data):
    result = []
    for name, phone in data.items():
        result.append(f"Name: {name}")
        result.append(f"Phone: {phone}")
        result.append("")  # Print an empty line between contacts
    return "\n".join(result)

@input_error
def phone_func(data, name):
    phone = data.get(name.lower())
    if phone:
        return f"Phone number for {name} is {phone}"
    else:
        return "Contact not found."

def handle_hello(user_input):
    print(hello_func())

def handle_exit(user_input):
    print(exit_func())
    return True  # Signal to exit the loop

def handle_add(contacts_dict):
    while True:
        name = input("Enter name: ").strip()
        if any(char.isdigit() for char in name):
            print("Name cannot contain numeric characters")
            continue  # Continue the loop if name is numeric
        phone = input("Enter phone: ").strip()
        if not phone.strip().replace("+", "").isdigit():
            print("Phone must be a numeric value, not a string")
            continue  # Continue the loop if phone contains letters
        try:
            add_result = add_func(contacts_dict, name, phone)
            if add_result:
                print(add_result)
            break  # Exit the loop if successful
        except ValueError:
            pass  # Suppress the error message and return None

def handle_change(contacts_dict):
    name = input("Enter name: ").strip()
    phone = input("Enter new phone: ").strip()
    change_result = change_func(contacts_dict, name, phone)
    if change_result:
        print(change_result)

def handle_show(contacts_dict):
    show_result = show_func(contacts_dict)
    if show_result:
        print(show_result)

def handle_phone(contacts_dict):
    name = input("Enter name: ").strip()
    phone_result = phone_func(contacts_dict, name)
    if phone_result:
        print(phone_result)

# ... (previous code)

def main():
    contacts_dict = AddressBook()

    print("Hi!")

    command_handlers = {
        'hello': handle_hello,
        'hi': handle_hello,
        'exit': handle_exit,
        'add': handle_add,
        'change': handle_change,
        'show all': handle_show,
        'phone': handle_phone,
    }

    while True:
        user_input = input('Enter command for bot: ')
        handler = command_handlers.get(user_input)
        if handler:
            if handler(contacts_dict):
                break
        else:
            print("Invalid command. How can I help you?")

if __name__ == "__main__":
    main()
