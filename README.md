# Mini-Project: Contact Management System

- Author: Jaycob Hoffman

- Date: 11 July 2024

## Documentation

The Contact Management System is a CLI application that allows the user to easily create and manage a contact list in a simple manner.

### Main Features

- **Add a new contact**: With the ```Add a new contact``` feature, the user can add contacts one at a time. They can enter the contact's name, phone number, and email address, as well as any additional info they see fit (notes, address, etc.), if desired.
- **Edit an existing contact**: With the ```Edit an existing contact``` feature, the user can edit a selected contact within their list. They can change the contact's name, phone number, email address, and/or additional info.
- **Delete a contact**: With the ```Delete a contact``` feature, the user can delete a selected contact within their list.
- **Search for a contact**: With the ```Search for a contact``` feature, the user can search for and display a contact within their list.
- **Display all contacts**: With the ```Display all contacts``` feature, the user can display their contact list in a formatted, easy-to-read manner.
- **Export contacts to a text file**: With the ```Export contacts to a text file``` feature, the user can create a text file to export their formatted contact list to.

### Bonus Features

- **Case Insensitivity**: Where applicable, all user inputs are case-insensitive.

### UI

When the user first runs the Contact Management System, the following UI will display:

```
Welcome to the Contact Management System!

Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Quit

Please select an option from the menu above by entering it's corresponding number:
```

The user can select an option from the menu by entering the number that precedes it. When the task has finished, the menu will display again and prompt the user to select another option. This cycle will continue indefinitely until the user selects option #7 and quits the program. Then, the following message will display:

```
Quitting program. Thank you for using the Contact Management System!
```

When created, the user's contact list will appear as follows:

```
Contacts:

John Doe:
Phone Number - 1234567890
Email Address - johndoe@email.com
Additional Info - Lorem ipsum dolor sit amet

Jane Doe:
Phone Number - 0987654321
Email Address - janedoe@email.com
Additional Info - consectetur adipisci elit
```

### Errors

The Contact Management System will raise ```ValueError```s with accompanying messages under the following circumstances:

- If the user leaves a field blank where they are not allowed to do so (e.g., leaving a contact's name blank).
- If the user enters an invalid input (e.g., an incorrectly formatted email address).
- If the user tries to add a contact whose name already exists in the system. The same goes for if the user edits a contact's name to be a name that already exists.
- If the user searches for a contact whose name does not exist in the system.
- If the user enters a non-numeric value when selecting a menu option.
- If the user enters a numeric value that does not have a corresponding menu option when selecting a menu option.

#

View the Contact Management System [GitHub Repository](https://github.com/JaycobHoffman1/mini-project-contact-management-system).