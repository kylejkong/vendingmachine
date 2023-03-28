from vendingmachine import Item, Vending_Machine, insert_coin, main,displayItem
import pytest
import sys

def test_displayItem():
    vm = Vending_Machine()
    assert str(vm.items[1].name) == "OJ"

    vm = Vending_Machine()
    assert str(vm.items[4].name) != "Water"

    vm = Vending_Machine()
    with pytest.raises(IndexError):
        str(vm.items[5]) 

    vm = Vending_Machine()
    assert str(vm.items[2].price) == "150"




"""
1. in insert_coin function, update from continue to raise ValueError under except ValueError
2. run pytest -s test_vendingmachine.py to test test_coin 
3. any input that isn't 100,50,25,10 or 5 will raise ValueError

"""
def test_insert_coin():

    with pytest.raises(ValueError):
        insert_coin(100) 



   


    

    


    