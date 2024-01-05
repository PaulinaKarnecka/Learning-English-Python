from datetime import datetime
import sqlite3
import json
import time

class Base():
    def __init__(self):
        self.con=sqlite3.connect("database/game.db")
        self.cur=self.con.cursor()
        # self.cur.execute("CREATE TABLE if not exists user (Dział,Ilość_słówek,Zdobyte_punkty,Ostatnie_logowanie,Data_powtórki,Słówka_do_nauki)")
        self.cur.execute("CREATE TABLE if not exists users (login, password, points, last_login)")
        self.con.commit()
        
    def show_tables(self):
        tables_list = []
        tables = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in tables:
            if table[0] != 'users':
                tables_list.append(table[0])
        return tables_list
    
    def table_seed(self, path, dict_name):
        with open(path, 'r', encoding='utf-8') as seed:
            data = json.loads(seed.read())
            
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {dict_name} (polish, english)")
            
        query = f"""
            INSERT INTO {dict_name} (polish, english) VALUES (?,?)
        """
        for row in data:
            self.cur.execute(query, (row, data[row]))
            
        self.con.commit()
        
    def load_game_dict(self, table):
        word_dict = {}
        query = f"""
            SELECT * FROM {table}
        """
        for word in self.cur.execute(query):
            word_dict[word[0]] = word[1]
        return word_dict
    
    def save_game(self, player_name, points, time):
        query = f"""
            UPDATE users SET points={int(points)}, last_login='{time}' WHERE login='{player_name}'
        """
        self.cur.execute(query)
        self.con.commit()

    def insert_user(self,user_info):
        try:
            self.cur.execute('''INSERT INTO users 
                            (login, password, points, last_login) VALUES (?,?,?,?)''', 
                            [user_info[0], user_info[1], 0, datetime.now().strftime('%Y/%m/%d %H:%M')])
            self.con.commit()
            return f"Gracz {user_info[0]} zarejestrowany poprawnie!"
        except Exception as e:
            return f"Wystąpił problem przy rejestracji:\n\t{e}"

    def check_and_return_user_data(self, user_credentials):
        query = f"""
            SELECT * FROM users WHERE login='{user_credentials[0]}'
        """
        try:
            data = list(self.cur.execute(query).fetchone())
            if data[1] == user_credentials[1]:
                user_dict = {
                    'login': data[0],
                    'password': data[1],
                    'points': data[2],
                    'last_login': data[3]
                }
                return user_dict
        except:
            print("Niepoprawny login lub hasło!")
            time.sleep(2)
            return False
        
    def __del__(self):
        self.con.close()
        
