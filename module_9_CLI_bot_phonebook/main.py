# main.py

from pathlib import Path


def get_script_directory():
    return Path(__file__).parent

def read_users_data(file_path):
    contacts = {}
    with open(file_path, 'r') as file:
        current_contact = {}
        for line in file:
            line = line.strip()
            if line.startswith("name: "):
                if current_contact:
                    contacts[current_contact['name']] = current_contact['phone']
                current_contact = {"name": line.replace("name: ", ""), "phone": None}
            elif line.startswith("phone: ") and current_contact.get('name') is not None:
                current_contact['phone'] = line.replace("phone: ", "")
                contacts[current_contact['name']] = current_contact['phone']
                current_contact = {}
    return contacts

def main():
    script_directory = get_script_directory()
    file_path = script_directory / "contact.txt"
    contacts = read_users_data(file_path)
    print("Hi!")

    while True:
        user_input = input().lower()
                  
        if user_input == "hello" or user_input == "hi":
            print("How can I help you?")
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye! Have a nice day!")
            break
        


        elif user_input.startswith("add"):
            while True:
                # Prompt the user for the name and phone number
                name_phone_input = input("Enter name and phone: ")

                # Split the input into name and phone, with error handling
                parts = name_phone_input.split(maxsplit=1)
                if len(parts) != 2:
                    print("Invalid input format. Please enter both name and phone number separated by a space.")
                    continue  # Restart the loop to get valid input

                name, phone = parts

                # Add the contact to the dictionary and update the file
                contacts[name.lower()] = phone

                with open(file_path, 'a') as file:
                    file.write(f"name: {name}, phone: {phone},\n")

                print(f"Added {name} with phone number {phone}.")
                break  # Exit the loop after successful addition



        elif user_input.startswith("change"):
            # Prompt the user for the name and new phone number
            name_phone_input = input("Enter name and new phone: ")
            
            # Split the input into name and phone, with error handling
            try:
                name, phone = name_phone_input.split(maxsplit=1)
            except ValueError:
                print("Invalid input format. Please enter both name and phone number separated by a space.")
                continue  # Restart the loop to get valid input

            # Initialize a flag to check if the contact was found
            contact_found = False

            # Read the existing data from the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Iterate through the lines to find and update the contact
            for i, line in enumerate(lines):
                if line.startswith(f"name: {name.lower()}, phone: "):
                    # Update the line with the new phone number
                    lines[i] = f"name: {name.lower()}, phone: {phone},\n"
                    contact_found = True
                    break

            # Write the modified lines back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

            # Check if the contact was found and updated
            if contact_found:
                print(f"Contact information updated for {name}.")
            else:
                print("Contact not found.")





        elif user_input.startswith("phone"):
            # file_path = Path(r"E:\PYTHON\PYTHON\Python Developer\Module 9\HM_4\contact.txt")

            users_data = []  # Initialize an empty list to store user data

            # Read data from the file and extract user information
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("name: ") and "phone: " in line:
                        name_start = line.find("name: ") + len("name: ")
                        name_end = line.find(",", name_start)
                        name = line[name_start:name_end].strip()

                        phone_start = line.find("phone: ") + len("phone: ")
                        phone = line[phone_start:].strip(",").strip()

                        users_data.append({"name": name, "phone": phone})

            # Get user input for a name
            name = input("Enter name: ").lower()  # Convert input to lowercase

            # Search for the name in the user data
            found = False
            for user in users_data:
                if user["name"].lower() == name:
                    print(f"Phone number for {user['name']} is {user['phone']}")
                    found = True
                    break

            if not found:
                print("Contact not found.")

            # print(users_data) 

        elif user_input == "show all":
            users_data = []  # Initialize an empty list to store user data
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("name: ") and "phone: " in line:
                        name_start = line.find("name: ") + len("name: ")
                        name_end = line.find(",", name_start)
                        name = line[name_start:name_end].strip()

                        phone_start = line.find("phone: ") + len("phone: ")
                        phone = line[phone_start:].strip(",").strip()

                        users_data.append({"name": name, "phone": phone})
                        
            for contact in users_data:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print()  # Print an empty line between contacts

        else:
            print("Invalid command. How can I help you?")


if __name__ == "__main__":
    main()

  
