# Mini Project – Contact Book (Dictionary + Loop)

def print_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Found contact - Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def main():
    contacts = {}
    while True:
        print_menu()
        choice = input("Choose an option (1 - 5): ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting contact book , goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()