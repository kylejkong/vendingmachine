    #### Video Demo:  https://youtu.be/qdy2a64PRv4
    #### Description: Vending Machine
    
    Vending machine app has 5 predetermined items with 3 variables: name, price and stock.

    The vending machine can be accessed by both admin(s) and users. An admin can check how many items have been sold and how much earned or refilling the machine via sys.argv which runs admin_check() or  adminadd() depending on the input. 

    Customer is shown a list of 5 items to choose from. Upon selecting an item, if the selected item is not out of stock ,the customer is shown how much to pay for the item and prompted to pay. If customer inserts an invalid coin, a message ("Invalid Coin") is shown and the customer is asked again to insert a coin. Once the insert amount is greater than the item amount , the item is dispensed and remaining change if any will be returne to the customer. The transactionw will be recorded in biz.csv 
