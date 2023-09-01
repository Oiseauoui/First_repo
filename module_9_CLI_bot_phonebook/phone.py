# phone.py

def get_phone(contacts, name):
    name = name.lower()
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}."
    else:
        return "Contact not found."
