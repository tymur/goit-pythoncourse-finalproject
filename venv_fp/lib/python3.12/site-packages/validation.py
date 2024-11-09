import re
from colorama import Fore, Style, init

# Ініціалізуємо colorama
init(autoreset=True)

def validate_phone(phone):
    """Перевіряє коректність номера телефону (+380XXXXXXXXX або XXXXXXXXXX)"""
    pattern = r"^\+?\d{10,15}$"  # Дозволяє формат +380XXXXXXXXX або 10-15 цифр без + в початку
    if re.match(pattern, phone):
        return True
    else:
        print(Fore.RED + "Некоректний номер телефону. Введіть номер у форматі +380XXXXXXXXX або XXXXXXXXXX.")
        return False

def validate_email(email):
    """Перевіряє коректність електронної пошти"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        print(Fore.RED + "Некоректна електронна пошта. Введіть коректну адресу (username@domain.com).")
        return False
