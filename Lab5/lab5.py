import numpy as np

file = open("input.txt")
lines = [line.rstrip() for line in file]

moves = {}

for i in range(2):
    split_text = lines[i].split(" ")
    cols = []
    for j in range(1,len(split_text)):
        cols.append(split_text[j])
    moves[split_text[0]] = cols

matrix = []
for i in range(2,len(lines)):
    split_text = lines[i].split(" ")
    tuples = []
    for text in split_text:
        s = text.split("/")
        tuples.append((s[0],s[1]))
    matrix.append(tuples)

def print_matrix(matrix):
    for line in matrix:
        print(line)

print_matrix(matrix)
print("")

def get_column_vals(matrix,index):
    vals = []
    for i in range(len(matrix)):
        vals.append(matrix[i][index])
    return vals

def find_dominant_strategies_2(matrix,player,**kwargs):
    max_c = []
    max_l = []
    if player == 'PlayerA':
        max_col_j = []
        for i in range(len(matrix)):
            col = get_column_vals(matrix,i)
            max_col = -999999
            max_j = -1
            max_i = -1
            for j in range(len(col)): #j=linie
                if(int(col[j][0])>max_col):
                    max_col = int(col[j][0])
                    max_j = j
                    max_i = i
            max_col_j.append(max_j)
            max_c.append((max_j,max_i))
            for j in range(len(col)):
                if int(col[j][0]) == max_col and i!= max_i:
                    max_l.append((j,i))
        unique = np.unique(max_col_j)
        if len(unique) == 1:
            if(kwargs.get('display')==True):
                print("PlayerA are strategie dominanta pe",moves['PlayerA'][unique[0]])
        return max_c
    elif player == 'PlayerB':
        max_line_j = []
        max_line = -99999
        for i in range(len(matrix)):
            line = matrix[i]
            max_line = -99999
            max_j = -1
            max_i = -1
            for j in range(len(line)):
                if(int(line[j][1])>max_line):
                    max_line = int(line[j][1])
                    max_j = j
                    max_i = i
            max_line_j.append(max_j)
            max_l.append((max_i,max_j))
            for j in range(len(line)):
                if int(line[j][1]) == max_line and j!= max_j:
                    max_l.append((i,j))
        unique = np.unique(max_line_j)
        if len(unique) == 1:
            if(kwargs.get('display')==True):
                print("PlayerB are strategie dominanta pe",moves['PlayerB'][unique[0]])
        return max_l



def find_nash_equilibriums_2(matrix):
    setA = set(find_dominant_strategies_2(matrix,'PlayerA',display=False))
    setB = set(find_dominant_strategies_2(matrix,'PlayerB',display=False))
    intersection = setA.intersection(setB)
    for int in intersection:
        print("Exista echilibru Nash la valoarea: (",int[0],",",int[1],")")



find_nash_equilibriums_2(matrix)


players = ['PlayerA','PlayerB']

for player in players:
    print("For " + player + ":")
    find_dominant_strategies_2(matrix,player,display=True)






