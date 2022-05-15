USERS = {}


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


def hello_handler(_):
    return 'How can I help you?'


def exit_handler(_):
    return


@handler_error
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f'User {name} added'


@handler_error
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f'{name} have new phone: {phone}. Old phone: {old_phone}.'


@handler_error
def show_all(_):
    result = ''
    for k, v in USERS.items():
        result += f'{k}, {v}\n'
    return result


@handler_error
def show_number(args):
    user = args[0]
    phone = USERS[user]
    return f'{user}: {phone}'


def unknown_cmd(_):
    return "Unknown command"


HANDLERS = {
    "hello": hello_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
    u"add": add_user,
    u"change": change_phone,
    u"show all": show_all,
    u"phone": show_number
}


def main():
    while True:
        user_input = input('>>> ')
        cmd, *args = user_input.split()
        try:
            handler = HANDLERS[cmd.lower()]
        except KeyError:
            if args:
                cmd = cmd + ' ' + args[0]
                args = args[1:]
            handler = HANDLERS.get(cmd.lower(), unknown_cmd)
        result = handler(args)
        if not result:
            print('Good bye!')
            break
        print(result)


if __name__ == '__main__':
    main()