#
# Lab 7
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('0) Input new goal lists')
    print('1) Get the latest score')
    print('2) Find the max number of goals')
    print('3) Find the number of wins')
    print('4) Print the results')
    
    ## Add any new menu options here.


    print('7) Quit')
    print()

def latest_score(bruins, opponents):
    """ returns the score of the latest (i.e., most recent) game
        inputs: bruins - a list of goals scored by the Bruins in a 
                  set of games
                opponents - a list of goals scored by their opponents
        We assume that both lists contain the same number of integers,
        and that they each contain at least one integer.
    """
    score = str(bruins[-1]) + '-' + str(opponents[-1])
    return score

## Add your helper functions for the remaining options below.
            

def main():
    """ the main user-interaction loop
    """
    bruins = []
    opponents = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            bruins = eval(input('Enter the Bruins list of goals: '))
            opponents = eval(input('Enter their opponents list of goals: '))
            if len(bruins) != len(opponents):
                print('The lists must have the same length.')
                print('Please select menu option 0 to try again.')
                bruins = []
                opponents = []
        elif choice == 7:
            break
        elif choice < 7 and len(bruins) == 0:
            print('You need to first enter the goal lists.')
            print('Please select menu option 0 to do so.')
        elif choice == 1:
            score = latest_score(bruins, opponents)
            print('The score of the latest game was', score)
        ## add code to process the other choices here
        elif choice == 2:
            maxgoals = find_max_goals(goals)
            print('Max goals: ' + str(maxgoals))


        else:
            print('Invalid choice. Please try again.')

    print('Goodbye!')

def find_max_goals(goals):
    """ returns the largest number of goals in the specified 
        list of goals, which we assume contains at least one integer
    """
    maxg = goals[0]

    for g in goals:
        if g > maxg:
            maxg = g

    return maxg

    
