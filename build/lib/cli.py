from notes_manager import NotesManager
from contacts_manager import ContactsManager
from colorama import Fore, Style, init
from prettytable import PrettyTable

# Ініціалізуємо colorama для кольорового виводу
init(autoreset=True)

def display_menu():
    # Виведемо меню у вигляді таблиці
    menu_table = PrettyTable()
    menu_table.field_names = ["Номер", "Опис команди"]
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
        # Відображаємо меню
        display_menu()

        # Отримуємо вибір користувача
        choice = input("Оберіть дію: ").strip()
        print(f"{Fore.BLUE}Вибір користувача: {choice}{Style.RESET_ALL}")  # Виводимо вибір для відладки

        if choice == "1":
            # Додати контакт
            name = input("Введіть ім'я: ")
            address = input("Введіть адресу: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть електронну пошту: ")
            birthday = input("Введіть день народження (YYYY-MM-DD): ")
            contacts_manager.add_contact(name, address, phone, email, birthday)
            print(Fore.GREEN + "Контакт додано.")

        elif choice == "4":
            # Показати всі контакти
            contacts_manager.display_all_contacts()

        elif choice == "5":
            # Додати нотатку
            title = input("Введіть назву нотатки: ")
            content = input("Введіть зміст нотатки: ")
            tags = input("Введіть теги через кому: ").split(",")
            notes_manager.add_note(title, content, tags)
            print(Fore.GREEN + "Нотатку додано.")

        elif choice == "8":
            # Показати всі нотатки
            notes_manager.display_all_notes()

        elif choice == "0":
            # Вихід з програми
            print(Fore.GREEN + "До побачення!")
            break

        else:
            print(Fore.RED + "Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
