import random
import time


def display_intro():
    print('This land is full of dragons!')
    time.sleep(2)
    print('''There are two caves in front of you. In one of the caves, their is a friendly dragon who is willing
to share his treasure with you. However, the other cave hosts a greedy and hungry dragon who will burn and eat you!''', '\n')


def choose_cave():
    cave = ' '
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2)')

    return cave


def check_cave(chosen_cave):
    print('Quietly, you enter the cave...')
    time.sleep(2)
    print('.')
    time.sleep(1)
    print('\n' * 100)
    print('..')
    time.sleep(1)
    print('\n' * 100)
    print('...')
    time.sleep(2)
    print("It's dark in here...")
    time.sleep(2)
    print("THE DRAGON COMES OUT OF NOWHERE AND OPENS HIS MOUTH AND...")
    time.sleep(3)
    print('\n' * 100)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('Gives you his treasure!')
    else:
        print(':(')
        time.sleep(2)
        print('Goodbye friend...')
        time.sleep(2)
        print('\n' * 100)
        print('.')
        time.sleep(1)
        print('\n' * 100)
        print('..')
        time.sleep(1)
        print('\n' * 100)
        print('...')
        print('He exhales scorching flames, incinerating you instantly and feeding on your cooked flesh.')


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    display_intro()
    cave_choice = choose_cave()
    check_cave(cave_choice)
    if not replay():
        break

