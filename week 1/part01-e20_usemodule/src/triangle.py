"""My module for triangle"""
# Enter you module contents here
__version__ = "1.0.1"
__author__ = "Tuija"


import math


# hypothenuse - return the length of the hypothenuse - parameter length of two other sides
def hypothenuse(l1, l2):
    """Hypothenuse function - takes 2 parameters and return calculated hypothenuse"""
    return math.sqrt(l1 ** 2 + l2 ** 2)

# area returns area - parameter two sides
def area(l1, l2):
    """Area function - takes 2 parameters and return calculated area"""
    return l1 * l2 / 2
