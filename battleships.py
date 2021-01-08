import random
from extension import Ocean
from Ship import Ship
import copy


def is_sunk(ship):
    # pass
    return ship.is_sunk()

def ship_type(ship):
    # pass
    length=ship.length
    if length==4:
        return "battleship"
    elif length==3:
        return "cruiser"
    elif length==2:
        return "destroyer"
    elif length==1:
        return "submarine"

def is_open_sea(row, column, grid):
    return grid[row][column] != "+"

def ok_to_place_ship_at(row, column, horizontal, length, grid):
    
    open_sea = True
    if not horizontal and row+length<10:
        for r in range(row,row+length):
            if not is_open_sea(r, column, grid):
                open_sea = False
                break
    elif horizontal and column + length < 10:
        for col in range(column, column+length):
            if not is_open_sea(row, col, grid):
                open_sea = False
                break
    else:
        open_sea = False
    return open_sea

def place_ship_at(row, column, horizontal, length, fleet):
    # pass
    # print("Saving")
    fleet.append(Ship(row,column,horizontal,length))
    # print("Saved")
    return fleet


def randomly_place_all_ships(new_grid):
    n = 1
    board_len = 10
    fleet = []
    shipcount = 0
    for length in reversed(range(1,5)):
        current_ship_count=0
        for count in range(1,n+1):
            while current_ship_count!= count:
            
                row = random.randint(0, board_len - 1)
                column=random.randint(0, board_len - 1)
                horizontal=random.choice([True, False])

                # print(count , current_ship_count, length)
                # print(row, column)
                
                if ok_to_place_ship_at(row, column, horizontal, length, new_grid):
                    # print(" ok to place")
                    fleet= place_ship_at(row,column,horizontal,length,fleet)
                    
                    if horizontal:
                        for col in range(column -1 ,column + length+1):
                            for r in range(row - 1,row + 2):
                                if col<10 and col >=0 and r<10 and r>=0:
                                    new_grid[r][col] = "+"
                    else:
                        for r in range(row - 1,row + length + 1 ):
                            for col in range(column - 1,column + 2):
                                if col<10 and col >=0 and r<10 and r>=0: 
                                    new_grid[r][col] = "+"
                    
                    shipcount += 1
                    current_ship_count+=1
                    # print("added  total ship {}".format(shipcount))
        n+=1
    return fleet

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    
    # print("check hits ---> ")
    hit_flag = False
    for ship in fleet:
        if (ship.horizontal and row == ship.row and column in range(ship.column,ship.column + ship.length)) or ((~ ship.horizontal) and (column == ship.column) and row in range(ship.row,ship.row + ship.length)):
            hit_flag = True
            break
    # print(hit_flag)
    return hit_flag
    

def hit(row, column, fleet):
    
    i = 0
    
    for ship in fleet:
        if (ship.horizontal and row == ship.row and column in range(ship.column,ship.column + ship.length)) or ((~ ship.horizontal) and (column == ship.column) and row in range(ship.row,ship.row + ship.length)):
            ship.hit(row,column)
            ship_hit = ship
            fleet[i] = ship
        i += 1
        
    return fleet, ship_hit

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    i = len(fleet)
    for ship in fleet:
        if ship.is_sunk():
            i -= 1
    return i > 0


def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)

    print("Game is started ")
    ocean = Ocean()
    ocean.display_board()
    print()

    # print(ocean.get_public_view())
    current_fleet = randomly_place_all_ships(copy.deepcopy(ocean.grid))

    # print(len(current_fleet))
    for ship in current_fleet:
        print(ship)
        print()
    game_over = False
    shots = 0

    while not game_over:
        loc_str = []
        
        while True:
            loc_str = input(" Enter row and colum to shoot (separted by space and between 0 - 9) : ").split()

            if len(loc_str) == 2 :
                current_row = int(loc_str[0])
                current_column = int(loc_str[1])
                if current_row < 10 and current_row >= 0 and current_column < 10 and current_column >= 0:
                    break

        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            # print(ship_hit)
            
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
                ocean.update_board_sunk(ship_hit)
            else:
                ocean.update_board_shot(current_row, current_column, "*")
        else:
            print("You missed!")
            ocean.update_board_shot(current_row, current_column, "-")
            

        if not are_unsunk_ships_left(current_fleet):
            game_over = True

    print("Game over! You required", shots, "shots.")

if __name__ == '__main__': #keep this in
    main()
