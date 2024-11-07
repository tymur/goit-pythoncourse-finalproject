from contacts_manager import ContactsManager
from notes_manager import NotesManager
from colorama import Fore, Style

def main():
    contacts_manager = ContactsManager()
    notes_manager = NotesManager()

    while True:
        print(Fore.CYAN + "\nКоманди:")
        print("1. Додати контакт")
        print("2. Редагувати поле контакту")
        print("3. Видалити поле контакту")
        print("4. Видалити контакт")
        print("5. Показати контакти")
        print("6. Показати контакти з днем народження через N днів")
        print("7. Додати нотатку")
        print("8. Редагувати нотатку")
        print("9. Видалити нотатку")
        print("10. Показати нотатки")
        print("11. Пошук нотаток за тегом")
        print("0. Вихід" + Style.RESET_ALL)

        command = input(Fore.YELLOW + "\nВведіть команду: " + Style.RESET_ALL)

        # Робота з контактами
        if command == "1":
            name = input("Ім'я: ")
            address = input("Адреса: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            birthday = input("День народження (рррр-мм-дд): ")
            contacts_manager.add_contact(name, address, phone, email, birthday)

        elif command == "2":
            index = int(input("Індекс контакту для редагування: "))
            field = input("Поле для редагування (name, address, phone, email, birthday): ").lower()
            new_value = input(f"Нове значення для {field}: ")
            contacts_manager.edit_contact_field(index, field, new_value)

        elif command == "3":
            index = int(input("Індекс контакту для видалення поля: "))
            field = input("Поле для видалення (name, address, phone, email, birthday): ").lower()
            contacts_manager.delete_contact_field(index, field)

        elif command == "4":
            index = int(input("Індекс контакту для видалення: "))
            contacts_manager.delete_contact(index)

        elif command == "5":
            contacts_manager.show_contacts()

        elif command == "6":
            days = int(input("Введіть кількість днів: "))
            contacts_manager.find_birthdays(days)

        # Робота з нотатками
        elif command == "7":
            content = input("Введіть текст нотатки: ")
            tags = input("Введіть теги через кому: ").split(", ")
            notes_manager.add_note(content, tags)

        elif command == "8":
            index = int(input("Індекс нотатки для редагування: "))
            content = input("Новий текст нотатки (залиште порожнім для пропуску): ")
            tags = input("Нові теги через кому (залиште порожнім для пропуску): ").split(", ")
            notes_manager.edit_note(index, content if content else None, tags if tags != [''] else None)

        elif command == "9":
            index = int(input("Індекс нотатки для видалення: "))
            notes_manager.delete_note(index)

        elif command == "10":
            notes_manager.show_notes()

        elif command == "11":
            tag = input("Введіть тег для пошуку: ")
            notes_manager.search_by_tag(tag)

        elif command == "0":
            print(Fore.MAGENTA + "Дякуємо за використання Персонального помічника!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Невідома команда. Спробуйте ще раз." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
