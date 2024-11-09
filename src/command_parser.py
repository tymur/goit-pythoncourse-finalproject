from validation import validate_phone, validate_email
from colorama import Fore

class CommandParser:
    def parse_command(self, command):
        command = command.lower().strip()

        # Вихід з програми
        if command in ["exit", "вийти", "0"]:
            return "exit", None

        # Додавання контактів
        elif command.startswith("додати контакт"):
            return "add_contact", command[14:].strip()

        # Редагування контактів
        elif command.startswith("редагувати контакт"):
            return "edit_contact", command[18:].strip()

        # Видалення контактів
        elif command.startswith("видалити контакт"):
            return "delete_contact", command[16:].strip()

        # Показати всі контакти
        elif command == "показати всі контакти":
            return "show_contacts", None

        # Додавання нотаток
        elif command.startswith("додати нотатку"):
            return "add_note", command[14:].strip()

        # Редагування нотаток
        elif command.startswith("редагувати нотатку"):
            return "edit_note", command[18:].strip()

        # Видалення нотаток
        elif command.startswith("видалити нотатку"):
            return "delete_note", command[16:].strip()

        # Показати всі нотатки
        elif command == "показати всі нотатки":
            return "show_notes", None

        # Пошук нотаток за тегом
        elif command.startswith("пошук нотаток за тегом"):
            return "find_notes_by_tag", command[21:].strip()
        
        elif command == "сортувати нотатки за тегами":
            return "sort_notes_by_tag", None

        # Якщо команда не розпізнана
        return None

    def execute(self, action, params, contacts_manager, notes_manager):
        if action == "add_contact":
            try:
                name, address, phone, email, birthday = map(str.strip, params.split(","))
                if validate_phone(phone) and validate_email(email):
                    contacts_manager.add_contact(name, address, phone, email, birthday)
                else:
                    print(Fore.RED + "Невірний формат телефону або електронної пошти.")
            except ValueError:
                print(Fore.RED + "Неправильний формат даних для додавання контакту.")

        elif action == "edit_contact":
            try:
                name, field, new_value = map(str.strip, params.split(","))
                if field == "phone" and not validate_phone(new_value):
                    print(Fore.RED + "Невірний формат номера телефону.")
                    return
                elif field == "email" and not validate_email(new_value):
                    print(Fore.RED + "Невірний формат електронної пошти.")
                    return
                contacts_manager.edit_contact(name, field, new_value)
            except ValueError:
                print(Fore.RED + "Неправильний формат даних для редагування контакту.")

        elif action == "delete_contact":
            contacts_manager.delete_contact(params)

        elif action == "show_contacts":
            contacts_manager.display_all_contacts()

        elif action == "add_note":
            try:
                title, content, tags = map(str.strip, params.split(","))
                tags = tags.split(" ") if tags else []
                notes_manager.add_note(title, content, tags)
            except ValueError:
                print(Fore.RED + "Неправильний формат даних для додавання нотатки.")

        elif action == "edit_note":
            try:
                title, field, new_value = map(str.strip, params.split(","))
                notes_manager.edit_note(title, field, new_value)
            except ValueError:
                print(Fore.RED + "Неправильний формат даних для редагування нотатки.")

        elif action == "delete_note":
            notes_manager.delete_note_by_title(params)

        elif action == "show_notes":
            notes_manager.display_all_notes()

        elif action == "find_notes_by_tag":
            notes_manager.find_notes_by_tag(params)

        else:
            print(Fore.RED + "Команда не розпізнана. Спробуйте ще раз.")
