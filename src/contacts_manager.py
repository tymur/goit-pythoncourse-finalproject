from storage import Storage
from models import Contact
from colorama import Fore
from prettytable import PrettyTable

class ContactsManager:
    def __init__(self):
        self.contacts = Storage.load_contacts()

    def add_contact(self, name, address, phone, email, birthday):
        new_contact = Contact(name=name, address=address, phone=phone, email=email, birthday=birthday)
        self.contacts.append(new_contact)
        Storage.save_contacts(self.contacts)
        print(Fore.GREEN + "Контакт успішно додано.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                Storage.save_contacts(self.contacts)
                print(Fore.GREEN + f"Контакт з ім'ям '{name}' видалено.")
                return
        print(Fore.RED + f"Контакт з ім'ям '{name}' не знайдено.")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        print(Fore.RED + f"Контакт з ім'ям '{name}' не знайдено.")
        return None

    def display_all_contacts(self):
        if not self.contacts:
            print(Fore.RED + "Немає контактів для відображення.")
            return

        # Відображаємо контакти у вигляді таблиці
        table = PrettyTable()
        table.field_names = ["Ім'я", "Адреса", "Телефон", "Email", "День народження"]
        for contact in self.contacts:
            table.add_row([contact.name, contact.address, contact.phone, contact.email, contact.birthday])

        print(table)