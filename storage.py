import json
from colorama import Fore, Style

class Storage:
    @staticmethod
    def save_data(data, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(data, f)
            print(Fore.GREEN + f"Дані збережено у {filename}!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Помилка збереження даних у {filename}: {e}" + Style.RESET_ALL)

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(Fore.RED + f"Помилка завантаження даних з {filename}: {e}" + Style.RESET_ALL)
            return []
