#
# ps7pr4.py (Problem Set 7, Problem 4)
#
# TT Securities
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the min and its day')
    print('(6) Find the max and its day')
    print('(7) Test a threshold')
    print('(8) Your TT investment plan')
    print('(9) Quit')
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
    ## IMPORTANT: You will need to change this function so
    ## that it prints a table of days and prices.
    print('Day Price')
    print('--- -----')
    day = 0
    for i in range(len(prices)):
        print(day,'%7.2f'%prices[i])
        day = day + 1
    print('current prices:', prices)

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your helper functions for options 3-8 below.

def average(prices):
    """returns the average value of the list"""
    list_sum = 0
    for i in range (len(prices)):
        list_sum = list_sum + prices[i]
    list_avg = list_sum/(len(prices))
    return list_avg

def std(prices):
    """return the standard deviation value of the list"""
    list_sum = 0
    list_avg = average(prices)
    for a in range(len(prices)):
        sub = (prices[a] - list_avg)
        power = sub**2
        list_sum = list_sum + power
    div = list_sum/(len(prices))
    stdlist = div**0.5
    return div

def min_day(prices):
    """gets the minimum value in the list and the day in which
       the value is in"""
    m = prices[0]
    count = 0
    for x in prices:
        if x < m:
            count = count + 1
            m = x
    return (m, count)

def max_day(prices):
    """gets the maximum value in the list and the day in which
       the value is in"""
    m = prices[0]
    count = 0
    for x in prices:
        if x > m:
            count = count  + 1
            m = x
    return (m, count)

def threshold(prices):
    """gets a threshold value and tell if there is any price in the list
       that is bigger than the threshold value"""
    x = int(input('Enter threshold value: '))
    count = 0
    for i in prices:
        if i > x:
            count = count +1
    if count > 0:
        return "there is at least one price over "+ str(x)
    else:
        return "there is no price over " + str(x)

def profit(prices):
    """tell when to buy and when to sell to make the most profit"""
    maxdiff = prices[0] - prices[0]
    pos1 = 0
    pos2 = 0
    price1 = prices[pos1]
    price2 = prices[pos2]
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            d = prices[j] - prices[i]
            if d >= maxdiff:
                maxdiff  = d
                pos1 = i
                pos2 = j
                price1 = prices[pos1]
                price2 = prices[pos2]
                
    return maxdiff,pos1, pos2, price1, price2

    
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
        elif choice == 9:
            break
        elif choice < 9 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print('The average price is ', average(prices))
        elif choice == 4:
            print('The standard deviation is ', std(prices))
        elif choice == 5:
            print('The min price is '+ str(min_day(prices)[0])+
                   ' on day '+ str(min_day(prices)[1]))
        elif choice == 6:
            print('The max price is '+ str(max_day(prices)[0])+
                   ' on day '+ str(max_day(prices)[1]))
        elif choice == 7:
            print(threshold(prices))
        elif choice == 8:
            print("Buy on day " + str(profit(prices)[1]) + " at price "
                  + str(profit(prices)[3]))
            print("Sell on day " + str(profit(prices)[2]) + " at price "
                  + str(profit(prices)[4]))
            print("Total Profit: " + str(profit(prices)[0]))
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
