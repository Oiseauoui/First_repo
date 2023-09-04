
def read_users_data():
    return {
        "kate": "+380507380000",
        "tom": "+30667774455",
        "bob": "+30667774455",
        "ben": "+380501230000",
        "emily": "+380992520022",
    }

def input_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            print("Error: Invalid input format or contact not found.")
    return wrapper

@input_error_handler
def add_contact(contacts):
    name_phone_input = input("Enter name and phone: ")
    name, phone = name_phone_input.split(maxsplit=1)
    contacts[name.lower()] = phone
    print(f"Added {name} with phone number {phone}.")

@input_error_handler
def change_contact(contacts, name, phone):
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        print(f"Contact information updated for {name}.")
    else:
        print("Contact not found.")

@input_error_handler
def find_contact(contacts, name):
    if name.lower() in contacts:
        print(f"Phone number for {name} is {contacts[name.lower()]}")
    else:
        print("Contact not found.")

def show_all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print()  # Print an empty line between contacts

def main():
    contacts = read_users_data()
    print("Hi!")

    while True:
        user_input = input().lower()

        if user_input == "hello" or user_input == "hi":
            print("How can I help you?")
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye! Have a nice day!")
            break
        elif user_input.startswith("add"):
            add_contact(contacts)
        elif user_input.startswith("change"):
            name_phone_input = input("Enter name and new phone: ")
            name, phone = name_phone_input.split(maxsplit=1)
            change_contact(contacts, name, phone)
        elif user_input.startswith("phone"):
            name = input("Enter name: ").lower()
            find_contact(contacts, name)
        elif user_input == "show all":
            show_all_contacts(contacts)
        else:
            print("Invalid command. How can I help you?")

if __name__ == "__main__":
    main()
