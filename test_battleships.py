import pytest
from battleships import *
from Ship import Ship
from extension import Ocean

def test_is_sunk1():
    
    hits1 = {(2,3), (3,3), (4,3)}
    hits2 = {(5,1), (5,2), (5,3)}
    hits3 = {(8,8)}
    hits4 = {(1,1),(1,2)}


    ex_ship1 = Ship(2,3,False,3)
    ex_ship2 = Ship(5,1,True,4)
    ex_ship3 = Ship(7,8,False,2)
    ex_ship4 = Ship(1,1,False,2)

    for x,y in hits1:
        ex_ship1.hit(x , y)
    
    assert is_sunk(ex_ship1) == True

    for x,y in hits2:
        ex_ship2.hit(x , y)
    assert is_sunk(ex_ship2) == False
    
    for x,y in hits3:
        ex_ship3.hit(x , y)
    assert is_sunk(ex_ship3) == False

    for x,y in hits4:
        ex_ship4.hit(x , y)
    assert is_sunk(ex_ship4) == True

def test_ship_type1():

    ex_ship = Ship(2,3,False,3)
    assert ship_type(ex_ship) == "cruiser"

def test_is_open_sea1():
    
    ocean = Ocean()
    assert is_open_sea(2, 3, ocean.grid) == True
    
    

def test_ok_to_place_ship_at1():
    
    ocean = Ocean()
    assert ok_to_place_ship_at(2, 3, False, 3,ocean.grid) == True

def test_place_ship_at1():
    fleet = []
    fleet = place_ship_at(2, 3, False, 3, fleet)
    assert len(fleet) == 1

def test_check_if_hits1():
    fleet = []
    fleet = place_ship_at(3, 0, False, 4, fleet)
    fleet = place_ship_at(1, 4, False, 3, fleet)
    fleet = place_ship_at(8, 0, True, 3, fleet)
    fleet = place_ship_at(4, 7, True, 2, fleet)
    fleet = place_ship_at(9, 1, True, 2, fleet)
    fleet = place_ship_at(0, 5, True, 2, fleet)
    fleet = place_ship_at(9, 5, True, 1, fleet)
    fleet = place_ship_at(5, 5, True, 1, fleet)
    fleet = place_ship_at(1, 2, False, 1, fleet)
    fleet = place_ship_at(9, 8, True, 1, fleet)

    assert check_if_hits(2 ,3 ,fleet) == False
    assert check_if_hits(3 ,0 ,fleet) == True
    assert check_if_hits(5 ,6 ,fleet) == False 

def test_hit1():
    fleet = []
    fleet = place_ship_at(3, 0, False, 4, fleet)
    fleet = place_ship_at(1, 4, False, 3, fleet)
    fleet = place_ship_at(8, 0, True, 3, fleet)
    fleet = place_ship_at(4, 7, True, 2, fleet)
    fleet = place_ship_at(9, 1, True, 2, fleet)
    fleet = place_ship_at(0, 5, True, 2, fleet)
    fleet = place_ship_at(9, 5, True, 1, fleet)
    fleet = place_ship_at(5, 5, True, 1, fleet)
    fleet = place_ship_at(1, 2, False, 1, fleet)
    fleet = place_ship_at(9, 8, True, 1, fleet)

    fleet, ship = hit(3, 0, fleet)
    assert len(ship.hits) == 1

def test_are_unsunk_ships_left1():

    fleet = []
    fleet = place_ship_at(3, 0, False, 4, fleet)
    fleet = place_ship_at(1, 4, False, 3, fleet)

    fleet, ship = hit(3, 0, fleet)
    fleet, ship = hit(4, 0, fleet)
    fleet, ship = hit(5, 0, fleet)
    fleet, ship = hit(6, 0, fleet)

    assert are_unsunk_ships_left(fleet) == True

    fleet, ship = hit(1, 4, fleet)
    fleet, ship = hit(2, 4, fleet)
    fleet, ship = hit(3, 4, fleet)

    assert are_unsunk_ships_left(fleet) == False
