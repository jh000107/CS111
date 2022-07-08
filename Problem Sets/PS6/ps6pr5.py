#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            deviation = std_dev(prices)
            print('The standard deviation is', deviation)
        elif choice == 5:
            index = max_day(prices)
            print('The max price is', prices[index], 'on day', index)
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            below = any_below(prices, threshold)
            if below == True:
                print('There is at least one price below', threshold)
            else:
                print('There are no prices below', threshold)
        elif choice == 7:
            most_profit = find_plan(prices)
            print(' Buy on day', most_profit[0], 'at price', prices[most_profit[0]])
            print('Sell on day', most_profit[1], 'at price', prices[most_profit[1]])
            print('Total profit:', most_profit[2])
        elif choice == 8:
            break
        
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')


def avg_price(prices):
    """ returns the average price
        input: prices --> a list of 1 or more prices
    """
    total_prices = 0
    num_prices = len(prices)
    for x in prices:
        total_prices += x
    average_price = total_prices / num_prices
    return average_price

def std_dev(prices):
    """ returns the standard deviation of the prices
        input: prices --> a list of 1 or more prices
    """
    sum_diff = 0
    num_prices = len(prices)
    for x in prices:
        squared_diff = (x - avg_price(prices))**2
        sum_diff += squared_diff
        standard_dev = math.sqrt(sum_diff/num_prices)
    return standard_dev

def max_day(prices):
    """ returns the day of the maximum price
        input: prices --> a list of 1 or more prices
    """
    max_index = 0
    max_price = prices[0]
    for x in range(len(prices)):
        if prices[x] > max_price:
            max_price = prices[x]
            max_index = x
    return max_index

def any_below(prices, threshold):
    count = 0
    for x in prices:
        if x < threshold:
            count += 1
    if count == 0:
        return False
    else:
        return True

def find_plan(prices):
    """ find the best days on which to buy and sell the stock whose prices
        are given in the list of prices
        input: prices --> a list of 2 or more prices
    """
    max_profit = 0
    for x in range(len(prices)):
        for y in range(x, len(prices)):
                diff = prices[y] - prices[x]
                if max_profit < diff:
                    buy_day = x
                    sell_day = y
                    max_profit = diff
    return [buy_day, sell_day, max_profit]
                
    


            
    
    
        
        

    
