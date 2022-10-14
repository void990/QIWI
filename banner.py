import pyfiglet

def banner(text: str) -> str:
    banner = pyfiglet.figlet_format(text, font='slant')
    return print(banner)
