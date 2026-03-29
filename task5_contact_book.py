# task5_contact_book.py

# 1. Create an empty dictionary
contacts = {}

print("Welcome to your Digital Contact Book!")

while True:
    print("\n--- Menu ---")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. View All Contacts")
    print("4. Delete a Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added: " + name)

    elif choice == '2':
        search_name = input("Enter the name to find: ")
        if search_name in contacts:
            print(search_name + "'s number is: " + contacts[search_name])
        else:
            print("Contact not found.")

    elif choice == '3':
        if len(contacts) == 0:
            print("Your contact book is empty!")
        else:
            print("\n--- All Contacts ---")
            for name, number in contacts.items():
                print("  " + name + ": " + number)
            print("--------------------")

    elif choice == '4':
        del_name = input("Enter the name to delete: ")
        if del_name in contacts:
            del contacts[del_name]        
            print("Contact deleted: " + del_name)
        else:
            print("Contact not found.")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")