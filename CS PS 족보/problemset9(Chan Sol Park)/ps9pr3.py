#
# ps9pr3.py (Problem Set 9, Problem 3)
#
# Date Clients
#

from ps9pr2 import Date

def get_age_on(birthday, other):
            """accepts two Date objects as parameters: one to represent a
               person’s birthday, and one to represent an arbitrary date.
               The function then returns the person’s age on that date as
               an integer.
            """
            x = birthday.copy()
            y = other.copy()
            age = 0

            if birthday.is_before(other) == True:
                        while x != y:
                                    if (x.day == y.day
                                       and x.month == y.month
                                       and x.year != y.year):
                                                age = age + 1
                                    x.tomorrow()
                        return age
            

def print_birthdays(filename):
            """accepts a string filename as a parameter. The function then opens
               the file that corresponds to that filename, read through the file,
               and print some information derived from that file.
            """
            file = open(filename, 'r')
            for line in file:
                        x = line.split(',')
                        name = x[0]
                        month = x[1]
                        day = x[2]
                        year = x[3]
                        day = Date(int(month), int(day), int(year))
                        d = str(day)
                        print (name,'('+ d +')','('+day.day_of_week()+')')
            file.close()
