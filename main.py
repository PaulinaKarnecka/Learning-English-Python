
from datetime import datetime
from sys import argv
from libs.db_connector import Base
from libs.game import Game
from libs.menu_content import MenuContent
from libs.player import Player
import os
import time


player = Player()
DB = Base()

try:
    arg_1 = argv[1]
    arg_2 = argv[2]
    print("Nowy słownik załadowany!")
except:
    arg_1 = False
    arg_2 = False

if arg_1 and arg_2:
    DB.table_seed(argv[1], argv[2])
    exit()

cleaner_command = 'cls'
continue_info = "\nWciśnij dowolny przycisk aby kontynuować..."
AUTH = False

if os.name == 'linux':
    cleaner_command = 'clear'


while True:   # menu loop
    os.system(cleaner_command)
    print(f"{MenuContent(player).main_menu}\n\n")
    user_choice = input("Wybór: ")
    try:
        user_choice = int(user_choice)
    except:
        print("Wybierz pozycję 1 - 5 i zatwierdź 'Enter'...")
        input(continue_info)
        
    if user_choice == 1:
        os.system(cleaner_command)
        result = player.register_user()
        print(result)
        time.sleep(2)
        
    elif user_choice == 2:
        os.system(cleaner_command)
        AUTH = player.confirm_user()
        if AUTH:
            player.login = AUTH['login']
            player.points = AUTH['points']
            player.last_login = datetime.now().strftime('%Y/%m/%d %H:%M')
        
    elif user_choice == 3:
        if AUTH:
            os.system(cleaner_command)
            Game(player)
        else:
            os.system(cleaner_command)
            print("Aby zagrać musisz się zalogować!")
            input(continue_info)
    elif user_choice == 4:
        if AUTH:
            os.system(cleaner_command)
            print(f"Statystyki gracza:\n\nlogin: {player.login}\npunkty: {player.points}\nostatnia gra: {player.last_login}")
            input(continue_info)
        else:
            os.system(cleaner_command)
            print("Aby zagrać musisz się zalogować!")
            input(continue_info)
            
    elif user_choice == 5:
        print("Dzięki za grę!")
        time.sleep(2)
        exit()
