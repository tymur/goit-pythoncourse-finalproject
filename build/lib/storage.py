import json
from models import Note, Contact
from colorama import Fore

NOTES_FILE = "notes.json"
CONTACTS_FILE = "contacts.json"

class Storage:
    @staticmethod
    def save_notes(notes, filename=NOTES_FILE):
        data = [
            {
                "title": note.title,
                "content": note.content,
                "tags": note.tags
            }
            for note in notes
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(Fore.GREEN + "Нотатки успішно збережено.")

    @staticmethod
    def load_notes(filename=NOTES_FILE):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                # Перевірка ключів даних для відладки
                print("Завантажені дані нотаток:", data)
                # Переконайтеся, що ключі 'title', 'content' і 'tags' існують
                return [Note(**note_data) for note_data in data]
        except FileNotFoundError:
            print(Fore.RED + "Файл з нотатками не знайдено. Створюємо новий файл.")
            return []
        except TypeError as e:
            print(Fore.RED + f"Помилка у форматі JSON: {e}")
            return []

    @staticmethod
    def save_contacts(contacts, filename=CONTACTS_FILE):
        data = [
            {
                "name": contact.name,
                "address": contact.address,
                "phone": contact.phone,
                "email": contact.email,
                "birthday": contact.birthday
            }
            for contact in contacts
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(Fore.GREEN + "Контакти успішно збережено.")

    @staticmethod
    def load_contacts(filename=CONTACTS_FILE):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            print(Fore.RED + "Файл з контактами не знайдено. Створюємо новий файл.")
            return []
