### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

###returns true or false
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        ### for loop with key, value and ingredients using items
        for food, amount in ingredients.items():
            ###if the amount is bigger than resources available, then false
            if amount > self.machine_resources[food]:
                #not enough resources
                print("Sorry there is not enough " + food)
                return False
        return True

### creates total to be used later
    def process_coins(self):
        total = 0
        print("input money here:")
        dollars = int(input("how many dollars? ")) * 1
        halfdollars = int(input("how many half dollars? ")) *.5
        quarters = int(input("how many quarters? ")) * .25
        nickels = int(input("how many nickels? ")) *.05
        total += dollars + halfdollars + quarters + nickels
        return total

### gives back money thats extra
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: uerse the output of process_coins() function for cost input"""
        if coins >= cost:
            giveback = coins - cost
            print(f"Here is ${giveback} in change")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
### updates resources for sandwiches
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for food, amount in order_ingredients.items():
            self.machine_resources[food] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']}")
        print(f"Ham: {self.machine_resources['ham']}")
        print(f"Cheese: {self.machine_resources['cheese']}")

###main loop logic below
### Make an instance of SandwichMachine class and write the rest of the codes ###
sandy = SandwichMachine(resources)
turned_on = True
while turned_on:
    select = input("What would you like? (small/ medium/ large/ off/ report)")
    if select == "off":
        turned_on = False
    elif select == 'report':
        sandy.report()
    elif select in recipes:
        sandwich = recipes[select]

        if sandy.check_resources(sandwich["ingredients"]):
            coins = sandy.process_coins()

            if sandy.transaction_result(coins, sandwich["cost"]):
                sandy.make_sandwich(select, sandwich["ingredients"])
    else:
        print("Couldn't create sandwich.")

