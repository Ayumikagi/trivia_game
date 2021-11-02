from pathlib import Path
from random import randint
from textwrap import dedent
import questions

class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    
    def welcome(self):
        print(f'Welcome {self.rank} {self.name}!')

try:
    data = Path('savedata.txt').read_text()
    user = data.split(', ')
    name, rank = user
except FileNotFoundError:
    name = input('Enter your name: ')
    rank = 'Rookie'
    Path('savedata.txt').write_text(f"{name}, {rank}")
player = Player(name, rank)
player.welcome()

print('Trivia Master 1.0.0 Loaded.')
while True:
    print('[1. New game] [2. Rename] [3. Quit]')
    choice = input("What's it gonna be?: ")
    if choice == '1':
        pool, right_answer, exclude = 5, 0, []
        print('Starting a new game...')
        while pool > 0:
            while True:
                question = randint(1, 5)
                if question in exclude:
                    pass
                else:
                    break
            A, B, C = questions.q(question)
            while True:
                choice = input('Enter your choice: ')
                if choice == 'A':
                    answer = A
                    break
                elif choice == 'B':
                    answer = B
                    break
                elif choice == 'C':
                    answer = C
                    break
                else:
                    print(f'"{choice}" is not a valid input.')
            if answer == True:
                print('Correct!')
                right_answer += 1
                pool -= 1
            elif answer == False:
                print('Wrong')
                pool -= 1
                if A == True:
                    print('The right answer was A.')
                elif B == True:
                    print('The right answer was B.')
                elif C == True:
                    print('The right answer was C.')
            exclude.append(question)
            A = B = C = None
        print(dedent(f'''
        Good job {player.name}!
        You have answered correctly to {right_answer} question(s).
        '''))
        if right_answer == 5 and rank == 'Rookie':
            print(f'Promoted from {rank} to Apprentice!')
            rank = 'Apprentice'
        elif right_answer == 5 and rank == 'Apprentice':
            print(f'Promoted from {rank} to Expert!')
            rank = 'Expert'
        elif right_answer == 5 and rank == 'Expert':
            print(f'Promoted from {rank} to Master!')
            rank = 'Master'
        elif right_answer == 5 and rank == 'Master':
            print(f'Promoted from {rank} to Legend!')
            rank = 'Legend'
        elif right_answer == 5 and rank == 'Legend':
            print(f'Promoted from {rank} to Gigachad!')
            rank = 'Gigachad'
        elif right_answer < 5:
            print('Rank remains unchanged.')
        input('Press any key to continue.')
        Path('savedata.txt').write_text(f"{name}, {rank}")
    elif choice == '2':
        name = input('Enter your new name: ')
        print(f'"{name}" set as your name.')
    elif choice == '3':
        Path('savedata.txt').write_text(f"{name}, {rank}")
        input('Bye! Press any key to continue.')
        exit()
    else:
        print(f'"{choice} is an invalid input."')
        
