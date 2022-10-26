from asyncio.windows_events import NULL
from cmath import inf
from copy import deepcopy
from collections import defaultdict 
from collections import deque
from queue import Empty

class recipient:
    def __init__(self, max_cap, **kwargs) -> None:
        self.max_cap = max_cap
        self.curr_cap = kwargs.get('curr_cap', 0)
        pass

    def fill_jar(self):
        self_copy = deepcopy(self)
        self_copy.curr_cap = self_copy.max_cap
        return self_copy
    
    def move_capacity(self, target_recipient, **kwargs):
        self_copy = deepcopy(self)
        target_copy = deepcopy(target_recipient)
        target_remaining_cap = target_copy.max_cap - target_copy.curr_cap
        invert = kwargs.get('invert', False)

        if(self_copy.curr_cap < target_remaining_cap):
            target_copy.curr_cap = target_copy.curr_cap + self_copy.curr_cap
            self_copy.curr_cap = 0

        else:
            target_copy.curr_cap = target_copy.max_cap
            self_copy.curr_cap = self_copy.curr_cap - target_remaining_cap
        if not invert: return [self_copy, target_copy]
        return [target_copy, self_copy]

    def empty_jar(self):
        self_copy = deepcopy(self)
        self_copy.curr_cap = 0
        return self_copy
    
def check_state(current_state):
    if(target_cap == current_state[0].curr_cap or target_cap == current_state[1].curr_cap): return True
    return False

jar1 = recipient(int(input('m: ')))
jar2 = recipient(int(input('n: ')))
target_cap = int(input('target capacity: '))

current_state = [jar1, jar2]  
visited = defaultdict(lambda: False)

def Water_Jug_problem(state):  

    X = state[0]
    Y = state[1]

    if (check_state(state)): 
        print("Final(",X.curr_cap, ", ",Y.curr_cap,")", sep ="") 
        return True
      
    if visited[(X.curr_cap, Y.curr_cap)] == False: 
        print("(",X.curr_cap, ", ",Y.curr_cap,")", sep ="") 
      
        visited[(X.curr_cap, Y.curr_cap)] = True

        return (Water_Jug_problem([X.empty_jar(), Y]) or
                Water_Jug_problem([X, Y.empty_jar()]) or
                Water_Jug_problem([X.fill_jar(), Y]) or
                Water_Jug_problem([X, Y.fill_jar()]) or
                Water_Jug_problem(X.move_capacity(Y)) or
                Water_Jug_problem(Y.move_capacity(X, invert=True)))
    else: 
        return False
  
def BFS(jar1, jar2):
    m = {}
    isSolvable = False
    path = []
 
    q = deque()
    q.append((jar1, jar2))
 
    while len(q) > 0:
        u = q.popleft()
 
        if (u[0].curr_cap, u[1].curr_cap) in m:
            continue

        path.append([u[0], u[1]])
        m[(u[0].curr_cap, u[1].curr_cap)] = 1
 
        if check_state([u[0],u[1]]):
            isSolvable = True
            for item in path:
                print("(", item[0].curr_cap, ",", item[1].curr_cap, ")")
            break
 
        q.append(u[0].move_capacity(u[1]))
        q.append(u[1].move_capacity(u[0], invert = True))

        q.append([u[0].fill_jar(), u[1]])
        q.append([u[0], u[1].fill_jar()])

        q.append([u[0].empty_jar(), u[1]])
        q.append([u[0], u[1].empty_jar()])
 
    if not isSolvable:
        print("No solution")

def heuristic_function(jar1,jar2,level, target_cap = target_cap):
    return abs(target_cap-jar1.curr_cap-jar2.curr_cap+level)

def a_star():
    m = {}
    isSolvable = False
    path = []
    closed_path = deque()
 
    q = deque()
    level = 0
    path.append([jar1.curr_cap,jar2.curr_cap])
    q.append(([jar1,jar2], level))
    while len(q) > 0:
        q_element = q.popleft()
        u = q_element[0]
        level = q_element[1]
        closed_path.append((u, level))
        
        #print("current: ",u[0].curr_cap,u[1].curr_cap, 'current level: ', level)

        m[(u[0].curr_cap, u[1].curr_cap)] = 1
 
        if check_state([u[0],u[1]]):
            isSolvable = True
            while len(closed_path) > 0:
                item = closed_path.popleft()
                print("(", item[0][0].curr_cap, ",", item[0][1].curr_cap, ")", 'level: ', item[1])
            break
        
        path.remove([u[0].curr_cap,u[1].curr_cap])
        best_h = []
        fill1 = (u[0].fill_jar(), u[1])
        if (fill1[0].curr_cap, fill1[1].curr_cap) not in m:
            best_h.append((heuristic_function(fill1[0], fill1[1],level), [fill1[0], fill1[1]]))
        fill2 = (u[0], u[1].fill_jar())
        if (fill2[0].curr_cap, fill2[1].curr_cap) not in m:
            best_h.append((heuristic_function(fill2[0], fill2[1],level), [fill2[0], fill2[1]]))

        empty1 = (u[0].empty_jar(), u[1])
        if (empty1[0].curr_cap, empty1[1].curr_cap) not in m:
            best_h.append((heuristic_function(empty1[0], empty1[1],level), [empty1[0], empty1[1]]))
        empty2 = (u[0], u[1].empty_jar())
        if (empty2[0].curr_cap, empty2[1].curr_cap) not in m:
            best_h.append((heuristic_function(empty2[0], empty2[1],level), [empty2[0], empty2[1]]))

        u1 = u[0].move_capacity(u[1])
        if (u1[0].curr_cap, u1[1].curr_cap) not in m:
            best_h.append((heuristic_function(u1[0], u1[1],level), [u1[0], u1[1]]))
        u2 = u[1].move_capacity(u[0], invert = True)
        if (u2[0].curr_cap, u2[1].curr_cap) not in m:
            best_h.append((heuristic_function(u2[0], u2[1],level), [u2[0], u2[1]]))
        
        best_h.sort(key=lambda x:x[0])
        #print(best_h[0][0], best_h[0][1][0].curr_cap, best_h[0][1][1].curr_cap)

        for item in best_h:
            path.append([item[1][0].curr_cap, item[1][1].curr_cap])
            q.append((item[1], level+1))
            
    if not isSolvable:
        print("No solution")

#hill_climb(current_state, target_cap)

def equal(current_state,new_state):
    print_state(current_state)
    print_state(new_state)
    if(current_state[0].curr_cap == new_state[0].curr_cap and current_state[1].curr_cap == new_state[1].curr_cap):
        return True
    return False

def print_state(state):
    print(state[0].curr_cap,state[1].curr_cap)

def hill_climbing_2(initial_state,target_cap):
    current_state = initial_state
    for i in range(10):
        u = current_state
        mc_AB =  u[0].move_capacity(u[1])
        mc_BA = u[1].move_capacity(u[0],invert = True)
        e_A = [u[0].empty_jar(), u[1]]
        e_B = [u[0], u[1].empty_jar()]
        f_A = [u[0].fill_jar(), u[1]]
        f_B = [u[0], u[1].fill_jar()]

        print_state(mc_AB)
        print_state(mc_BA)
        print_state(e_A)
        print_state(e_B)
        print_state(f_A)
        print_state(f_B)

        print(heuristic_function(mc_AB[0],mc_AB[1],target_cap))
        print(heuristic_function(mc_BA[0],mc_BA[1],target_cap))
        print(heuristic_function(e_A[0],e_A[1],target_cap))
        print(heuristic_function(e_B[0],e_B[1],target_cap))
        print(heuristic_function(f_A[0],f_A[1],target_cap))
        print(heuristic_function(f_B[0],f_B[1],target_cap))

        print("hr current",heuristic_function(current_state[0],current_state[1],target_cap))


        best_state = []
        min = 999999

        if heuristic_function(mc_AB[0],mc_AB[1],target_cap) <=  min and not (current_state[0].curr_cap == mc_AB[0].curr_cap and current_state[1].curr_cap == mc_AB[1].curr_cap):
            min = heuristic_function(mc_AB[0],mc_AB[1],target_cap)
            best_state = mc_AB
        
        if heuristic_function(mc_BA[0],mc_BA[1],target_cap) <=  min and not (current_state[0].curr_cap == mc_BA[0].curr_cap and current_state[1].curr_cap == mc_BA[1].curr_cap):
            min = heuristic_function(mc_BA[0],mc_BA[1],target_cap)
            best_state = mc_BA
        
        if heuristic_function(f_A[0],f_A[1],target_cap) <=  min and not (current_state[0].curr_cap == f_A[0].curr_cap and current_state[1].curr_cap == f_A[1].curr_cap):
            min = heuristic_function(f_A[0],f_A[1],target_cap)
            best_state = f_A
        
        if heuristic_function(f_B[0],f_B[1],target_cap) <=  min and not (current_state[0].curr_cap == f_B[0].curr_cap and current_state[1].curr_cap == f_B[1].curr_cap):
            min = heuristic_function(f_B[0],f_B[1],target_cap)
            best_state = f_B
        
        if heuristic_function(e_A[0],e_A[1],target_cap) <=  min and not (current_state[0].curr_cap == e_A[0].curr_cap and current_state[1].curr_cap == e_A[1].curr_cap):
            min = heuristic_function(e_A[0],e_A[1],target_cap)
            best_state = e_A
        
        if heuristic_function(e_B[0],e_B[1],target_cap) <=  min and not (current_state[0].curr_cap == e_B[0].curr_cap and current_state[1].curr_cap == e_B[1].curr_cap):
            min = heuristic_function(e_B[0],e_B[1],target_cap)
            best_state = e_B
        
        if not best_state:
            return current_state
        
        print("best_state: ",best_state[0].curr_cap,best_state[1].curr_cap)

        current_state = best_state


#print("solution: ",hill_climbing_2(current_state,target_cap))

import math

if not (target_cap%math.gcd(jar1.max_cap,jar2.max_cap) == 0 and jar1.max_cap + jar2.max_cap > target_cap):
    print("Problema nu se poate rezolva")
    is_Solvable = False
else:
    print("Problema se poate rezolva...")
    is_Solvable = True

while(is_Solvable):
    string = input("Selecteaza strategia: <hill-climbing>,<a_star>,<bfs>,<bkt>",)

    if string == "hill-climbing":
        hill_climbing_2(current_state,target_cap)
        break
    elif string == "a_star":
        a_star()
        break
    elif string == "bfs":
        BFS(current_state[0],current_state[1])
        break
    elif string == "bkt":
        Water_Jug_problem(current_state)
        break
    else:
        print("Nu exista o astfel de strategie")



        

        

        



