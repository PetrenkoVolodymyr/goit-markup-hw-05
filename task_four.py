#DECORATORS
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"
        except IndexError:
            return "Enter user name"
    return inner


#MAIN FUNCTIONS
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        contacts[name] = int(phone)
        return "Contact added."
    else:
        return "Contact already exists."
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = int(phone)
    return "Contact updated."

@input_error
def get_contact(args, contacts):
    return contacts[args[0]]



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
        elif command == "all":
            print(contacts)
        elif command == "phone":
            print(get_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()