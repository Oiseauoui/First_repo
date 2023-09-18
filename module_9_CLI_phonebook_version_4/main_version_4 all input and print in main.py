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

def main():
    contacts_dict = {
        "kate": "+380507380000",
        "tom": "+30667774455",
        "bob": "+30667774455",
        "ben": "+380501230000",
        "emily": "+380992520022"
    }
    
    print("Hi!")

    while True:
        user_input = input('Enter command for bot: ')
        if user_input == 'hello'or user_input == 'hi':
            print(hello_func())
        elif user_input == 'exit':
            print(exit_func())
            break
        elif user_input == 'add':
            while True:
                name = input("Enter name: ").strip()
                if name.strip().isdigit():
                    print("Name cannot be numeric")
                    break  # Exit the loop if name is numeric
                phone = input("Enter phone: ").strip()
                if not phone.strip().replace("+", "").isdigit():
                    print("Phone must be a numeric value, not a string")
                    break  # Exit the loop if phone contains letters
                try:
                    add_result = add_func(contacts_dict, name, phone)
                    if add_result:
                        print(add_result)
                    break  # Exit the loop if successful
                except ValueError:
                    pass  # Suppress the error message and return None
        

        elif user_input == 'change':
            name = input("Enter name: ").strip()
            phone = input("Enter new phone: ").strip()
            change_result = change_func(contacts_dict, name, phone)
            if change_result:
                print(change_result)

        elif user_input == 'show all':
            show_result = show_func(contacts_dict)
            if show_result:
                print(show_result)
                
        elif user_input == 'phone':
            name = input("Enter name: ").strip()
            phone_result = phone_func(contacts_dict, name)
            if phone_result:
                print(phone_result)
        else:
            print("Invalid command. How can I help you?")

if __name__ == "__main__":
    main()

