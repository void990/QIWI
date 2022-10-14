import rich
import os, sys
import banner

from SimpleQIWI import *
from rich.console import Console
from config import token, phone_number

console = Console()

api = QApi(token=token, phone=phone_number)

console.print(
'''
Author: https://github.com/void990/qiwi
0.1 (Test Version!)
''', style = "bold white"
)

banner.banner(text='QIWI')

console.print('''[bold white]

[1] Wallet balance
[2] Transfer money
''')

main = console.input('[red]>>[/] ')

if main == "1":

   balance = api.balance
   
   console.print(f'[red]Your balance[/]> [white]{balance}')


elif main == "2":
     try:
        phone = console.input('[red]Recipients phone[/]> ')
        amount = console.input('[red]Transfer amount[/]> ')
        comment = console.input('[red]Comment[/]> ')
     
        api.pay(
          account=phone, 
          amount=1, 
          comment=comment
        )
        
        console.print('[green]The payment has been sent!')
        
     except:
           console.input('[bold red]Payment is not possible!\n')
           sys.exit()
