# parse command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add name phone
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command format. Use 'add username phone'."

# change username phone
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return f"No contact found with the name '{name}'."
    else:
        return "Invalid command format. Use 'change username phone'."

# phone username
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"No contact found with the name '{name}'."
    else:
        return "Invalid command format. Use 'phone username'."

# all
def show_all(contacts):
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
Enter a command: add Dmytro +38095111222333
Contact added.
Enter a command: add Oleg +380508887777
Contact added.
Enter a command: change Dmytro +19999999999
Contact updated.
Enter a command: all
All contacts:
Dmytro: +19999999999
Oleg: +380508887777
Enter a command: add Vasyl +4805555555
Contact added.
Enter a command: all
All contacts:
Dmytro: +19999999999
Oleg: +380508887777
Vasyl: +4805555555
Enter a command: phone Vasyl
+4805555555
Enter a command: hello
How can I help you?
Enter a command: exit
Good bye!
'''