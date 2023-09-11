# DOGsaic™ - a Mosaic dog food calculator
<img src="https://dorian-album-covers.s3.amazonaws.com/IMG_0106.jpg" alt="Logo" width="300" >


This dog food calculator calculates how much dog food is required for a month, based on the number of dogs per size (small, medium, large) and the amount of remaining dog food from the previous month.

## Getting Started


### Installing

Cloning the repo
```
git clone https://github.com/momes/dogsaic.git
cd dogsaic
```

### Usage

Run the script by passing the following parameters:

* --small: (int) number of small dogs
* --medium: (int) number of medium dogs
* --large: (int) number of large dogs
* --remaining_food: (int) remaining_food in pounds
```
python app.py --small 3 --medium 1 --large 4 --remaining_food 15
```

This will return an integer of the minimum pounds of food to purchase for next month's dog food order.

## Help

The number of dogs and remaining_food must be a number greater than zero. 

If the remaining food is greater than the minimum order of dog food, the order result will be 0.

## Running Tests

To run tests:

```
python test_app.py
```
## Authors

Contributors names and contact info

Mo Valentini
[@momes](https://github.com/momes)
