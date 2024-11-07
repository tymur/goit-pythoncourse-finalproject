from difflib import get_close_matches

class CommandParser:
    commands_list = [
        "add_contact", "edit_contact", "delete_contact", "show_contacts",
        "find_birthdays", "add_note", "edit_note", "delete_note", "show_notes"
    ]

    @staticmethod
    def suggest_command(user_input):
        matches = get_close_matches(user_input, CommandParser.commands_list, n=1, cutoff=0.6)
        if matches:
            print(f"Можливо, ви мали на увазі: {matches[0]}")
            return matches[0]
        else:
            print("Команда не розпізнана.")
            return None
