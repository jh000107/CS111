#
# point.py
#
# The beginnings of a class for Point objects
#
# CS 111
#

import math

class Point:
    """ A class for objects that represent points in
        the Cartesian plane.
    """
    
    def __init__(self, init_x, init_y):
        """ constructor for a Point object that represents a point
            with coordinates (init_x, init_y)
        """
        self.x = init_x
        self.y = init_y

    def distance_from_origin(self):
        """ computes and returns the distance of the called Point object
            (self) from the origin (i.e., from (0, 0))
        """
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist

    def move_down(self, amount):
        """ moves the called Point object (self) in a downwards
            direction by the specified amount
        """
        self.y -= amount
        
    def __repr__(self):
        """ returns a string representation for the called Point
        object (self)
        """
        s = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return s

    def quadrant(self):
        """ returns the number of the quadrant (if any)
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0
        
    def __eq__(self, other):
        """ returns True if the called Point object (self) has the same
            coordinates as the Point object other, and False otherwise
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def flip(self):
        """ negates and swaps the coordinates of the called Point object
        """
        a = self.x
        self.x = -1 * self.y
        self.y = -1 * a

    def in_same_quadrant(self, other):
        """ returns True if the called Point object and the other Point object
            are on same quadrants. False otherwise
        """
        if self.quadrant() == 0 or other.quadrant() == 0:
            return False
        elif self.quadrant() == other.quadrant():
            return True
        else:
            return False

    
