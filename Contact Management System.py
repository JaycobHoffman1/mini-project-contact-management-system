import re

phone_number_pattern = r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}"
email_address_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"

# Ensures user input is not blank or composed entirely of spaces
def check_input(user_input, input_type):
    while True:
        try:
            _input = input(user_input).strip()

            if len(_input) == 0 or len(_input) == _input.count(" "):
                raise ValueError(f"{input_type} cannot be blank.")
        except ValueError as v:
            print(v)
        else:
            return _input

# Performs "check_input()" function while also checking user input against given regex       
def validate_input(user_input, input_type, pattern):
    while True:
        try:
            _input = check_input(user_input, input_type.capitalize())

            if not re.search(pattern, _input):
                raise ValueError(f"Invalid {input_type}.")
        except ValueError as v:
            print(v)
        else:
            return _input

''' "validate_input()" function refactored for "edit_existing()" function,
returns if user input is blank or is composed entirely of spaces'''
def validate_input_edit(user_input, input_type, pattern):
    while True:
        _input = input(user_input)

        if len(_input) != 0 and len(_input) != _input.count(" "):
            try:
                if not re.search(pattern, _input):
                    raise ValueError(f"Invalid {input_type}.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
        return False

# Checks if contact already exists  
def check_if_exists(contact_dict, contact_name):
    try:
        if contact_dict.get(contact_name, False):
            raise ValueError("\nLooks like this contact already exists!")
    except ValueError as v:
        print(v)

        return True

# Adds contact
def add_contact(contact_dict):
    print("\nAdd a new contact:\n")

    # Takes and validates contact info
    contact_name = check_input("Enter contact's name: ", "Name")
    phone_number = re.sub(r"\D", r"", validate_input("Enter contact's phone number: ", \
    "phone number", phone_number_pattern))
    email_address = validate_input("Enter contact's email address: ", \
    "email address", email_address_pattern)
    additional_info = check_input("*OPTIONAL - TYPE \"none\" TO EXCLUDE* \
Enter any additional information (address, notes, etc.): ", "Field")

    if check_if_exists(contact_dict, contact_name):
        return
    
    # Adds contact to dictionary if contact doesn't already exist
    contact_dict[contact_name] = {"Phone Number": phone_number, "Email Address": email_address}

    # Adds "Additional Info" if value is not "none"
    if additional_info.lower().strip() != "none":
        contact_dict[contact_name]["Additional Info"] = additional_info

    print("\nContact added!")

# Edits existing contact
def edit_existing(contact_dict):
    print("\nEdit a contact:\n")

    # Checks if dictionary is empty
    if not contact_dict:
        print("Nothing to edit! Your contact list is empty.")

        return

    # Checks if contact exists in dictionary
    try:
        contact_to_find = check_input("Enter the contact name you wish to edit: ", "Field")

        for contact_name in contact_dict.keys():
            if contact_name.lower() == contact_to_find.lower():
                
                # Takes and validates new contact info
                new_contact_name = input("\nEnter contact's new name (leave blank to keep unchanged): ")
                new_phone_number = validate_input_edit("Enter contact's new phone number (leave blank to keep unchanged): ", \
                "phone number", phone_number_pattern)
                new_email_address = validate_input_edit("Enter contact's new email address (leave blank to keep unchanged): ", \
                "email address", email_address_pattern)
                new_additional_info = input("*OPTIONAL - TYPE \"none\" TO EXCLUDE* \
Enter any additional information (leave blank to keep unchanged): ")
                
                if check_if_exists(contact_dict, new_contact_name):
                    return

                # Replaces old contact info if any old info was changed above
                if new_phone_number:
                    new_phone_number = re.sub(r"\D", r"", new_phone_number)
                    contact_dict[contact_name]["Phone Number"] = new_phone_number

                if new_email_address:
                    contact_dict[contact_name]["Email Address"] = new_email_address
                
                # Includes additional check to ensure "Additional Info" does not equal "none"
                if contact_dict[contact_name].get("Additional Info", False) and new_additional_info.lower().strip() == "none":
                    del contact_dict[contact_name]["Additional Info"]
                elif len(new_additional_info) != 0 and len(new_additional_info) != new_additional_info.count(" "):
                    contact_dict[contact_name]["Additional Info"] = new_additional_info

                if len(new_contact_name) != 0 and len(new_contact_name) != new_contact_name.count(" "):
                    contact_dict[new_contact_name] = contact_dict.pop(contact_name)

                print("\nContact edited!")

                return
            
        # If entered contact wasn't found
        raise ValueError("\nContact not found.")
    except ValueError as v:
        print(v)

# Deletes contact
def delete_contacts(contact_dict):
    print("\nDelete a contact:\n")

    # Checks if dictionary if empty
    if not contact_dict:
        print("Nothing to delete! Your contact list is empty.")

        return

    # Checks if contact exists in dictionary
    try:
        contact_to_find = check_input("Enter the contact name you wish to delete: ", "Field")

        for contact_name in contact_dict.keys():
            if contact_name.lower() == contact_to_find.lower():
                del contact_dict[contact_name]

                print(f"\nContact deleted!")

                return
        
        # If entered contact wasn't found
        raise ValueError("\nContact not found.")
    except ValueError as v:
        print(v)

# Searches for and displays contact
def search_contacts(contact_dict):
    print("\nSearch for a contact:\n")

    # Checks if dictionary is empty
    if not contact_dict:
        print("Nothing to search for! Your contact list is empty.")

        return

    # Checks if contact exists in dictionary
    try:
        contact_to_find = check_input("Search for contact name: ", "Field")

        for contact_name in contact_dict.keys():
            if contact_name.lower() == contact_to_find.lower():

                # Displays found contact in formatted manner
                print(f"\nContact {contact_name} found!\n\n{contact_name}:")

                for detail in contact_dict[contact_name].keys():
                    print(f"{detail} - {contact_dict[contact_name][detail]}")

                return
        
        # If entered contact wasn't found
        raise ValueError("\nContact not found.")
    except ValueError as v:
        print(v)

# Displays contacts in formatted manner
def display_contacts(contact_dict):
    print("\nDisplay All Contacts:\n")

    # Checks if dictionary is empty
    if not contact_dict:
        print("Nothing to display! Your contact list is empty.")

        return
    
    print("Contacts:")

    # Prints contacts in formatted manner
    for identifier, details in contact_dict.items():
        print(f"\n{identifier}:")

        for detail in details.keys():
            print(f"{detail} - {details[detail]}")

# Exports contacts to .txt file in formatted manner
def export_contacts(contact_dict):
    print("\nExport Contacts to a Text File:\n")

    # Checks if dictionary is empty
    if not contact_dict:
        print("Nothing to export! Your contact list is empty.")

        return

    file_name = check_input("Name the file you wish to export contacts to: ", "File name")

    # Appends .txt extension if not entered by user
    if not re.search(r".txt$", file_name):
        file_name += ".txt"

    # Writes formatted contact list to user-created file
    with open(file_name, "w") as file:
        file.write("Contacts:")

        for identifier, details in contact_dict.items():
            file.write(f"\n\n{identifier}:")

            for detail in details.keys():
                file.write(f"\n{detail} - {details[detail]}")
            
    print("\nExported successfully!")

def main():
    user_contacts = {} # Contact list -- details stored in nested dictionaries

    print("\nWelcome to the Contact Management System!")

    while True:
        print("\nMenu:\n\
1. Add a new contact\n\
2. Edit an existing contact\n\
3. Delete a contact\n\
4. Search for a contact\n\
5. Display all contacts\n\
6. Export contacts to a text file\n\
7. Quit\n")
        
        # Ensures user input is within range of numbers that appear on the menu
        while True:
            try:
                user_selection = int(check_input("Please select an option from the menu above \
by entering it's corresponding number: ", "Selection"))

                if user_selection < 1 or user_selection > 8:
                    raise ValueError("Please enter a valid numeric value and ensure it appears on the menu.")
            except ValueError as v:
                print(v)
            else:
                break

        if user_selection == 1:
            add_contact(user_contacts)
        elif user_selection == 2:
            edit_existing(user_contacts)
        elif user_selection == 3:
            delete_contacts(user_contacts)
        elif user_selection == 4:
            search_contacts(user_contacts)
        elif user_selection == 5:
            display_contacts(user_contacts)
        elif user_selection == 6:
            export_contacts(user_contacts)
        elif user_selection == 7:
            print("\nQuitting program. Thank you for using the Contact Management System!\n")

            break # Quits program

if __name__ == "__main__":
    main()