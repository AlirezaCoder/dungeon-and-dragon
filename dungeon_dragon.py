"""
this module is coded by Alireza branch oo
"""
import time
from random import *
import os


dimension = ()
escape_door_position = ()
dragon_position = ()
user_position = ()
game_matrix = ()
directions = []
user_dimension = []


def make_matrix():
    global escape_door_position, escape_door_position, dragon_position, user_position, game_matrix
    escape_door_position = get_random_position(dimension[0]-1, dimension[1]-1)
    dragon_position = get_random_position(dimension[0]-1, dimension[1]-1)
    user_position = get_random_position(dimension[0]-1, dimension[1]-1)
    game_matrix = []
    for i in range(dimension[0]):
        row = ()
        for j in range(dimension[1]):

            if [i, j] == escape_door_position:
                row = row + ("ESCAPE",)
            elif [i, j] == dragon_position:
                row = row + ("DRAGON",)
            elif [i, j] == user_position:
                row = row + ("USER",)
            else:
                row = row + ("EMPTY",)
        game_matrix.append(row)
    return game_matrix


def get_random_position(_max_x, _max_y):
    x = randint(0, _max_x)
    y = randint(0, _max_y)
    point = [x, y]
    return point


def draw_game_screen():
    print(dimension[0]*' _')
    for i in range(dimension[0]):
        row = ""
        for j in range(dimension[1]):
            if [i, j] == user_position:
                row += '|X'
            else:
                row += '|_'
        row += "|"
        print(row)


def check_input(_input):
    if _input:
        if str(_input).isnumeric():
            if 3 <= int(_input) <= 10:
                return True

    return False


def check_direction_input(_user_direction):
    global directions
    if _user_direction:
        if str(_user_direction).upper() in directions:
            return True
    return False


def update_user_position(_user_input):
    _user_input = str(_user_input).upper()
    if _user_input == "LEFT":
        user_position[1] = user_position[1]-1
    elif _user_input == "RIGHT":
        user_position[1] = user_position[1]+1
    elif _user_input == "DOWN":
        user_position[0] = user_position[0]+1
    elif _user_input == "UP":
        user_position[0] = user_position[0]-1


def print_navigation_directions():
    global directions
    directions = []
    direction_message = "you can move to "
    if user_position[0] > 0:
        directions.append("UP")
    if user_position[0] < dimension[0]-1:
        directions.append("DOWN")
    if user_position[1] > 0:
        directions.append("LEFT")
    if user_position[1] < dimension[1]-1:
        directions.append("RIGHT")
    direction_message += str(directions) + "by type these words."
    print(direction_message)


def check_dragon():
    if dragon_position == user_position:
        return True
    else:
        return False


def check_escape_door():
    if escape_door_position == user_position:
        return True
    else:
        return False


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def initiate_game():
    global user_dimension,dimension
    print("Welcome To Dungeon & Dragon Game")
    print("please enter your game dimension between 3 and 10")
    while True:
        cls()
        user_dimension = input()
        print("you entered " + user_dimension)
        if not check_input(user_dimension):
            print("invalid input try again")
            continue
        else:
            break
    dimension = [int(user_dimension), int(user_dimension)]
    make_matrix()
    print("user position is " + str(user_position))


def check_renew_game():
        print("Do You Want To Start A New Round Of Game?")
        user_input = input()
        if user_input:
            if user_input.upper() == "Y" or user_input.upper() == "YES":
                return True
        return False


initiate_game()
while True:
    cls()
    draw_game_screen()
    print("user position is " + str(user_position))
    print_navigation_directions()
    print("Enter Exit to Close The Game")
    print("please enter your direction to move.")
    user_direction = input()
    if str(user_direction).upper() == "EXIT":
        print("user finished the game. good by.")
        exit()
    elif not check_direction_input(user_direction):
        print("please select correct input, you cannot walk on the walls!")
        continue
    else:
        update_user_position(user_direction)
        if check_dragon():
            print("WOWWWW")
            time.sleep(3)
            print("Dragon is very powerful!!!")
            time.sleep(2)
            print("you lose. GOOD BY.")
            if check_renew_game():
                initiate_game()
            else:
                print("good by.")
                exit()
        elif check_escape_door():
            print("ha ha ha")
            time.sleep(3)
            print("You Escaped Successfully! congratulations.")
            time.sleep(2)
            print("you WON. GOOD LUCK.")
            if check_renew_game():
                initiate_game()
            else:
                print("good by.")



