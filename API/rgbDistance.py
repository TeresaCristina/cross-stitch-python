# RGBDistance: compares two RGB numbers and calculates the distance between them
# Teresa Costa - Jun/2021

# Global variables
maxDiff = (255**2)*3


# General Functions
def diff(n_one, n_two):
    return n_one - n_two


def power(numb, ind=2):
    return numb ** ind


def distance(n_one, n_two):
    return power(diff(n_one, n_two))


def is_match(n_one, n_two):
    match = False
    if n_one == n_two:
        match = True
    return match


# Input Format: (xxx,xxx,xxx)
class RGBDistance:
    def __init__(self, rgb_number):
        self.r_number = rgb_number[0]
        self.g_number = rgb_number[1]
        self.b_number = rgb_number[2]

    def __eq__(self, rgb_other):
        if is_match(rgb_other.r_number, self.r_number) \
                and is_match(rgb_other.g_number, self.g_number) \
                and is_match(rgb_other.b_number, self.b_number):
            return True
        else:
            return False

    def r_number(self, rgb_other):
        return distance(rgb_other.r_number, self.r_number)

    def g_number(self, rgb_other):
        return distance(rgb_other.g_number, self.g_number)

    def b_number(self, rgb_other):
        return distance(rgb_other.b_number, self.b_number)

    def margin(self, rgb_other):
        return self.r_number(rgb_other) + self.g_number(rgb_other) + self.b_number(rgb_other)

    def match(self, rgb_other):
        match = False
        if rgb_other == self:
            match = True
        return match
