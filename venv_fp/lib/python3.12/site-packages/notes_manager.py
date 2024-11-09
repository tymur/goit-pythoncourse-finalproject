from storage import Storage
from models import Note
from colorama import Fore
from prettytable import PrettyTable

class NotesManager:
    def __init__(self):
        self.notes = Storage.load_notes()

    def add_note(self, title, content, tags=None):
        new_note = Note(title=title, content=content, tags=tags)
        self.notes.append(new_note)
        Storage.save_notes(self.notes)
        print(Fore.GREEN + "Нотатку успішно додано.")

    def edit_note(self, title, field, new_value):
        note = self.find_note_by_title(title)
        if note:
            setattr(note, field, new_value)
            Storage.save_notes(self.notes)
            print(Fore.GREEN + f"Нотатку '{title}' оновлено.")
        else:
            print(Fore.RED + "Нотатку не знайдено.")

    def delete_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                Storage.save_notes(self.notes)
                print(Fore.GREEN + f"Нотатку з назвою '{title}' видалено.")
                return
        print(Fore.RED + f"Нотатку з назвою '{title}' не знайдено.")

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        print(Fore.RED + f"Нотатку з назвою '{title}' не знайдено.")
        return None

    def display_all_notes(self):
        if not self.notes:
            print(Fore.RED + "Немає нотаток для відображення.")
            return

        table = PrettyTable()
        table.field_names = ["Назва", "Зміст", "Теги"]
        for note in self.notes:
            tags_formatted = ", ".join(note.tags) if note.tags else "Немає"
            table.add_row([note.title, note.content, tags_formatted])
        print(table)

    def find_notes_by_tag(self, tag):
        # Фільтруємо нотатки за тегом
        results = [note for note in self.notes if tag in note.tags]
        
        if results:
            # Відображаємо результати у вигляді таблиці
            table = PrettyTable()
            table.field_names = ["Назва", "Зміст", "Теги"]
            for note in results:
                tags_formatted = ", ".join(note.tags) if note.tags else "Немає"
                table.add_row([note.title, note.content, tags_formatted])
            print(Fore.GREEN + f"Знайдено нотатки з тегом '{tag}':")
            print(table)
        else:
            print(Fore.RED + f"Нотаток з тегом '{tag}' не знайдено.")
