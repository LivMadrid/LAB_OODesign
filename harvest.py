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

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

all_melon_types = []

def make_melon_types():
    """Returns a list of current melon types."""

    # Instantiate 4 melon types

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    all_melon_types.append(musk)
    musk.add_pairing('Mint')

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    all_melon_types.append(cas)
    cas.add_pairing('Strawberries')
    
    cas.add_pairing('Mint')

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    all_melon_types.append(cren)
    cren.add_pairing('Proscuitto')

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    all_melon_types.append(yw)
    yw.add_pairing('Ice Cream')

    return all_melon_types

make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pair in melon.pairings:
            print(f'- {pair}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melon_dictionary = {}
    
    for melon in melon_types:
        melon_dictionary[melon.code] = melon

    return melon_dictionary

make_melon_type_lookup(all_melon_types)

print(make_melon_type_lookup(all_melon_types))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, field, farmer):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.farmer = farmer
        
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable(self):
        if self.color_rating >= 5 and self.shape_rating >= 5 and self.field != 3:
            return True
        else:
            return False

melons_harvested = []

def make_melons(all_melon_types):
    """Returns a list of Melon objects."""
    
    melon_by_id = make_melon_type_lookup(all_melon_types)

    melon_1 = Melon(melon_by_id['yw'], 8, 9, 35, 'Michael')
    melons_harvested.append(melon_1)
    melon_2 = Melon(melon_by_id['yw'], 3, 4, 2, 'Sheila')
    melons_harvested.append(melon_2)   
    melon_3 = Melon(melon_by_id['yw'], 9, 8, 3, 'Sheila')
    melons_harvested.append(melon_3)
    melon_4 = Melon(melon_by_id['cas'], 10, 6, 35, 'Sheila')
    melons_harvested.append(melon_4)
    melon_5 = Melon(melon_by_id['cren'], 8, 9, 35, 'Michael')
    melons_harvested.append(melon_5)  
    melon_6 = Melon(melon_by_id['cren'], 8, 2, 35, 'Michael')
    melons_harvested.append(melon_6)
    melon_7 = Melon(melon_by_id['cren'], 2, 3, 4, 'Michael')
    melons_harvested.append(melon_7)
    melon_8 = Melon(melon_by_id['musk'], 6, 7, 4, 'Michael')
    melons_harvested.append(melon_8)   
    melon_9 = Melon(melon_by_id['yw'], 7, 10, 3, 'Sheila')
    melons_harvested.append(melon_9)

    return melons_harvested

make_melons(all_melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    #Print only, do not return anything
    for melon in melons:
        if melon.is_sellable():
            message = '(CAN BE SOLD)'
        else:
            message = '(NOT SELLABLE)'
            
        print(f'{melon.code.code} harvested by {melon.farmer} from Field {melon.field} {message}')

get_sellability_report(melons_harvested)


