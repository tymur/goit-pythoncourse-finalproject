import re
from colorama import Fore

def validate_phone(phone):
    if re.match(r"^\+?1?\d{9,15}$", phone):
        print(Fore.GREEN + "Телефон пройшов валідацію.")
        return True
    else:
        print(Fore.RED + "Невірний формат телефону. Будь ласка, введіть коректний номер.")
        return False

def validate_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        print(Fore.GREEN + "Електронна пошта пройшла валідацію.")
        return True
    else:
        print(Fore.RED + "Невірний формат електронної пошти. Будь ласка, введіть коректну адресу.")
        return False
