from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

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

    def __str__(self):
        field_str = "\n".join([str(field) for field in self.fields])
        return f"Name: {self.name}\nFields:\n{field_str}"

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


# Example usage:
if __name__ == "__main__":
    address_book = AddressBook()

    record1 = Record("John Doe")
    record1.add_field(Phone("+123456789"))
    record1.add_field(Phone("+987654321"))
    address_book.add_record(record1)

    record2 = Record("Jane Smith")
    record2.add_field(Phone("+111222333"))
    address_book.add_record(record2)

    # Search for records containing "John" or "+987654321" in either name or phone
    search_criteria = ["Jane", "+111222333"]
    results = address_book.search_records(search_criteria)

    for result in results:
        print(result)
