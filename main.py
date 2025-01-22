# ----- Module Two Lab -----
# return and break can be used almost interchangeably

# go to source control
# commit code to git repository
# go to squares on bottom of tools on left side and search python and install

# North Loop Provisions Donut Shop
# Your first python program for module two

# Northloop Provisions Donut Shop
# Module Two Project

# message to user
def welcome_message():
    # display welcome message
    print("Welcome to North Loop Provisions! ")
    print("Crafting artisinal donuts in Minneapolis' North Loop")
    print("-----------------------------------------") # separate message

# second function - go back to far left
def show_menu():
    # Display current donut menu
    menu = { # dictionary items
        "Classic Glazed": 3.50, # key has to be unique - cannot repeat menu item name
        "Maple Bacon": 4.50,
        "Spyhouse Coffee Flavor": 4.00,
        "Minnesota Berry": 4.25,
        "Local Honey": 4.00
    }

    print("\nToday's Donut Menu:")
    print("-------------------------------")
    for donut, price in menu.items(): # for loop to print donuts and price
        print(f"{donut}: ${price:.2f}") # format price at .2f two places after decimal point, and f string for format


# all the way to the left again
# start the main program
if __name__ == "__main__": # allow you to create main function - auto executes - calls first - calls all other functions - not required
    welcome_message() # call function
    show_menu() # call next function
    print("\nReady to serve our community with the finest donuts!")

    # our complete menu organized by category
    donut_menu = { # dictionary with key value pairs where value is list
        'Small Batch': [ # list nested inside dictionary
            'Wild Rice & Honey',
            'Maple Bacon',
            'Swedish Cardamom'
        ],
        'Seasonal': [
            'Apple Cider',
            'Joocy Lucy',
            'Lake of the Woods'
        ],
        'Local Collabs': [
            'Spyhouse Coffee Cake',
            'Fulton Beer & Pretzel',
            'Sweet Science Ice Cream'
        ]
        } # closing brace for dictionary

        # Locally-sourced toppings
toppings = [
    'House-Made Sprinkles',
    'Candied Hazlenuts',
    'Bee Pollen',
    'Cookie Butter Drizzle'
]

morning_sales = []

# record morning sales - by appending a transaction to the sales dictionary
morning_sales.append({
    'item': 'Wild Rice & Honey',
    'quantity': 2,
    'toppings': ['Bee Pollen'],
    'time': '7:30 AM'
})

# Display our current menu - using a for loop
print("Today's Morning Menu:")
for category, items in donut_menu.items():
    print(category + ":")
    for item in items: # nested for loop
        print(" - " + item)
    