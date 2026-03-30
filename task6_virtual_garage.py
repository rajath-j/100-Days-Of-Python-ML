# task6_virtual_garage.py

# 1. Create an empty dictionary to store vehicles in the garage
garage = {}

print("Welcome to your Virtual Garage!")

# 2. Main Menu Loop
while True:
    print("\n--- Menu ---")
    print("1. Add a Vehicle")
    print("2. View All Vehicles")
    print("3. Search for a Vehicle")
    print("4. Update Vehicle Details")
    print("5. Remove a Vehicle")
    print("6. Exit")

    choice = input("\nChoose an option (1-6): ")

    # 3. Add a Vehicle - stores nested dictionary with vehicle details
    if choice == '1':
        license_plate = input("Enter license plate number: ")

        # Check if vehicle already exists
        if license_plate in garage:
            print("A vehicle with this license plate already exists!")
        else:
            make = input("Enter vehicle make (e.g., Toyota, Honda): ")
            model = input("Enter vehicle model: ")
            year = input("Enter vehicle year: ")
            color = input("Enter vehicle color: ")

            # Store vehicle details as a nested dictionary
            garage[license_plate] = {
                'make': make,
                'model': model,
                'year': year,
                'color': color
            }
            print("Vehicle added successfully!")

    # 4. View All Vehicles - displays all vehicles in the garage
    elif choice == '2':
        if len(garage) == 0:
            print("Your garage is empty!")
        else:
            print("\n--- All Vehicles in Garage ---")
            for plate, details in garage.items():
                print(f"\nLicense Plate: {plate}")
                print(f"  Make: {details['make']}")
                print(f"  Model: {details['model']}")
                print(f"  Year: {details['year']}")
                print(f"  Color: {details['color']}")
            print("-----------------------------")

    # 5. Search for a Vehicle - find by license plate
    elif choice == '3':
        search_plate = input("Enter license plate to search: ")
        if search_plate in garage:
            details = garage[search_plate]
            print(f"\nVehicle Found:")
            print(f"  License Plate: {search_plate}")
            print(f"  Make: {details['make']}")
            print(f"  Model: {details['model']}")
            print(f"  Year: {details['year']}")
            print(f"  Color: {details['color']}")
        else:
            print("Vehicle not found in garage.")

    # 6. Update Vehicle Details - modify existing vehicle info
    elif choice == '4':
        update_plate = input("Enter license plate of vehicle to update: ")
        if update_plate in garage:
            print(f"\nCurrent details for {update_plate}:")
            print(f"  Make: {garage[update_plate]['make']}")
            print(f"  Model: {garage[update_plate]['model']}")
            print(f"  Year: {garage[update_plate]['year']}")
            print(f"  Color: {garage[update_plate]['color']}")

            print("\nEnter new details (press Enter to keep current value):")
            new_make = input(f"  Make ({garage[update_plate]['make']}): ")
            new_model = input(f"  Model ({garage[update_plate]['model']}): ")
            new_year = input(f"  Year ({garage[update_plate]['year']}): ")
            new_color = input(f"  Color ({garage[update_plate]['color']}): ")

            # Update only if new value provided
            if new_make:
                garage[update_plate]['make'] = new_make
            if new_model:
                garage[update_plate]['model'] = new_model
            if new_year:
                garage[update_plate]['year'] = new_year
            if new_color:
                garage[update_plate]['color'] = new_color

            print("Vehicle updated successfully!")
        else:
            print("Vehicle not found.")

    # 7. Remove a Vehicle - delete from garage
    elif choice == '5':
        del_plate = input("Enter license plate to remove: ")
        if del_plate in garage:
            del garage[del_plate]
            print(f"Vehicle {del_plate} removed from garage.")
        else:
            print("Vehicle not found.")

    # 8. Exit the program
    elif choice == '6':
        print(f"\nGoodbye! You have {len(garage)} vehicle(s) in your garage.")
        break

    # 9. Handle invalid input
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
