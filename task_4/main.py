class CommandHandler:
    def __init__(self, contact_book):
        self.contact_book = contact_book
    
    def add_contact(self, name, phone):
        self.contact_book[name] = phone
        print('Contact added.')
    
    def change_contact(self, name, phone):
        if name in self.contact_book:
            self.contact_book[name] = phone
            print('Contact updated.')
        else:
            print('Contact not found.')
    
    def show_phone(self, name):
        if name in self.contact_book:
            print(self.contact_book[name])
        else:
            print('Contact not found.')
    
    def show_all(self):
        if self.contact_book:
            for name, phone in self.contact_book.items():
                print(f'{name}: {phone}')
        else:
            print('Contact book is empty.')

class CLI:
    def __init__(self):
        self.contact_book = {}
        self.command_handler = CommandHandler(self.contact_book)
    
    def greeting(self):
        print("Welcome to the assistant bot!")
    
    def run_command(self, command, args):
        if command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            name, phone = args
            self.command_handler.add_contact(name, phone)
        elif command == "change" and len(args) == 2:
            name, phone = args
            self.command_handler.change_contact(name, phone)
        elif command == "phone" and len(args) == 1:
            name = args[0]
            self.command_handler.show_phone(name)
        elif command == "all":
            self.command_handler.show_all()
        elif command in ["close", "exit"]:
            print("Good bye!")
            return True
        else:
            print("Invalid command.")
        return False

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def main():
    cli_bot = CLI()
    cli_bot.greeting()
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, args = parse_input(user_input)
        
        if cli_bot.run_command(command, args):
            break

if __name__ == "__main__":
    main()

