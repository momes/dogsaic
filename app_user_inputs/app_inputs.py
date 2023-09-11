import math

# Dog size to food requirements in lbs
SIZE_TO_FOOD_DICT = {
    'small': 10,
    'medium': 20,
    'large': 30
}

def get_input(prompt):
    return input(prompt)

def get_positive_int_input(prompt):
    """
    Get an input and validate as positive integer

    Returns:
        int: valid positive integer input
    """
    while True:
        try:
            int_input = int(get_input(prompt))
            if int_input >= 0:
                return int_input
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.") 


def calculate_monthly_food(small, medium, large, remaining_food):
    """
    Calculate the amount of dog food required for order.
    Args:
        small (int): Number of small dogs.
        medium (int): Number of medium dogs.
        large (int): Number of large dogs.
        remaining_food (int): Remaining food in lbs.

    Returns:
        int: Dog food to order in lbs.
    """

    small_food = small * SIZE_TO_FOOD_DICT['small']
    medium_food = medium * SIZE_TO_FOOD_DICT['medium']
    large_food = large * SIZE_TO_FOOD_DICT['large']

    minimum_order = (small_food + medium_food + large_food - remaining_food) * 1.2 

    return int(math.ceil(max(minimum_order, 0)))

def main():
    # Get and validate order params
    small = get_positive_int_input('Small Dogs: ')
    medium = get_positive_int_input('Medium Dogs: ')
    large = get_positive_int_input('Large Dogs: ')
    remaining_food = get_positive_int_input('Remaining Food (lbs): ')

    result = calculate_monthly_food(small, medium, large, remaining_food)
    print("The minimum order of dog food: %s lbs." % result)

if __name__ == "__main__":
    main()