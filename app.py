import argparse
import math

# Dog size to food requirements in lbs
SIZE_TO_FOOD_DICT = {
    'small': 10,
    'medium': 20,
    'large': 30
}

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
    parser = argparse.ArgumentParser(description="Calculate the amount of dog food required next month in pounds.")
    parser.add_argument("--small", type=int, default=0, help="The number of small dogs")
    parser.add_argument("--medium", type=int, default=0, help="The number of medium dogs")
    parser.add_argument("--large", type=int, default=0, help="The number of large dogs")
    parser.add_argument("--remaining_food", type=int, default=0, help="The number of remaining food")

    args = parser.parse_args()
    
    result = calculate_monthly_food(args.small, args.medium, args.large, args.remaining_food)
    print("The minimum order of dog food: %s lbs." % result)

if __name__ == "__main__":
    main()