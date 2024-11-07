import re
from colorama import Fore, Style

class Validator:
    @staticmethod
    def validate_phone(phone):
        pattern = re.compile(r"^\+?\d{10,}$")
        if pattern.match(phone):
            return True
        else:
            print(Fore.RED + "Некоректний номер телефону!" + Style.RESET_ALL)
            return False

    @staticmethod
    def validate_email(email):
        pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        if pattern.match(email):
            return True
        else:
            print(Fore.RED + "Некоректний email!" + Style.RESET_ALL)
            return False
