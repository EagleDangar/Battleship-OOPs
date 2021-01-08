class Ocean:
    
    def __init__(self):
        self.grid = []
        nrows = 10
        ncols = 10
        #Creates the 2D Data Grid
        for row in range(nrows):
            row = []
            for _ in range(ncols):
                row.append('.')
            self.grid.append(row)
    
    def update_board_shot(self, row, column, char):
        self.grid[row][column] = char
        self.display_board()
    
    def update_board_sunk(self, ship):
        # print(" updating sunk grid ===> ")
        if ship.horizontal:
            start = ship.column
            for col in range(start, start+ship.length):
                self.grid[ship.row][col] = ship.type
        else:
            start = ship.row
            for row in range(start, start+ship.length):
                self.grid[row][ship.column] = ship.type
        self.display_board()

    def display_board(self):
        #Prints the labels for the grid
        rocol = len(self.grid)
        print("  "+" ".join(map(str,range(rocol))))
        print("  "+ " ".join(["_"]*rocol))
        for i,row in enumerate(self.grid):
            print(str(i)+"|" + " ".join(row))
        

