from  address_book import Record, AddressBook, Name, Phone, Birthday
import pickle

USERS = {}
DEFAULT_ADDRESS_BOOK_PATH = './.address_book.bin'


def dump_address_book(address_book):
    with open('./.address_book.bin', 'wb') as file:
        pickle.dump(address_book, file)


def load_address_book(path):
    try:
        with open(path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


def handler_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return 'No user with given me'
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner


def hello_handler():
    return 'How can I help you?'


def help_handler():
    return f'Available commands: {[i for i in HANDLERS.keys()]}'


@handler_error
def add_user():
    name = input('Input name: ')
    phone = input('Input phone: ')
    print(name, phone)
    record = Record(Name(name), [Phone(phone)])
    address_book.add(record)
    return f'Added new record: Name: {name}, Phone: {phone}'


@handler_error
def change_phone():
    name = input('Input Name: ')
    old_phone = input('Input old phone: ')
    new_phone = input('Input new phone: ')
    old_record = Record(Name(name), [Phone(old_phone)])
    new_record = Record(Name(name), [Phone(new_phone)])
    address_book.edit_record(old_record, new_record)
    return f'{name} have new phone: {new_phone}. Old phone: {old_phone}.'


@handler_error
def show_all():
    result = ''
    for page in address_book.iterator(2):
        result += page + '\n'
    return result


@handler_error
def show_number(args):
    user = args[0]
    phone = USERS[user]
    return f'{user}: {phone}'


@handler_error
def delete_handler():
    name = input('Input name: ')
    phone = input('Input phone: ')
    record = Record(Name(name), [Phone(phone)])
    address_book.delete(record)
    return f'Record with Name: {name} and Phone: {phone} deleted'


def exit_handler():
    print('Bye!')
    dump_address_book(address_book)


def unknown_cmd():
    return "Unknown command"


HANDLERS = {
    "hello": hello_handler,
    "help": help_handler,
    "good bye": exit_handler,
    "exit": exit_handler,
    u"add": add_user,
    u"edit": change_phone,
    u"delete": delete_handler,
    u"show all": show_all,
    u"phone": show_number
}

address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)


def main():
    print(f'Available commands: {[i for i in HANDLERS.keys()]}')
    while True:
        user_input = input('>>> ')
        cmd = user_input
        handler = HANDLERS.get(cmd.lower(), unknown_cmd)
        result = handler()
        if not result:
            break
        print(result)


if __name__ == '__main__':
    main()