def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter username and phone number."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


def parse_input(user_input): # parse command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts): # add name phone
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts): # change username phone
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts): # phone username
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts): # all
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts saved yet."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

''' INPUT -> OUTPUT:
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add Mikel +1895623741
Contact added.
Enter a command: add Georg +4896321784
Contact added.
Enter a command: add Olga +125847963 qwerty
Give me name and phone please.
Enter a command: add Olga +125847963
Contact added.
Enter a command: change Olga +111111111111
Contact updated.
Enter a command: phone Olga
+111111111111
Enter a command: all
All contacts:
Mikel: +1895623741
Georg: +4896321784
Olga: +111111111111
Enter a command: stramge_command
Invalid command.
Enter a command: exit
Good bye!
'''