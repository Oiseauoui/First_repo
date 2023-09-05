def read_users_data():
    return {
        "kate": "+380507380000",
        "tom": "+30667774455",
        "bob": "+30667774455",
        "ben": "+380501230000",
        "emily": "+380992520022",
    }

def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return None  # Return None instead of the error message
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'
    return wrapper

def add_contact(contacts, name, phone):
    contacts[name.lower()] = phone
    print(f"Added {name} with phone number {phone}.")

def change_contact(contacts, name, phone):
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        print(f"Contact information updated for {name}.")
    else:
        print("Contact not found.")

def find_contact(contacts, name):
    if name.lower() in contacts:
        return contacts[name.lower()]
    else:
        return None

def show_all_contacts(contacts):
    return contacts

def handle_hello():
    print("How can I help you?")

def handle_goodbye():
    print("Goodbye! Have a nice day!")

def handle_add(contacts):
    def inner():
        name_phone_input = input("Enter name and phone: ")
        name_phone_parts = name_phone_input.split(maxsplit=1)
        if len(name_phone_parts) != 2:
            print("Please input both name and phone")  # Print the message
        else:
            name, phone = name_phone_parts
            add_contact(contacts, name, phone)
    return inner

def handle_change(contacts):
    def inner():
        name_phone_input = input("Enter name and new phone: ")
        name_phone_parts = name_phone_input.split(maxsplit=1)
        if len(name_phone_parts) != 2:
            print("Please input both name and phone")  # Print the message
        else:
            name, phone = name_phone_parts
            change_contact(contacts, name, phone)
    return inner

def handle_phone(contacts):
    def inner():
        name = input("Enter name: ").lower()
        phone = find_contact(contacts, name)
        if phone:
            print(f"Phone number for {name} is {phone}")
        else:
            print("Contact not found.")
    return inner

def handle_show_all(contacts):
    def inner():
        all_contacts = show_all_contacts(contacts)
        for name, phone in all_contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print()  # Print an empty line between contacts
    return inner

def handle_goodbye_and_exit():
    print("Goodbye! Have a nice day!")
    exit()  # Exit the program

def main():
    contacts = read_users_data()
    print("Hi!")

    handlers = {
        "hello": handle_hello,
        "hi": handle_hello,
        "good bye": handle_goodbye_and_exit,
        "close": handle_goodbye_and_exit,
        "exit": handle_goodbye_and_exit,
        "add": handle_add(contacts),
        "change": handle_change(contacts),
        "phone": handle_phone(contacts),
        "show all": handle_show_all(contacts),
    }

    while True:
        user_input = input('Enter command for bot: ')
        if user_input in handlers:
            handlers[user_input]()
        else:
            print("Invalid command. How can I help you?")

if __name__ == "__main__":
    main()
