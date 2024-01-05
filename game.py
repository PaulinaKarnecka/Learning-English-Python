from libs.db_connector import Base
import os
import random
import time

class Game():
    def __init__(self, player):
        self.player = player
        self.cleaner = "cls"
        self.info = "Wciśnij dowolny klawisz aby kontynuować..."
        self.DB = Base()
        self.tables = self.DB.show_tables()
        dict_list = []
        print(f"Dostępne słowniki:\n")
        for table in self.tables:
            print(f"-  {table}")
            dict_list.append(table)
            
        self.dict_choice = input("\n\nWybierz słownik:  ")
        if self.dict_choice in dict_list:
            self.play(self.dict_choice)
        else:
            print("Wybrany słownik nie istnieje!")
            input("\nWciśnij dowolny przycisk aby kontynuować...")
                
    
    def play(self, dict):
        dict_of_words = self.DB.load_game_dict(dict)
        print("Tłumaczenie:\n\n1.   polski > angielski\n2.   angielski > polski\n\n")
        language = input("Wybór: ")
        if language != '1' and language != '2':
            print("Błędny wybór!")
            input(self.info)
            os.system(self.cleaner)
        
        while True:
            os.system(self.cleaner)
            print("Aby wyjść wpisz 'EXIT' i wciśniej 'Enter'")
            
            if language == '1':
                while True:
                    print(self.player.known_words)
                    rnd_word = random.choice(list(dict_of_words))
                    if dict_of_words[rnd_word] not in self.player.known_words:
                        break
                answer = input(f"Jak poprawnie przetłumaczysz {dict_of_words[rnd_word]}:   ")
                if answer == rnd_word:
                    self.player.points += 1
                    self.player.known_words.append(dict_of_words[rnd_word])
                    print("TO POPRAWNA ODPOWIEDŹ! :)")
                    time.sleep(2)
                elif answer.upper() == 'EXIT':
                    break
                else:
                    print("Zła odpowiedź! :(")
                    time.sleep(2)
                    
            if language == '2':
                while True:
                    print(self.player.known_words)
                    rnd_word = random.choice(list(dict_of_words))
                    if rnd_word not in self.player.known_words:
                        break
                answer = input(f"Jak poprawnie przetłumaczysz {rnd_word}:   ")
                if answer == dict_of_words[rnd_word]:
                    self.player.points += 1
                    self.player.known_words.append(rnd_word)
                    print("TO POPRAWNA ODPOWIEDŹ! :)")
                    time.sleep(2)
                elif answer.upper() == 'EXIT':
                    break
                else:
                    print("Zła odpowiedź! :(")
                    time.sleep(2) 
        