class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_phone, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.phone == old_phone:
                self.contacts[i] = new_contact

    def delete_contact(self, phone):
        self.contacts = [contact for contact in self.contacts if contact.phone != phone]


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == '2':
            print("\nContact List:")
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for result in results:
                    print(f"Name: {result.name}, Phone: {result.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            old_phone = input("Enter the phone number of the contact to update: ")
            contact_to_update = contact_manager.search_contact(old_phone)
            if contact_to_update:
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone, email, address)
                contact_manager.update_contact(old_phone, new_contact)
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == '5':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_manager.delete_contact(phone)
            print("Contact deleted successfully!")

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()