from prettytable import PrettyTable
from colorama import Fore, Style
from storage import Storage
from datetime import datetime, timedelta

CONTACTS_FILE = "contacts.json"

class Contact:
    """Клас, який представляє окремий контакт."""
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def to_dict(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "Phone": self.phone,
            "Email": self.email,
            "Birthday": self.birthday
        }

    def edit_field(self, field, new_value):
        """Редагує окреме поле контакту."""
        if hasattr(self, field):
            setattr(self, field, new_value)
            print(Fore.GREEN + f"Поле '{field}' оновлено успішно!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Поле '{field}' не існує!" + Style.RESET_ALL)


class ContactsManager:
    """Клас для управління контактами."""
    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts_data = Storage.load_data(CONTACTS_FILE)
        return [Contact(**contact) for contact in contacts_data]

    def save_contacts(self):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        Storage.save_data(contacts_data, CONTACTS_FILE)

    def add_contact(self, name, address, phone, email, birthday):
        new_contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(Fore.GREEN + "Контакт додано успішно!" + Style.RESET_ALL)

    def edit_contact_field(self, index, field, new_value):
        """Редагує окреме поле контакту за індексом."""
        try:
            contact = self.contacts[index]
            contact.edit_field(field, new_value)
            self.save_contacts()
        except IndexError:
            print(Fore.RED + "Контакт не знайдено!" + Style.RESET_ALL)

    def delete_contact_field(self, index, field):
        """Видаляє значення окремого поля контакту за індексом."""
        try:
            contact = self.contacts[index]
            if hasattr(contact, field):
                setattr(contact, field, None)
                self.save_contacts()
                print(Fore.GREEN + f"Поле '{field}' видалено успішно!" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Поле '{field}' не існує!" + Style.RESET_ALL)
        except IndexError:
            print(Fore.RED + "Контакт не знайдено!" + Style.RESET_ALL)

    def delete_contact(self, index):
        """Видаляє контакт за індексом."""
        try:
            self.contacts.pop(index)
            self.save_contacts()
            print(Fore.GREEN + "Контакт видалено успішно!" + Style.RESET_ALL)
        except IndexError:
            print(Fore.RED + "Контакт не знайдено!" + Style.RESET_ALL)

    def show_contacts(self):
        """Виводить список контактів у вигляді таблиці."""
        table = PrettyTable()
        table.field_names = ["Index", "Name", "Address", "Phone", "Email", "Birthday"]
        for i, contact in enumerate(self.contacts):
            table.add_row([i, contact.name, contact.address, contact.phone, contact.email, contact.birthday])
        print(table)

    def find_birthdays(self, days):
        """Шукає контакти з днем народження через задану кількість днів."""
        target_date = datetime.now() + timedelta(days=days)
        table = PrettyTable()
        table.field_names = ["Name", "Address", "Phone", "Email", "Birthday"]

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d")
            birthday_this_year = birthday.replace(year=datetime.now().year)

            if birthday_this_year == target_date:
                table.add_row([contact.name, contact.address, contact.phone, contact.email, contact.birthday])

        if table.rows:
            print(Fore.GREEN + f"Контакти з днем народження через {days} днів:" + Style.RESET_ALL)
            print(table)
        else:
            print(Fore.YELLOW + f"Немає контактів з днем народження через {days} днів." + Style.RESET_ALL)
