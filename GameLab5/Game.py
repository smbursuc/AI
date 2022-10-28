import os

class player:
    def __init__(self, name, main_move_list) -> None:
        self.name = name
        self.main_move_list = main_move_list
        self.move_dict = {}
        pass
    
    def get_move_list(self):
        return self.main_move_list

    def append_side_moves(self, side_move_list):
        self.side_move_list = side_move_list

    def append_move_values(self, move_values_list):
        for move_type, move_value in zip(self.main_move_list + self.side_move_list, move_values_list):
            print(self.name, move_type, move_value)
            self.move_dict[move_type] = move_value

    def print(self):
        print(f'{self.name} has {self.main_move_list}, with move dictionary being: {self.move_dict}')

def get_player_from_input(file_desc):
    lines = file_desc.readline()
    player_input = lines.split()
    player_data = player(player_input[0], [player_input[1], player_input[2]])
    return player_data

def get_player_move_value_input(file_desc):
    lines = file_desc.readline()
    player_a_data_value = []
    player_b_data_value = []
    while(lines):
        for value in lines.split():
            value = value.split('/')
            player_a_data_value.append(value[0])
            player_b_data_value.append(value[1])
        lines = file_desc.readline()
    return (player_a_data_value, player_b_data_value)

def print_matrix(player_a, player_b):
    print(f'{player_a.name} / {player_b.name} \t {player_b.main_move_list}')
    for move_a, move_b in zip(player_a.main_move_list, player_b.main_move_list):
        print(f'{move_a} \t\t\t |{player_a.move_dict[move_a]}\\{player_b.move_dict[move_a]}|, |{player_a.move_dict[move_b]}\\{player_b.move_dict[move_b]}|')

def read_input():
    file_path = os.getcwd() # cd to the working folder for this command to work properly
    print(file_path + '\\input.txt')
    with open(file_path + '\\input.txt', 'r') as f:
        # Read player A
        player_a = get_player_from_input(f)
        # Read player B
        player_b = get_player_from_input(f)
        # Intersect players move lists
        player_a.append_side_moves(player_b.get_move_list())
        player_b.append_side_moves(player_a.get_move_list())

        # Read player A move list values and append them to the class
        players_data_tuple = get_player_move_value_input(f)
        player_a.append_move_values(players_data_tuple[0])
        player_b.append_move_values(players_data_tuple[1])

        player_a.print()
        player_b.print()
    return (player_a, player_b)


players = read_input()
print_matrix(players[0], players[1])