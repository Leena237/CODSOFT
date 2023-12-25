class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = addr

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts
                          if search_term.lower() in contact.name.lower() or
                          search_term in contact.phone]
        return found_contacts

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            addr = input("Enter contact address: ")
            new_contact = Contact(name, phone, email, addr)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            try:
                index = int(input("Enter the index of the contact to update: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    name = input("Enter new contact name: ")
                    phone = input("Enter new contact phone number: ")
                    email = input("Enter new contact email: ")
                    addr = input("Enter new contact address: ")
                    updated_contact = Contact(name, phone, email, addr)
                    contact_book.update_contact(index, updated_contact)
                    print("Contact updated successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "5":
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    contact_book.delete_contact(index)
                    print("Contact deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "6":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()