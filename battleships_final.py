
import sys
import random
import os
import string
from termcolor import colored

#os.system('color 70')
os.get_terminal_size()
width = os.get_terminal_size().columns

def init_player_board(board_dimension):
    board = [[colored('O', 'blue')] * board_dimension for _ in range(board_dimension)]
    return board

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_player_board(board_dimension, board, rows_letters):
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')
    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(board[i][j] + ' ', end=' ')
        print('\n')

def main_menu():  
    user_choice_before_game_valid = False
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' © JP, FB 2020'.center(width))
    print(' v. 1.0'.center(width))
    print( '''  
                ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ ███████╗
                ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗██╔════╝
                ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝███████╗
                ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ ╚════██║
                ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     ███████║
                ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝\n\n\n''') 
    print('''

            ▄█░ ▄ 　 ▒█▀▀▀█ ░▀░ █▀▀▄ █▀▀▀ █░░ █▀▀ 　 █▀▀█ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ 
            ░█░ ░ 　 ░▀▀▀▄▄ ▀█▀ █░░█ █░▀█ █░░ █▀▀ 　 █░░█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
            ▄█▄ ▀ 　 ▒█▄▄▄█ ▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 █▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ 


            █▀▀█ ▄ 　 ▒█▀▀▀ █░█ ░▀░ ▀▀█▀▀ 
            █▄▀█ ░ 　 ▒█▀▀▀ ▄▀▄ ▀█▀ ░░█░░ 
            █▄▄█ ▀ 　 ▒█▄▄▄ ▀░▀ ▀▀▀ ░░▀░░ \n''')

    while user_choice_before_game_valid == False:  
        print('''
    ᴠ  TYPE A NUMBER
    ᴠ''')
        user_choice_before_game = str(input())
        if (user_choice_before_game == '1') or (user_choice_before_game == '2') or (user_choice_before_game == '0'):
            user_choice_before_game_valid = True
            return user_choice_before_game
        else:
            print('\n- - - TRY AGAIN - - -\n')
            continue

def implacement_phase_pl_vs_pl(board_dimension):
    
    ship_types = ['Patrol Ship (1 cell: < X >)', 'Destroyer (2 cells: < XX >):', 'Aircraft carrier (3 cells: < XXX >):']
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    list_of_forbidden_coordinates = []
    clear_console()
    a = implacement_phase_player_1(ship_types, list_of_forbidden_coordinates, rows_letters)
    pl_1_placed_ships = a[0]
    list_of_ships_coordinates_pl_1 = a[1]
    wait_for_press_in_placem_phase('in')
    clear_console()
    
    list_of_forbidden_coordinates = []
    a = implacement_phase_player_2(ship_types, list_of_forbidden_coordinates, rows_letters)
    pl_2_placed_ships = a[0]
    list_of_ships_coordinates_pl_2 = a[1]
    wait_for_press_in_placem_phase('after')
    clear_console()        
    return (pl_1_placed_ships, pl_2_placed_ships, list_of_ships_coordinates_pl_1, list_of_ships_coordinates_pl_2) 
    

def implacement_phase_player_1(ship_types, list_of_forbidden_coordinates, rows_letters):
    player_1_board = init_player_board(board_dimension)
    print_player_board(board_dimension, player_1_board, rows_letters)
    list_of_forbidden_coordinates = list()
    list_of_ships_coordinates = list()
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, player_1_board)
        clear_console()
        put_ship_on_board(player_1_board, valid_coordinates, ship_type_number)
        print_player_board(board_dimension, player_1_board, rows_letters)
        list_of_ships_coordinates.insert(0, valid_coordinates)    
    return (player_1_board, list_of_ships_coordinates)


def implacement_phase_player_2(ship_types, list_of_forbidden_coordinates, rows_letters):
    player_2_board = init_player_board(board_dimension)
    print_player_board(board_dimension, player_2_board, rows_letters)
    list_of_forbidden_coordinates = list()
    list_of_ships_coordinates = list()
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, player_2_board)
        clear_console()
        put_ship_on_board(player_2_board, valid_coordinates, ship_type_number)
        print_player_board(board_dimension, player_2_board, rows_letters)
        list_of_ships_coordinates.insert(0, valid_coordinates)
    return (player_2_board, list_of_ships_coordinates)

def get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, board):
    checking_result_of_user_input = ()
    if ship_type_number == 0 or ship_type_number == 1:
        while not checking_result_of_user_input == 'coord_valid':      
            print(f'Provide coordinate for {(ship_type_number + 1)} {ship_types[0]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
    if ship_type_number == 2 or ship_type_number == 3:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation(h: horizontal, v: vertical) and coordinates for {(ship_type_number - 1)} {ship_types[1]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
    if ship_type_number == 4:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation(h: horizontal, v: vertical) and coordinates for {ship_types[2]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)   

def check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters):
    invalid_input = 'INVALID INPUT'
    too_close = 'SHIPS TOO CLOSE'
    coord_valid = 'coord_valid'
    if len(coordinates_given_by_user) != 2 and len(coordinates_given_by_user) != 3:
        return invalid_input
    try:
        coordinates = make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters) 
    except:
        return invalid_input
    try:
        is_not_too_close = mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board, coordinates, ship_type_number, list_of_forbidden_coordinates)
    except:
        return invalid_input
    if is_not_too_close == 'too_close':
        return too_close
    return coord_valid
    
def make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters):
    coordinates_given_by_user = coordinates_given_by_user.upper()
    coordinates_given_by_user_list = []
    for i in coordinates_given_by_user:
        coordinates_given_by_user_list.append(i)
    if len(coordinates_given_by_user_list) == 2:
        for rows_iteration_counter_2 in range(len(rows_letters)):
            if coordinates_given_by_user_list[0] == rows_letters[rows_iteration_counter_2]:
                row = int(rows_iteration_counter_2)
                break
        if int(coordinates_given_by_user_list[1]) > board_dimension or int(coordinates_given_by_user_list[1]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[1]) - 1
        orient = ''
        return (orient, row, col)
    elif len(coordinates_given_by_user_list) == 3:
        for rows_iteration_counter_3 in range(len(rows_letters)):
            if coordinates_given_by_user_list[1] == rows_letters[rows_iteration_counter_3]:
                row = int(rows_iteration_counter_3)
                break
        if int(coordinates_given_by_user_list[2]) > board_dimension or int(coordinates_given_by_user_list[2]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[2]) - 1
        orient = coordinates_given_by_user_list[0]
        if orient != 'H' and orient != 'V':
            raise
        return (orient, row, col)

def mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board, coordinates, ship_type_number, list_of_forbidden_coordinates):
    row = coordinates[1]
    col = coordinates[2]
    if ship_type_number == 0 or ship_type_number == 1:
        if (row, col) in list_of_forbidden_coordinates:
            return 'too_close'
        board[row][col] = 'X'
        list_of_forbidden_coordinates.append((row, col))
        list_of_forbidden_coordinates.append((abs(row -1), col))
        list_of_forbidden_coordinates.append((row +1, col))
        list_of_forbidden_coordinates.append((row, abs(col -1)))
        list_of_forbidden_coordinates.append((row, col +1))
    if ship_type_number == 2 or ship_type_number == 3:
        if coordinates[0] != 'H' and coordinates [0] != 'V':
            raise
        if coordinates[0] == 'H':
            if (row, col) in list_of_forbidden_coordinates or (row, col+1) in list_of_forbidden_coordinates:
                return 'too_close'
            board[row][col] = 'X'
            board[row][col+1] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((abs(row-1), col+1))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+1, col+1))
        elif coordinates[0] == 'V':
            if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates:
                return 'too_close'
            board[row][col] = 'X'
            board[row+1][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((row+1, abs(col-1)))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
    if ship_type_number == 4:
        if coordinates[0] != 'H' and coordinates [0] != 'V':
            raise
        if coordinates[0] == 'H':
            if (row, col) in list_of_forbidden_coordinates or (row, col+1) in list_of_forbidden_coordinates or (row, col+2) in list_of_forbidden_coordinates:
                return 'too_close'
            board[row][col] = 'X'
            board[row][col+1] = 'X'
            board[row][col+2] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((abs(row-1), col+1))
            list_of_forbidden_coordinates.append((abs(row-1), col+2))
            list_of_forbidden_coordinates.append((row, col+3))
            list_of_forbidden_coordinates.append((row+1, col+2))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+1, col))
        elif coordinates[0] == 'V':
            if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates or (row+2, col) in list_of_forbidden_coordinates:
                return 'too_close'
            board[row][col] = 'X'
            board[row+1][col] = 'X'
            board[row+2][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col+1))
            list_of_forbidden_coordinates.append((row+3, col))
            list_of_forbidden_coordinates.append((row+2, abs(col-1)))
            list_of_forbidden_coordinates.append((row+1, abs(col-1)))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
      
def put_ship_on_board(board, valid_coordinates, ship_type_number):
    orient = valid_coordinates[0]
    row = valid_coordinates[1]
    col = valid_coordinates[2]
    if ship_type_number == 0 or ship_type_number == 1:
        board[row][col] = colored('X', 'yellow')
    if ship_type_number == 2 or ship_type_number == 3:
        if orient == 'V':
            board[row][col] = colored('X', 'yellow')
            board[row+1][col] = colored('X', 'yellow')
        elif orient == 'H':
            board[row][col] = colored('X', 'yellow')
            board[row][col+1] = colored('X', 'yellow')
    if ship_type_number == 4:
        if orient == 'V':
            board[row][col] = colored('X', 'yellow')
            board[row+1][col] = colored('X', 'yellow')
            board[row+2][col] = colored('X', 'yellow')
        elif orient == 'H':
            board[row][col] = colored('X', 'yellow')
            board[row][col+1] = colored('X', 'yellow')
            board[row][col+2] = colored('X', 'yellow')
        
def wait_for_press_in_placem_phase(in_or_after):
    if in_or_after == 'in':
        print('NEXT PLAYER PLACEMENT PHASE')
        os.system('pause')
    elif in_or_after == 'after':
        print('SHOOTING PHASE')
        os.system('pause')

def implacement_phase_cpu():
    pass

def print_both_boards(board_dimension, player_1_shooting_board, player_2_shooting_board):
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    print('\n')
    print('        ' + 'PLAYER 1' + '               ' + 'PLAYER 2' + '\n') 
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('          ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')

    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(player_1_shooting_board[i][j] + ' ', end=' ')
        print('      ', end='')
        print(rows_letters[i] + '  ', end=' ')
        
        for j in range(0,board_dimension):
            print(player_2_shooting_board[i][j] + ' ', end=' ')
        print('\n')

def get_shot_coordinates(board_dimension):
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    while True:
        print('Provide shot coordinates: ')
        coordinates_given_by_user = str(input())
        coord_valid = check_user_input_shot_coordinates(coordinates_given_by_user, board_dimension, rows_letters)
        if coord_valid == 'coord_valid':
            coordinates = make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
            return coordinates
        elif coord_valid == 'INVALID INPUT':
            print('INVALID INPUT')


def check_user_input_shot_coordinates(coordinates_given_by_user, board_dimension, rows_letters): 
    invalid_input = 'INVALID INPUT'
    valid_input = 'coord_valid'
    if len(coordinates_given_by_user) != 2:
        return invalid_input
    try:
        make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
    except:
        return invalid_input
    return valid_input


def what_is_shot_effect(coordinates, placed_ships, patrol_boat_1, patrol_boat_2, destroyer_1, destroyer_2, aircraft_carrier):
    #step 1
    if placed_ships[coordinates[1]][coordinates[2]] == colored('O', 'blue'):
        return 'M'
    #step 2
    elif [coordinates[1], coordinates[2]] == patrol_boat_1:
        patrol_boat_1 = 'S'
        return 'S'
    elif [coordinates[1], coordinates[2]] == patrol_boat_2:   
        patrol_boat_2 = 'S'
        return 'S'
    #step 3
    for i in range(2):
        if (coordinates[1], coordinates[2]) == destroyer_1[i]:
            destroyer_1[i] = 'H'
        if (coordinates[1], coordinates[2]) == destroyer_2[i]:
            destroyer_2[i] = 'H'
    for i in range(3):
        if (coordinates[1], coordinates[2]) == aircraft_carrier[i]:
            aircraft_carrier[i] = 'H'
    #step 4
    if destroyer_1[0] == 'H' and destroyer_1[1] == 'H':
        destroyer_1[0] = 'S'
        destroyer_1[1] = 'S'
        
        return 'S'
    if destroyer_2[0] == 'H' and destroyer_2[1] == 'H':
        destroyer_2[0] = 'S'
        destroyer_2[1] = 'S'
        
        return 'S'
#step 5
    if aircraft_carrier[0] == 'H' and aircraft_carrier[1] == 'H' and aircraft_carrier[2] == 'H':
        aircraft_carrier[0] = 'S'
        aircraft_carrier[1] = 'S'
        aircraft_carrier[2] = 'S'
        
        return 'S'
    else:
        return 'H'

        
def get_ship_placement_separate_list(list_of_ships_coordinates):
    patrol_boat_1_adress = list_of_ships_coordinates[4]
    patrol_boat_1 = [patrol_boat_1_adress[1], patrol_boat_1_adress[2]] 

    patrol_boat_2_adress = list_of_ships_coordinates[3]
    patrol_boat_2 = [patrol_boat_2_adress[1], patrol_boat_2_adress[2]]

    destroyer_1_adress = list_of_ships_coordinates[2]
    if destroyer_1_adress[0] == 'V':
        destroyer_1 = [(destroyer_1_adress[1], destroyer_1_adress[2]), (destroyer_1_adress[1]+1, destroyer_1_adress[2])]
    if destroyer_1_adress[0] == 'H':
        destroyer_1 = [(destroyer_1_adress[1], destroyer_1_adress[2]), (destroyer_1_adress[1], destroyer_1_adress[2]+1)]

    destroyer_2_adress = list_of_ships_coordinates[1]
    if destroyer_2_adress[0] == 'V':
        destroyer_2 = [(destroyer_2_adress[1], destroyer_2_adress[2]), (destroyer_2_adress[1]+1, destroyer_2_adress[2])]
    if destroyer_2_adress[0] == 'H':
        destroyer_2 = [(destroyer_2_adress[1], destroyer_2_adress[2]), (destroyer_2_adress[1], destroyer_2_adress[2]+1)]

    aircraft_carrier_adress = list_of_ships_coordinates[0]
    if aircraft_carrier_adress[0] == 'V':
        aircraft_carrier = [(aircraft_carrier_adress[1], aircraft_carrier_adress[2]), (aircraft_carrier_adress[1]+1, aircraft_carrier_adress[2]), (aircraft_carrier_adress[1]+1, aircraft_carrier_adress[2])]
    if aircraft_carrier_adress[0] == 'H':
        aircraft_carrier = [(aircraft_carrier_adress[1], aircraft_carrier_adress[2]), (aircraft_carrier_adress[1], aircraft_carrier_adress[2]+1), (aircraft_carrier_adress[1], aircraft_carrier_adress[2]+2)]
    
    return (patrol_boat_1, patrol_boat_2, destroyer_1, destroyer_2, aircraft_carrier)


def mark_shot_effect_on_board(board, shoot_effect, coordinates, patrol_boat_1, patrol_boat_2, destroyer_1, destroyer_2, aircraft_carrier, destroyer_1_copy, destroyer_2_copy, aircraft_carrier_copy):

    if shoot_effect == 'M':
        board[coordinates[1]][coordinates[2]] = colored('M', 'cyan')
    elif shoot_effect == 'H': 
        board[coordinates[1]][coordinates[2]] = 'H'
    elif shoot_effect == 'S':
        if [coordinates[1], coordinates[2]] == patrol_boat_1:
            board[coordinates[1]][coordinates[2]] = 'S'
        if [coordinates[1], coordinates[2]] == patrol_boat_2:   
            board[coordinates[1]][coordinates[2]] = 'S'

    #refractor, try, except forbidden
        if (coordinates[1], coordinates[2]) in destroyer_1_copy:
            if destroyer_1[0] == 'S' and destroyer_1[1] == 'S':
                board[coordinates[1]][coordinates[2]] = 'S'
                try:
                    if board[coordinates[1]+1][coordinates[2]] == 'H':
                        board[coordinates[1]+1][coordinates[2]] = 'S'
                except:
                    pass
                try:
                    if board[coordinates[1]][coordinates[2]+1] == 'H':
                        board[coordinates[1]][coordinates[2]+1] = 'S'
                except:
                    pass
                try:
                    if board[coordinates[1]][abs(coordinates[2]-1)] == 'H':
                        board[coordinates[1]][abs(coordinates[2]-1)] = 'S'
                except:
                    pass
                try:
                    if board[abs(coordinates[1]-1)][coordinates[2]] == 'H':
                        board[abs(coordinates[1]-1)][coordinates[2]] = 'S'
                except:
                    pass

        
        if (coordinates[1], coordinates[2]) in destroyer_2_copy:
            if destroyer_2[0] == 'S' and destroyer_2[1] == 'S':
                board[coordinates[1]][coordinates[2]] = 'S'
                try:
                    if board[coordinates[1]+1][coordinates[2]] == 'H':
                        board[coordinates[1]+1][coordinates[2]] = 'S'
                except:
                    pass
                try:
                    if board[coordinates[1]][coordinates[2]+1] == 'H':
                        board[coordinates[1]][coordinates[2]+1] = 'S'
                except:
                    pass
                try:
                    if board[coordinates[1]][abs(coordinates[2]-1)] == 'H':
                        board[coordinates[1]][abs(coordinates[2]-1)] = 'S'
                except:
                    pass
                try:
                    if board[abs(coordinates[1]-1)][coordinates[2]] == 'H':
                        board[abs(coordinates[1]-1)][coordinates[2]] = 'S'
                except:
                    pass

        
        if (coordinates[1], coordinates[2]) in aircraft_carrier_copy:
            if aircraft_carrier[0] == 'S' == aircraft_carrier[1] == aircraft_carrier[2]:
                board[coordinates[1]][coordinates[2]] = 'S'
                try:
                    if board[coordinates[1]+1][coordinates[2]] == 'H':
                        board[coordinates[1]+1][coordinates[2]] = 'S'
                        try:
                            if board[coordinates[1]+2][coordinates[2]] == 'H':
                                board[coordinates[1]+2][coordinates[2]] = 'S' 
                        except:
                            pass       
                except:
                    pass 
                try:
                    if board[coordinates[1]][coordinates[2]+1] == 'H':
                        board[coordinates[1]][coordinates[2]+1] = 'S'
                        try:
                            if board[coordinates[1]][coordinates[2]+2] == 'H':
                                board[coordinates[1]][coordinates[2]+2] = 'S'
                        except:
                            pass
                except:
                    pass
                try:
                    if board[coordinates[1]][abs(coordinates[2]-1)] == 'H':
                        board[coordinates[1]][abs(coordinates[2]-1)] = 'S'
                        try:
                            if board[coordinates[1]][abs(coordinates[2]-2)] == 'H':
                                board[coordinates[1]][abs(coordinates[2]-2)] = 'S'
                        except:
                            pass
                except:
                    pass
                try:
                    if board[abs(coordinates[1]-1)][coordinates[2]] == 'H':
                        board[abs(coordinates[1]-1)][coordinates[2]] = 'S'
                        try:
                            if board[abs(coordinates[1]-2)][coordinates[2]] == 'H':
                                board[abs(coordinates[1]-2)][coordinates[2]] = 'S'
                        except:
                            pass
                except:
                    pass
                    
def print_shoot_effect(shoot_effect):
    if shoot_effect == 'M':
        print('YOU MISSED!')
    elif shoot_effect == 'H':
        print('YOU HIT OPPONENT SHIP')
    elif shoot_effect == 'S':
        print('YOU DESTROYED THE SHIP!')

def its_a_draw():
    print('--- WE HAVE A TIE ---')

def has_won(board):
    s_counter = 0
    for i in range(0,board_dimension):
        for j in range(0,board_dimension):
            if board[i][j] == 'S':
                s_counter += 1
    if s_counter == 9:
        return True
    else:
        return False

def print_result(player_has_won, player):
    if player_has_won == True:
        print(f'--> {player} <--- IS THE WINNER !\n')  
        return True
    else:
        return False

def after_game():
    user_choice_after_game_valid = False
    while user_choice_after_game_valid == False:
        user_choice_after_game = str(input('\n1: Main menu\n0: Exit game\n'))
        if (user_choice_after_game == '1') or (user_choice_after_game == '0') or (user_choice_after_game == '2'):
            user_choice_after_game_valid = True
            return user_choice_after_game
        else:
            print('- - - WRONG INPUT - - -')

# MAIN GAME LOOP
# implacement_phase(
# shooting phase
# make_a_list_placed_ships
# get_shot_coordinates
# check_user_input_shot_coordinates
# what_shoot_effect (s, m, h, repeated move ?)
# mark_shoot_effect_on_board
# has_won bedzie potrzebne czy wszystkie statki ustrzelone, czyli czy mamy 5 'S'
# print_result  

'''turns_left = 10
board_dimension = 5'''

while True:
    user_choice_before_game = main_menu()
    if user_choice_before_game == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
        sys.exit()
    elif user_choice_before_game == '1':
        pass
    elif user_choice_before_game == '2':
        pass

    clear_console()
    turns_left = int(input('\n\nNUMBER OF TURNS IS:'))
    board_dimension = int(input('\n\nBOARD DIMENSION IS:'))
    clear_console()

    b = implacement_phase_pl_vs_pl(board_dimension)
    pl_1_placed_ships = b[0]
    pl_2_placed_ships = b[1]
    list_of_ships_coordinates_pl_1 = b[2]
    list_of_ships_coordinates_pl_2 = b[3]

    ship_separate_list_pl_1 = get_ship_placement_separate_list(list_of_ships_coordinates_pl_2)
    ship_separate_list_pl_2 = get_ship_placement_separate_list(list_of_ships_coordinates_pl_1)

    player_1_shooting_board = init_player_board(board_dimension)
    player_2_shooting_board = init_player_board(board_dimension)

    patrol_boat_1_pl_1 = ship_separate_list_pl_2[0] 
    patrol_boat_2_pl_1 = ship_separate_list_pl_2[1]
    destroyer_1_pl_1 = ship_separate_list_pl_2[2]
    destroyer_2_pl_1 = ship_separate_list_pl_2[3]
    aircraft_carrier_pl_1 = ship_separate_list_pl_2[4]



    patrol_boat_1_pl_2 = ship_separate_list_pl_1[0]
    patrol_boat_2_pl_2 = ship_separate_list_pl_1[1]
    destroyer_1_pl_2 = ship_separate_list_pl_1[2]
    destroyer_2_pl_2 = ship_separate_list_pl_1[3]
    aircraft_carrier_pl_2 = ship_separate_list_pl_1[4]


    destroyer_1_pl_1_copy = (destroyer_1_pl_1[0], destroyer_1_pl_1[1])
    destroyer_2_pl_1_copy = (destroyer_2_pl_1[0], destroyer_2_pl_1[1])
    aircraft_carrier_pl_1_copy = (aircraft_carrier_pl_1[0], aircraft_carrier_pl_1[1], aircraft_carrier_pl_1[2])

    destroyer_1_pl_2_copy = (destroyer_1_pl_2[0], destroyer_1_pl_2[1])
    destroyer_2_pl_2_copy = (destroyer_2_pl_2[0], destroyer_2_pl_2[1])
    aircraft_carrier_pl_2_copy = (aircraft_carrier_pl_2[0], aircraft_carrier_pl_2[1], aircraft_carrier_pl_2[2])

    destroyer_1_pl_2_copy, destroyer_2_pl_2_copy, aircraft_carrier_pl_2_copy


    print_both_boards(board_dimension, player_1_shooting_board, player_2_shooting_board)

    game_is_over = False

    while game_is_over == False:
        player_switch = 0
        
        if player_switch % 2 == 0:
            player = 'PLAYER 1'
        else:
            player = 'PLAYER 2'
        print(f'     {turns_left} TURNS LEFT')
        print(f'---> {player} TURN')
        coordinates = get_shot_coordinates(board_dimension)
        shoot_effect = what_is_shot_effect(coordinates, pl_2_placed_ships, patrol_boat_1_pl_2, patrol_boat_2_pl_2, destroyer_1_pl_2, destroyer_2_pl_2, aircraft_carrier_pl_2)
        mark_shot_effect_on_board(player_2_shooting_board, shoot_effect, coordinates, patrol_boat_1_pl_2, patrol_boat_2_pl_2, destroyer_1_pl_2, destroyer_2_pl_2, aircraft_carrier_pl_2, destroyer_1_pl_2_copy, destroyer_2_pl_2_copy, aircraft_carrier_pl_2_copy)
        clear_console()
        print_both_boards(board_dimension, player_1_shooting_board, player_2_shooting_board)
        print_shoot_effect(shoot_effect)
        player_switch += 1
        player_1_has_won = has_won(player_2_shooting_board)
        game_is_over = print_result(player_1_has_won, player)
        if game_is_over == True:
            break


        if player_switch % 2 == 0:
            player = 'PLAYER 1'
        else:
            player = 'PLAYER 2'
        print(f'     {turns_left} TURNS LEFT')
        print(f'---> {player} TURN')
        coordinates = get_shot_coordinates(board_dimension)
        shoot_effect = what_is_shot_effect(coordinates, pl_1_placed_ships, patrol_boat_1_pl_1, patrol_boat_2_pl_1, destroyer_1_pl_1, destroyer_2_pl_1, aircraft_carrier_pl_1)
        mark_shot_effect_on_board(player_1_shooting_board, shoot_effect, coordinates, patrol_boat_1_pl_1, patrol_boat_2_pl_1, destroyer_1_pl_1, destroyer_2_pl_1, aircraft_carrier_pl_1, destroyer_1_pl_1_copy, destroyer_2_pl_1_copy, aircraft_carrier_pl_1_copy)
        clear_console()
        print_both_boards(board_dimension, player_1_shooting_board, player_2_shooting_board)
        print_shoot_effect(shoot_effect)
        turns_left -= 1
        player_2_has_won = has_won(player_1_shooting_board)
        game_is_over = print_result(player_2_has_won, player)

        if game_is_over == True:
            break
        
        else:
            if turns_left == 0:
                its_a_draw()
                game_is_over = True

    after_game_choice = False
    while after_game_choice == False:
        after_game_choice = after_game()   
        if after_game_choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
            sys.exit()
        elif after_game_choice == '1':
            after_game_choice_valid = True
        else:
            after_game_choice_valid = False



# try
# files