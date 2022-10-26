
class Chess_Table:
    matrix = {}
    size = 0
    queen_list = []
    def __init__(self, size = 4) -> None:
        self.queen_list = []
        self.size = size
        for i in range(size):
            for j in range(size):
                self.matrix[i,j] = {'has queen': 0, 'can place': True, 'blocked by': 0}
        pass

    def print_matrix(self):
        for i in range(self.size): 
            line = []
            for j in range(self.size):
                line.append((self.matrix[i,j]['has queen'])) # if you want to see who blocked the tile use !!!self.matrix[i,j]['blocked by']!!!
            print(line)
        print("Queen positions: ", self.queen_list)

    def block_tile_switch(self, coord_x, coord_y):
        self.matrix[coord_x,coord_y] = {'has queen': 0, 'can place': not self.matrix[coord_x,coord_y]['can place'], 'blocked by': -1}

    def place_queen_switch(self, coord_x, coord_y):
        if (self.matrix[coord_x,coord_y]['has queen'] == 0):
            # print(f'place queen on {coord_x},{coord_y}')
            self.queen_list.append([coord_x, coord_y])
            self.matrix[coord_x,coord_y] = {'has queen': 1, 'can place': False, 'blocked by': len(self.queen_list)}
            self.block_queen_paths(coord_x, coord_y, False)
        else:
            # print(f'remove queen from {coord_x},{coord_y}')
            self.queen_list.remove([coord_x, coord_y])
            self.matrix[coord_x,coord_y] = {'has queen': 0, 'can place': True, 'blocked by': 0}
            self.block_queen_paths(coord_x, coord_y, True)

    def block_queen_paths(self, coord_x, coord_y, var):
        for i in range(self.size): 
            if i == coord_x:
                for j in range(self.size):
                    if not var and self.matrix[i,j]['blocked by'] == 0:
                        self.matrix[i,j] = {'has queen': self.matrix[i,j]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                    elif self.matrix[i,j]['blocked by'] == len(self.queen_list):
                        self.matrix[i,j] = {'has queen': self.matrix[i,j]['has queen'], 'can place': var, 'blocked by': 0}

        for i in range(self.size): 
            for j in range(self.size):
                if j == coord_y:
                    if not var and self.matrix[i,j]['blocked by'] == 0:
                        self.matrix[i,j] = {'has queen': self.matrix[i,j]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                    elif self.matrix[i,j]['blocked by'] == len(self.queen_list):
                        self.matrix[i,j] = {'has queen': self.matrix[i,j]['has queen'], 'can place': var, 'blocked by': 0}


        d1_i, d1_j = coord_x, coord_y
        k=1
        while True:
            if(d1_i+k < self.size and d1_j+k < self.size):
                if not var and self.matrix[d1_i+k, d1_j+k]['blocked by'] == 0:
                    self.matrix[d1_i+k, d1_j+k] = {'has queen': self.matrix[d1_i+k, d1_j+k]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                elif self.matrix[d1_i+k, d1_j+k]['blocked by'] == len(self.queen_list):
                    self.matrix[d1_i+k, d1_j+k] = {'has queen': self.matrix[d1_i+k, d1_j+k]['has queen'], 'can place': var, 'blocked by': 0}
                k = k+1
                continue
            break
        k=1
        while True:
            if(d1_i-k >= 0 and d1_j+k < self.size):
                if not var and self.matrix[d1_i-k, d1_j+k]['blocked by'] == 0:
                    self.matrix[d1_i-k, d1_j+k] = {'has queen': self.matrix[d1_i-k, d1_j+k]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                elif self.matrix[d1_i-k, d1_j+k]['blocked by'] == len(self.queen_list):
                    self.matrix[d1_i-k, d1_j+k] = {'has queen': self.matrix[d1_i-k, d1_j+k]['has queen'], 'can place': var, 'blocked by': 0}
                k = k+1
                continue
            break
        k=1
        while True:
            if(d1_i-k >= 0 and d1_j-k >= 0):
                if not var and self.matrix[d1_i-k, d1_j-k]['blocked by'] == 0:
                    self.matrix[d1_i-k, d1_j-k] = {'has queen': self.matrix[d1_i-k, d1_j-k]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                elif self.matrix[d1_i-k, d1_j-k]['blocked by'] == len(self.queen_list):
                    self.matrix[d1_i-k, d1_j-k] = {'has queen': self.matrix[d1_i-k, d1_j-k]['has queen'], 'can place': var, 'blocked by': 0}
                k = k+1
                continue
            break
        k=1
        while True:
            if(d1_i+k < self.size and d1_j-k >= 0):
                if not var and self.matrix[d1_i+k, d1_j-k]['blocked by'] == 0:
                    self.matrix[d1_i+k, d1_j-k] = {'has queen': self.matrix[d1_i+k, d1_j-k]['has queen'], 'can place': var, 'blocked by': len(self.queen_list)}
                elif self.matrix[d1_i+k, d1_j-k]['blocked by'] == len(self.queen_list):
                    self.matrix[d1_i+k, d1_j-k] = {'has queen': self.matrix[d1_i+k, d1_j-k]['has queen'], 'can place': var, 'blocked by': 0}
                k = k+1
                continue
            break      

    def check_position(self, coord_x, coord_y):
            lineH = []
            for i in range(self.size): 
                if i == coord_x:
                    for j in range(self.size):
                        lineH.append(self.matrix[i,j]['has queen'])
            if(not sum(lineH) > 1): return False

            lineV = []
            for i in range(self.size): 
                for j in range(self.size):
                    if j == coord_y:
                        lineV.append(self.matrix[i,j]['has queen'])
            if(not sum(lineV) > 1): return False

            row, col = (coord_x, coord_y)
            nrows, ncols = (self.size, self.size)
            # First diagonal
            d1_i, d1_j = nrows - 1 - max(row - col, 0), max(col - row, 0)
            d1_len = min(d1_i + 1, ncols - d1_j)
            diag1 = [self.matrix[d1_i - k, d1_j + k]['has queen'] for k in range(d1_len)]
            # Second diagonal
            t = min(row, ncols - col - 1)
            d2_i, d2_j = nrows - 1 - row + t, col + t
            d2_len = min(d2_i, d2_j) + 1
            diag2 = [self.matrix[d2_i - k, d2_j - k]['has queen'] for k in range(d2_len)]
            if(not (sum(diag1) > 1 and sum(diag2) > 1)): return False

    def check_validity(self):
        for queen in self.queen_list:
            self.check_position(queen[0], queen[1])
        return True

    def SolveFCAlg(self, MRV=False):
        queens = len(self.queen_list)
        if(queens == self.size):
            self.print_matrix()
            return True
        if(MRV):
            rows = self.getRowsDomainMRV()
        else:
            rows = self.getRowsDomain(queens)
        for row in rows:
            self.place_queen_switch(row, queens)
            domainWipeout = False
            for pair in self.getUnassigned():
                if(self.forward_check(pair[1], MRV=MRV)):
                    domainWipeout = True
                    break
            if not domainWipeout:
                if self.SolveFCAlg(MRV=MRV):
                    return True
            self.place_queen_switch(row, queens)

    def getUnassigned(self):
        result =[]
        for i in range(self.size):
            for j in range(self.size):
                if(self.matrix[i,j]['has queen'] == 0 and self.check_position(i,j)):
                    result.append((i,j))
        return result

    def getRowsDomain(self, coord_y):
        rows = []
        for i in range(self.size):
            if(self.matrix[i,coord_y]['can place']):
                rows.append((i))
        return rows
    
    def getRowsDomainMRV(self):
        rows = {}
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if(self.matrix[j,i]['can place']):
                    row.append((j))
            if len(row) > 0:
                rows[i] = row
        sorted(rows.items(), key=lambda item: item[1])
        if(len(rows) > 0):
            for key, item in rows.items():
                return item
        else: return []

    def forward_check(self, coord_y, MRV=False):
        if MRV:actualDomain = self.getRowsDomainMRV()
        else: actualDomain = self.getRowsDomain(coord_y)
        temp_domain = list(actualDomain)
        for row in actualDomain:
            if(not self.check_position(row[0], coord_y)):
                temp_domain.remove(row)
        return len(temp_domain) == 0



# ------------------Start Class Example------------------
# board = Chess_Table()
# board.block_tile_switch(0, 0)
# board.block_tile_switch(1, 1)
# board.block_tile_switch(3, 2)
# board.place_queen_switch(0,2)
# board.place_queen_switch(1,0)
# board.place_queen_switch(2,3)
# board.place_queen_switch(3,1)
# print(board.check_validity())
# board.print_matrix()
# ------------------End Class Example--------------------

# Forawrd Checking Alg:
board = Chess_Table(int(input('FC Normal: ')))
board.block_tile_switch(0, 0)
board.block_tile_switch(1, 1)
board.block_tile_switch(3, 2)
board.SolveFCAlg()
#MRV Solution
board = Chess_Table(int(input('FC+MRV: ')))
board.block_tile_switch(0, 0)
board.block_tile_switch(1, 1)
board.block_tile_switch(3, 2)
board.SolveFCAlg(MRV=True)