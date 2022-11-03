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

def find_dominant_strategies(matrix,player):
    if player == 'PlayerA':
        max_line_vals = []
        for i in range(len(matrix)):
            line = matrix[i]
            maximum = -999999
            for tuple in line:
                if int(tuple[0])>maximum:
                    maximum=int(tuple[0])
                elif int(tuple[1])>maximum:
                    maximum=int(tuple[1])
            max_line_vals.append(maximum)
        
        for i in range(len(matrix)):
            line = matrix[i]
            good = 1
            for tuple in line:
                val1 = int(tuple[0])
                if val1< min(max_line_vals):
                    good = 0
            if good == 1:
                print("PlayerA are strategie dominanta pe",moves['PlayerA'][i])
    elif player=='PlayerB':
        max_col_vals = []
        for i in range(len(matrix)):
            col = get_column_vals(matrix,i)
            maximum = -999999
            for tuple in col:
                if int(tuple[0])>maximum:
                    maximum=int(tuple[0])
                elif int(tuple[1])>maximum:
                    maximum=int(tuple[1])
            max_col_vals.append(maximum)
        
        for i in range(len(matrix)):
            col = get_column_vals(matrix,i)
            good = 1
            for tuple in col:
                val2 = int(tuple[1])
                if val2 < min(max_col_vals):
                    good = 0
            if good == 1:
                print("PlayerB are strategie dominanta pe",moves['PlayerB'][i])

def find_nash_equilibriums(matrix,first_player):
    if first_player == 'PlayerA':
        for i in range(len(matrix)):
            max_j_index = -1
            max_line = -999999
            for j in range(len(matrix)):
                if int(matrix[i][j][0]) > max_line:
                    max_line = int(matrix[i][j][0])
                    max_j_index = j
        
            col = get_column_vals(matrix,max_j_index)
            max_col = -9999999
            max_i_index = -1
            for i in range(len(col)):
                if(int(col[i][1])>max_col):
                    max_col = int(col[i][1])
                    max_i_index = i
            
            val = matrix[max_i_index][max_j_index]
            val1 = val[0]
            val2 = val[1]


            if int(val1) == max_line and int(val2) == max_col:
                print("Exista echilibru Nash la valoarea: (",max_line,",",max_col,")")
                
        
            



find_dominant_strategies(matrix,'PlayerB')
find_nash_equilibriums(matrix,'PlayerA')




