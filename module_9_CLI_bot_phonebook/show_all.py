# show_all.py

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."

    contacts_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contacts_list
