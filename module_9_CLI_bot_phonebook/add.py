# add.py

from pathlib import Path

def add_contact(file_path, contacts, name, phone):
    contacts[name.lower()] = phone

    with open(file_path, 'a') as file:
        file.write(f"name: {name}, phone: {phone},\n")

    return f"Added {name} with phone number {phone}."
