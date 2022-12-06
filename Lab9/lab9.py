import random
from itertools import product
import numpy as np
import pprint
r = [[-1 for j in range(12)] for i in range(4)]


for i in range(1,11):
    r[3][i] = -100


r[3][11] = 100


def check_if_out_of_bounds(i,j):
    if i<0 or i>3:
        return True
    elif j<0 or j>11:
        return True
    return False

def choose_next_state(q_table,state,moves):
    q_max = -9999999
    max_move = -1
    for key,value in moves.items():
        i = state[0] + value["i"]
        j = state[1] + value["j"]
        if check_if_out_of_bounds(i,j) == False:
            if q_table[(i,j)][key] > q_max:
                q_max = q_table[(i,j)][key]
                max_move = key
    return max_move


q_table = {}

states = []
arr1 = [0,1,2,3]
arr2 = [0,1,2,3,4,5,6,7,8,9,10,11]
states = list(product(arr1,arr2))

for state in states:
    q_table[state] = [0,0,0,0]


def q_learning(state):
    moves = {0:{"i":0,"j":1},1:{"i":1,"j":0},2:{"i":0,"j":-1},3:{"i":-1,"j":0}}
    episodes = 10000
    epsilon = 1.0
    alpha = 0.1
    gamma = 1
    decrease = 0.005
    while episodes > 0:
    #for i in range(0,50):
        action = -1
        if random.random() <= epsilon:
            action = random.sample(moves.keys(), k=1)[0]
            while check_if_out_of_bounds(state[0] + moves[action]["i"],state[1] + moves[action]["j"]) == True:
                action = random.sample(moves.keys(), k=1)[0]
        else:
            action = choose_next_state(q_table,state,moves)
        
        
        if epsilon > 0.1:
            epsilon -= decrease
        
        new_i = state[0] + moves[action]["i"]
        new_j = state[1] + moves[action]["j"]
        new_state = (new_i,new_j)
        next_R = r[new_state[0]][new_state[1]]

        q_table[(state[0],state[1])][action] = q_table[(state[0],state[1])][action] + alpha*(next_R + gamma*max(q_table[(new_i,new_j)]) - q_table[(state[0],state[1])][action])

        # print("Current state:",state)
        # print("Next state:",new_state)
        state = new_state


        if next_R == -100 or next_R == 100:
            state = (3,0)
            episodes -= 1
        
        #print(episodes)
        

initial_state = (3,0)
q_learning(initial_state)

for key,value in q_table.items():
    print(key,value)

for i in range(4):
    print(r[i])

print("1 dreapta, 2 jos, 3 stanga, 4 sus")
