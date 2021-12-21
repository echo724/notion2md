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

def _formatted_print(left,right,error=False):
    color = Style.RED if error else Style.GREEN
    print()
    print(f"{color}{Style.BOLD}{left+' ':>12}{Style.RESET}{right}")
    print()

def print_error(message):
    _formatted_print("ERROR",message)

def print_status(status,message):
    _formatted_print(status,message)
