def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("")
    number = input("")
    email = input("")
    address = input("")

    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
	    "phone": number,
	    "email": email,
	    "address": address
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    contact_name = input()

    if contact_name in contact_book:
        details = contact_book[contact_name]
        print("Name: " + contact_name)
        print("Phone: " + details["phone"])
        print("Email: " + details["email"])
        print("Address: " + details["address"])  
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    usr_contact = input()

    if usr_contact in contact_book:
        new_phone = input()
        new_email = input()
        new_address = input()

        new_details = contact_book[usr_contact]

        if new_phone:
            new_details["phone"] = new_phone
        if new_email:
            new_details["email"] = new_email
        if new_address:
            new_details["address"] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    delete_cntct = input()

    if delete_cntct not in contact_book:
        print("Contact not found!")
    else:
        contact_book.pop(delete_cntct)
        print("Contact deleted successfully!")

def list_all_contacts(contact_book):

    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print("Name: " + name)
            print("Phone: " + details["phone"])
            print("Email: " + details["email"])   
            print("Address: " + details["address"])
            print("")


contact_book = {}

while True:
    display_menu()
    choice = input()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")