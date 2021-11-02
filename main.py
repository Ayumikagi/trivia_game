from pathlib import Path
from random import randint
from textwrap import dedent
import questions

class Player:
    def __init__(self, name, rank, exp, nexp):
        self.name = name
        self.rank = rank
        self.exp = exp
        self.nexp = nexp
    
    def welcome(self):
        print(f'Welcome {self.rank} {self.name}!')
        
try:
    data = Path('savedata.txt').read_text()
    user = data.split(', ')
    name, rank, exp, nexp = user
    exp = int(exp)
except FileNotFoundError:
    name = input('Enter your name: ')
    rank = 'Rookie'
    exp = 0
    nexp = '5'
    Path('savedata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
player = Player(name, rank, exp, nexp)
player.welcome()

print('Trivia Master 1.0.0 Loaded.')
while True:
    print('[1. New game] [2. Profile] [3. Quit]')
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
                choice = input('Enter your choice: ').upper()
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
        exp += right_answer
        if 10 > exp > 4 and rank == 'Rookie':
            print(f'Promoted from {rank} to Apprentice!')
            rank = 'Apprentice'
            nexp = '10' 
        elif 20 > exp > 9 and rank == 'Apprentice':
            print(f'Promoted from {rank} to Expert!')
            rank = 'Expert'
            nexp = '20'
        elif 35 > exp > 19 and rank == 'Expert':
            print(f'Promoted from {rank} to Master!')
            rank = 'Master'
            nexp = '35'
        elif 50 > exp > 34 and rank == 'Master':
            print(f'Promoted from {rank} to Legend!')
            rank = 'Legend'
            nexp = '50'
        elif exp > 49 and rank == 'Legend':
            print(f'Promoted from {rank} to Gigachad!')
            rank = 'Gigachad'
            nexp = 'MAX'
        elif right_answer < 5:
            print('Rank remains unchanged.')
        print(f'Next rank progress: {exp}/{nexp}')
        input('Press any key to continue.')
        Path('savedata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
    elif choice == '2':
        print(f'Name: {name} | Rank: {rank} | XP: {exp}/{nexp}')
        while True:
            choice = input('Would you like to change your name? [Y/N]: ').upper()
            if choice == 'Y':
                name = input('Enter your new name: ')
                player.name = name
                print(f'"{name}" set as your name.')
                Path('savedata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
                break
            elif choice == 'N':
                break
            else:
                print(f'"{choice}" is not a valid input.')
    elif choice == '3':
        Path('savedata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
        input('Bye! Press any key to continue.')
        exit()
    else:
        print(f'"{choice} is an invalid input."')
        
