from collections import UserDict


class AddressBook(UserDict):
    def add(self, record):
        if record.name not in self.data:
            self.data[record.name] = record
        else:
            self.data[record.name].add_phones(record.phones)

    def edit(self, old_record, new_record):
        if old_record.name not in self.data:
            return
        self.data[old_record.name].update_phone(old_record.phones[0], new_record.phones[0])

    def delete(self, record):
        if record.name in self.data:
            self.data.pop(record.name)


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        if phones is None:
            self.phones = []
        else:
            self.phones = phones
        self.birthday = birthday

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def add_phones(self, phone_numbers):
        self.phones.extend(phone_numbers)

    def update_phone(self, old_phone, new_phone):
        index = 0
        for idx, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                index = idx
                break
        self.phones[index] = new_phone


class Field:
    pass


class Name:
    pass


class Phone:
    pass
