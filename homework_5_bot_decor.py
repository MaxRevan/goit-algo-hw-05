def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            return "Give me name please."
        
    return inner    

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number: {contacts[name]}"
    else:
        raise KeyError
    
@input_error
def show_all_contacts(args, contacts):
    if len(args) != 0:
        return "Invalid command format. Use: all"
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Set command (hello, add, change, phone, all, exit):")
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
            print(show_all_contacts(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
