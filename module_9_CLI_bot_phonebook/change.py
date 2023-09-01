# change.py

from pathlib import Path

def change_contact(file_path, contacts, name, new_phone):
    name = name.lower()
    if name in contacts:
        contacts[name] = new_phone

        # Update the contact in the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for i, line in enumerate(lines):
                if line.startswith(f"name: {name}, phone: "):
                    lines[i] = f"name: {name}, phone: {new_phone},\n"

            file.writelines(lines)
        
        return f"Changed phone number for {name} to {new_phone}."
    else:
        return "Contact not found."
