import rich

from rich.console import Console
from rich.prompt import Prompt

console = Console()

console.rule('Requirements')

token = console.input('[bold yellow]api token from your qiwi[/]> ')
phone = console.input('[bold red]phone number[/]> ')

file = open('config.py', 'w')
file.write(f'token = "{token}"\nphone_number = "{phone}"')
file.close()

console.rule('Added :) https://t.me/WhiteTermux')

