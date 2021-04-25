from secret import Secret
from menu import menu, create, find, find_accounts

sr = Secret()
secret = sr.get_secret_key()

passw = input(
    'Please provide the master password to start using password Manager:')
if passw == secret:
    print('acces granted')
else:
    print('acess denied')
    exit()

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    elif choice == '2':
        find_accounts()
    elif choice == '3':
        find()
    choice = menu()
exit()
