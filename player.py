from libs.db_connector import Base
import getpass
import time


class Player():
    def __init__(self):
        self.query = Base()
        self.login = ''
        self.points = 0
        self.last_login = ''
        self.known_words = []
    
    def register_user(self):
        new_login = input("Podaj nowy login: ")
        new_passwd = input("Podaj hasło konta: ")
        if new_login and new_passwd:
            return self.query.insert_user([new_login, new_passwd])
        else:
            print("Pola nie mogą być puste!")
            time.sleep(2)
            
    
    def confirm_user(self):
        login = input("Wprowadź login użytkownika: ")
        passwd = input("Wprowadź hasło użytkownika: ")
        return self.query.check_and_return_user_data([login, passwd])
    
    def __del__(self):
        print(self.last_login)
        self.query.save_game(self.login, self.points, self.last_login)
        print("Gra zapisana pomyślnie!")