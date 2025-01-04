import array
class Contact_list():
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            return "No contacts in the list"
        else:
            print("contact list")
            for contact in self.contacts:
                print(contact)