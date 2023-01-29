# ========The beginning of the class==========
global shoe_obj  # pycharm defined this variable

inventory = open('inventory.txt', 'r')


class Shoe:

    def __init__(self, country, code, product, cost, quantity):  # variables initialised
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        shoe_cost = self.cost * self.quantity
        return shoe_cost

    def get_quantity(self):
        return self.shoe_quantity

    def __str__(self):
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():  # opening file to read data
    with open('inventory.txt', 'r') as inventory:
        inventory.readline()
        for line in inventory:
            line = line.strip("\n").split(",")
            country = line[0]
            code = line[1]
            product = line[2]
            cost = line[3]
            quantity = line[4]
            sneakers = Shoe(country, code, product, cost, int(quantity))
            shoe_list.append(sneakers)  # data in defined function


read_shoes_data()

'''
    This function will open the file inventory.txt
     and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
     data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():  # getting shoe data from user
    global shoe_obje
    shoe_country = input("Enter the country where shoe is available: ")
    shoe_code = input("Enter the shoe code(e.g SKU96800): ")
    shoe_brand = input("Enter shoe brand: ")
    shoe_cost = input("Enter shoe cost: ")
    shoe_quantity = input("Enter the quantity: ")

    shoe_obje = Shoe(shoe_country, shoe_code, shoe_brand, shoe_cost, shoe_quantity)
    shoe_list.append(shoe_obje)  # data captured with function

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''


def view_all():  # viewing all the shoes available
    for i in shoe_list:
        print(i)

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def re_stock():  # searching for the shoe with the lowest quantity
    running_low = int(shoe_list[0].quantity)
    shoe_pos = 0

    for count, shoe_object in enumerate(shoe_list):
        if int(shoe_object.quantity) <= running_low:
            running_low = int(shoe_object.quantity)
            shoe_pos = count

    print(shoe_list[shoe_pos])

    current_quantity = input("Enter current quantity: ")
    shoe_list[shoe_pos].quantity = current_quantity
    # running_low.setQuantity(current_quantity)

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe():  # searching for shoe that user is looking for
    find_shoes = input("Enter code for shoe you're looking for: ")
    for shoe in shoe_list:
        if shoe.code == find_shoes:
            print(shoe)
            break
        else:
            continue

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


def value_per_item():  # getting value of each item
    # read_shoes_data()
    for shoe in shoe_list[1:]:
        shoe_list.append(shoe)
        shoe_cost = float(shoe.cost)
        shoe_quantity = float(shoe.quantity)
        value = int(float(shoe_cost) * int(float(shoe_quantity)))
        print(f"The stock value of {shoe} is : {value}")

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():  # function get the shoe with the highest quantity

    highest_val = int(shoe_list[0].quantity)
    shoe_pos = 0

    for count, shoe_object in enumerate(shoe_list):
        if int(shoe_object.quantity) >= highest_val:
            highest_val = int(shoe_object.quantity)
            shoe_pos = count

    print(f"This shoe for sale is: {shoe_list[shoe_pos]}")  # prints shoe that's for sale

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


def updated_shoe():
    with open('inventory.txt', 'w+') as inventory:
        # inventory.readlines()
        inventory.write("Country,Code,Product,Cost,Quantity\n")
        for lines in shoe_list:
            shoe_string = f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n"
            inventory.write(shoe_string)


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    menu = input("\n"'''Select one of the following options:
    rd - read shoe data
    cs - capture shoes
    va - view all
    r - restock
    s - search shoe
    vi - value per item
    h - highest quantity
    up - update list of shoes
    e - exit
    ''').lower()

    if menu == 'rd':  # calling the functions according to menu selection
        read_shoes_data()

    elif menu == 'cs':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 'r':
        re_stock()

    elif menu == 's':
        search_shoe()

    elif menu == 'vi':
        value_per_item()

    elif menu == 'h':
        highest_qty()

    elif menu == 'up':
        updated_shoe()

    elif menu == 'e':

        exit()

    else:
        print("Invalid option")
