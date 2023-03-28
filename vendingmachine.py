import sys
import csv
from tabulate import tabulate
import pandas as pd
import pyttsx3

#########Vending Machine################
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return (f"Name: {self.name} , ${self.price} , Q:{self.stock}")

class Vending_Machine:
    def __init__(self):
        self.items = [
        Item("Water", 100, 5),
        Item("OJ", 120, 0),
        Item("Oreos", 150, 1),
        Item("Coffee", 140, 2),
        Item("Coke", 120, 3)
        ]
        
        self.inserted = 0.00


    def display_items(self):
        for code, item in enumerate(self.items, start = 1):
            print(f"[{code}] - {item.name} - (${item.price:.2f}) - {item.stock}")
    
        
    def __str__(self):
        return self.items



 
# vm = Vending_Machine()
# print(vm.items[1-1])

def main():
    
    if len(sys.argv) == 2 and sys.argv[1] == "admin":
        print(admin_check())
    
    elif len(sys.argv) == 2 and sys.argv[1] == "adminadd":
        adminadd()

    elif len(sys.argv) == 1:
        name, price = displayItem(displayItem)
        # print(price)
        change_owed = insert_coin(price)
        save(name,price)
        saythis = (f"Please take your change {change(change_owed)} cents and your {name}")
        print("Please take your change" , change(change_owed),"cents" , "and your" , name)
        text2speech(saythis)
        

"""
request user to select an item
if out of stock or wrong selection, user will be promopted to select again.
"""

def displayItem(n):
    vm = Vending_Machine()

    vm.display_items()

    while True:
        try:
            selection = int(input("Enter item code: "))
            n = vm.items[selection-1]
            if n.stock <= 0:
                print (f"{n} - Out Of Stock")
                raise ValueError
        except ValueError:
            continue
        if selection in range(1, len(vm.items)+1):
            n.stock = n.stock - 1
            print(f"You have selected {n.name}")    
            break
            
    # print(vm.items[2])
    return n.name, n.price
"""
request user to insert coin
and if coin is not valid, it will prompt user to insert coin again
"""
def insert_coin(due):
    vm = Vending_Machine()
    
    while due > 0:
    
        while True:
            try:                
                print("Amount Due: ", due)
                vm.inserted = int(input("Insert Coin: "))
                if vm.inserted not in [100,50,25,10,5]:
                    print("Invalid Coin")
                    raise ValueError 
              
            except ValueError:
                continue 
                #repalce *continue* with *raise ValueError* for pytest
                
            else:
                print(vm.inserted)
                due = due - vm.inserted

                break

    return due

def change(changeOwed):
    return abs(changeOwed)

def save(n,p):
    
    with open("biz.csv", "a", newline='') as file:

            writer = csv.DictWriter(file, fieldnames=["NAME", "PRICE"])

            ###Open biz.csv and check and see if header exists
            with open("biz.csv") as f:
                first = f.read(1)
                if not first:
                    writer.writeheader()
            writer.writerow({"NAME": n, "PRICE": p})



"""
check biz.csv to see how many each item(in column 1) has sold
check biz.csv to see how much has been genearted(in column 2)
"""
def admin_check():
    df = pd.read_csv("biz.csv")
    column1 = df.iloc[:,0]
    counts = column1.value_counts(sort=True)
    print(counts)

    column2 = df.iloc[:,1]
    return (f"Revenue: {column2.sum()}")

def text2speech(n):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(n)
    engine.runAndWait()
    engine.stop()


"""
refilling vending machine
"""
def adminadd():
    vm = Vending_Machine()

    vm.display_items()

    while True:
        try:
            selection = int(input("Enter item code: "))
            n = vm.items[selection-1]
            
        except ValueError:
            continue
        if selection in range(1, len(vm.items)+1):
            
            try:
                amount = int(input("Amount you want to add: "))
                n.stock = n.stock + amount
                # print(n)
            except ValueError:
                continue
            else:
                break

if __name__ == "__main__":
    main()




