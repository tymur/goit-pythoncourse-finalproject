from notes_manager import NotesManager
from contacts_manager import ContactsManager
from colorama import Fore, Style, init
from prettytable import PrettyTable
from validation import validate_phone, validate_email

init(autoreset=True)

def display_menu():
    menu_table = PrettyTable()
    menu_table.field_names = ["Номер", "Опис дії"]
    menu_table.add_rows([
        ["1", "Додати контакт"],
        ["2", "Редагувати контакт"],
        ["3", "Видалити контакт"],
        ["4", "Показати всі контакти"],
        ["5", "Додати нотатку"],
        ["6", "Редагувати нотатку"],
        ["7", "Видалити нотатку"],
        ["8", "Показати всі нотатки"],
        ["9", "Пошук нотаток за тегом"],
        ["0", "Вийти"]
    ])
    print(menu_table)

def main():
    notes_manager = NotesManager()
    contacts_manager = ContactsManager()

    while True:
        display_menu()
        choice = input("Оберіть дію (введіть номер): ").strip()

        if choice == "1":
            name = input("Введіть ім'я: ")
            address = input("Введіть адресу: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть електронну пошту: ")
            birthday = input("Введіть день народження (YYYY-MM-DD): ")

            if validate_phone(phone) and validate_email(email):
                contacts_manager.add_contact(name, address, phone, email, birthday)
            else:
                print(Fore.RED + "Невірний формат телефону або електронної пошти.")

        elif choice == "2":
            name = input("Введіть ім'я контакту для редагування: ")
            contact = contacts_manager.find_contact_by_name(name)
            if contact:
                print("Що ви хочете змінити?")
                print("1. Ім'я")
                print("2. Адресу")
                print("3. Номер телефону")
                print("4. Електронну пошту")
                print("5. День народження")
                sub_choice = input("Оберіть дію: ").strip()

                if sub_choice == "1":
                    new_name = input("Введіть нове ім'я: ")
                    contact.edit_name(new_name)
                elif sub_choice == "2":
                    new_address = input("Введіть нову адресу: ")
                    contact.edit_address(new_address)
                elif sub_choice == "3":
                    new_phone = input("Введіть новий номер телефону: ")
                    if validate_phone(new_phone):
                        contact.edit_phone(new_phone)
                    else:
                        print(Fore.RED + "Невірний формат номера телефону.")
                elif sub_choice == "4":
                    new_email = input("Введіть нову електронну пошту: ")
                    if validate_email(new_email):
                        contact.edit_email(new_email)
                    else:
                        print(Fore.RED + "Невірний формат електронної пошти.")
                elif sub_choice == "5":
                    new_birthday = input("Введіть новий день народження (YYYY-MM-DD): ")
                    contact.edit_birthday(new_birthday)
                else:
                    print(Fore.RED + "Некоректний вибір.")
                contacts_manager.edit_contact(name, sub_choice, new_birthday)

        elif choice == "3":
            name = input("Введіть ім'я контакту для видалення: ")
            contacts_manager.delete_contact(name)

        elif choice == "4":
            contacts_manager.display_all_contacts()

        elif choice == "5":
            title = input("Введіть назву нотатки: ")
            content = input("Введіть зміст нотатки: ")
            tags = input("Введіть теги через кому: ").split(",")
            notes_manager.add_note(title, content, tags)

        elif choice == "6":
            title = input("Введіть назву нотатки для редагування: ")
            note = notes_manager.find_note_by_title(title)
            if note:
                print("Що ви хочете змінити?")
                print("1. Назву")
                print("2. Зміст")
                print("3. Теги")
                sub_choice = input("Оберіть дію: ")

                if sub_choice == "1":
                    new_title = input("Введіть нову назву: ")
                    note.edit_title(new_title)
                elif sub_choice == "2":
                    new_content = input("Введіть новий зміст: ")
                    note.edit_content(new_content)
                elif sub_choice == "3":
                    new_tags = input("Введіть нові теги через кому: ").split(",")
                    note.edit_tags(new_tags)
                else:
                    print(Fore.RED + "Некоректний вибір.")
                notes_manager.edit_note(title, sub_choice, new_tags)

        elif choice == "7":
            title = input("Введіть назву нотатки для видалення: ")
            notes_manager.delete_note_by_title(title)

        elif choice == "8":
            notes_manager.display_all_notes()

        elif choice == "9":
            tag = input("Введіть тег для пошуку: ")
            notes_manager.find_notes_by_tag(tag)

        elif choice == "0":
            print(Fore.GREEN + "До побачення!")
            break

        else:
            print(Fore.RED + "Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
