############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings = self.pairings.append(self.pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # self, code, first_harvest, color, is_seedless, is_bestseller, name
    
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    all_melon_types.append(musk)
    musk.add_pairing('Mint')

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    all_melon_types.append(cas)
    musk.add_pairing('Strawberries and Mint')

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    all_melon_types.append(cren)
    musk.add_pairing('Proscuitto')

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermellon')
    all_melon_types.append(yw)
    musk.add_pairing('Ice Cream')

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



