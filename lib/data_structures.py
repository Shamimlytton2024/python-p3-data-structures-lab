
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Returns a list of names of the spicy foods.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of the spiciest foods (heat level > 5).
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Prints the name and heat level of each spicy food formatted with 🌶 emojis.
    """
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns the first spicy food that matches the given cuisine.
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
def print_spiciest_foods(spicy_foods):
    """
    Prints the name and heat level of the spiciest foods (heat level > 5) formatted with 🌶 emojis.
    """
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    """
    Returns the average heat level of all spicy foods.
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods) if spicy_foods else 0

def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy food to the list of spicy foods.
    """
    spicy_foods.append(spicy_food)
    return spicy_foods