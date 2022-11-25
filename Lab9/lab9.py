import random
q = [["0" for j in range(12)] for i in range(4)]

q[3][0] = "s"
#q[1][1] = "s"
#q[2][1] = "1"
#q[1][0] = "1"
q[3][11] = "d"

for i in range(1,11):
    q[3][i] = '-100'

recompense = {}
recompense["x"] = -100


for i in range(4):
    print(q[i])

def check_if_out_of_bounds(i,j):
    if i<0 or i>3:
        return True
    elif j<0 or j>11:
        return True
    return False

def choose_next_state(i,j):
    moves = {1:{"i":0,"j":1},2:{"i":1,"j":0},3:{"i":0,"j":-1},4:{"i":-1,"j":0}}
    maximum = -1
    maximum_move = 0
    for move in moves:
        i_new = i + moves[move]["i"]
        j_new = j + moves[move]["j"]
        if check_if_out_of_bounds(i_new,j_new) == False:
            if int(q[i_new][j_new]) > maximum:
                maximum = int(q[i_new][j_new])
                maximum_move = move
    return maximum_move
    
print(choose_next_state(1,1))

