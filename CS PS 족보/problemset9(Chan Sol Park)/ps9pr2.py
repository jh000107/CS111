#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A class to represent calendar dates
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

    def tomorrow(self):
        """changes the called object so that it represents one
           calendar day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.is_leap_year():
            days_in_month[2] = 29
        self.day = self.day + 1

        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month = self.month + 1

        if self.month > 12:
            self.month = 1
            self.year = self.year + 1

    def add_n_days(self, n):
        """changes the calling object so that it represents n calendar
           days after the date it originally represented. Additionally,
           the method should print all of the dates from the starting date
           to the finishing date, inclusive of both endpoints.
        """
        print(self)
        for r in range(n):
            self.tomorrow()
            print(self)
            
    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other)
           represent the same calendar date.
        """
        return (self.day == other.day
                and self.month == other.month
                and self.year == other.year)

    def is_before(self, other):
        """returns True if the called object represents a calendar date that
           occurs before the calendar date that is represented by other.
        """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif (self.day < other.day
             and self.month == other.month
             and self.year == other.year):
            return True
        else:
            return False

    def is_after(self, other):
        """returns True if the calling object represents a calendar date that
           occurs after the calendar date that is represented by other.
        """
        if self.year > other.year:
            return True
        elif self.month > other.month and self.year == other.year:
            return True
        elif (self.day > other.day
             and self.month == other.month
              
             and self.year == other.year):
            return True
        else:
            return False

    def diff(self, other):
        """returns an integer that represents the number of days between self
           and other.
        """
        days = 0
        x = self.copy()
        y = other.copy()

        if self.is_before(other) == True:
            while x != y:
                x.tomorrow()
                days += 1
            return days*-1
            
        elif self.is_after(other) == True:
            while y != x:
                y.tomorrow()
                days += 1
            return days
                
        else:
            return 0

    def day_of_week(self):
        """returns a string that indicates the day of the week of the Date object
           that calls it.
        """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        mon = Date(11, 14, 2016)
        diff = self.diff(mon) % 7
        return day_of_week_names[diff]
