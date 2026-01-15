contacts = []


def add_contact():
    name = input('Name ')
    phone = input('Phone number ')
    email = input('Email ')
    contact_name = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact_name)


def view_all_contacts():
    if len(contacts) == 0:
        print('No contact found')
    else:
        i = 1
        for contact in contacts:
            print(f'Contact {i}'.center(20, '-'))
            print(f'''Name: {contact['name']}
Phone# :{contact['phone']}
Email: {contact['email']}
''')
            i += 1


def search_contact_by_name():
    search_name = input('Name> ').lower()
    for name in contacts:
        if name['name'].lower() == search_name:
            print(f'''Name: {name['name']}
Contact: {name['phone']}
Email :{name['email']}
''')
            return
    print(f'Sorry contact with name {search_name} not found')


def delete_contact():
    contact_name = input('Name> ').lower()
    for contact in contacts:
        if contact['name'].lower() == contact_name:
            contacts.remove(contact)
            return
    print(f'{contact_name} not found')


def update_contact():
    if len(contacts) == 0:
        print(f'Contact book is empty. Create a contact in the main menu')
        return
    i = 0
    while True:
        contact_name = input('Name> ').lower()
        for contact in contacts:
            if contact['name'].lower() == contact_name:
                while True:
                    choice = int(input(f'''What do you want to update?
1: Name
2: Phone
3: Email
4: Exit to Main Menu
Choice> '''))
                    if choice == 1:
                        name = input('Enter a new name: ')
                        contact['name'] = name
                    elif choice == 2:
                        phone = input('Enter a new phone number: ')
                        contact['phone'] = phone
                    elif choice == 3:
                        email = input('Enter a new email: ')
                        contact['email'] = email
                    elif choice == 4:
                        return
                    else:
                        print('Invalid choice. Try again.')
                return  # exit after updating
        print(f'{contact_name} not found. Try another name.')
        i += 1
        if i >= 3:
            print(f'Sorry wrong name go back to main menu')
            return


while True:
    user_choice = int(input(f'''1:Add Contact
2:View All Contacts
3:Search Contact
4:Delete Contact
5:Update Contact
6:Exit
'''))
    if user_choice == 1:
        add_contact()
    elif user_choice == 2:
        view_all_contacts()
    elif user_choice == 3:
        search_contact_by_name()
    elif user_choice == 4:
        delete_contact()
    elif user_choice == 5:
        update_contact()
    elif user_choice == 6:
        print('Exiting')
        break
