import os

os.system("")

class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_error(message):
    print(f"{Style.RED}{Style.BOLD}{'ERROR'+' ':>12}{Style.RESET}{message}")

def print_status(status,message):
    print(f"{Style.GREEN}{Style.BOLD}{status+' ':>12}{Style.RESET}{message}")
