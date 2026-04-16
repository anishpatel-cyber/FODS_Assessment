'''
Program to create a class Dish with attributes:
dish_id, dish_name, ingredients, and instructions.
Also create a Cookbook class to manage a collection of dishes.
'''

# Define Dish class
class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions


# Define Cookbook class
class Cookbook:
    def __init__(self):
        # List to store dishes
        self.dishes = []

    # Method to add a dish to cookbook
    def add_dish(self, dish):
        self.dishes.append(dish)

    # Method to display all dishes
    def display_dishes(self):
        print("\nCookbook Dishes:\n")

        for dish in self.dishes:
            print("Dish ID:", dish.dish_id)
            print("Dish Name:", dish.dish_name)
            print("Ingredients:", dish.ingredients)
            print("Instructions:", dish.instructions)
            print("------------------------")


# Create Cookbook object
cookbook = Cookbook()

# Take input for one dish (can add more if needed)
dish_id = input("Enter Dish ID: ")
dish_name = input("Enter Dish Name: ")
ingredients = input("Enter Ingredients: ")
instructions = input("Enter Instructions: ")

# Create Dish object
dish = Dish(dish_id, dish_name, ingredients, instructions)

# Add dish to cookbook
cookbook.add_dish(dish)

# Display all dishes
cookbook.display_dishes()