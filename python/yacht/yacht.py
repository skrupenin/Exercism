# Score categories
# Change the values as you see fit
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

q_ONES = q_TWOS = q_THREES = q_FOURS = q_FIVES = q_SIXES = -1


def calc_YACHT(dice):
    return 50*( max([q_ONES, q_TWOS, q_THREES, q_FOURS, q_FIVES, q_SIXES])>=5 )

def calc_ONES(dice):
    return q_ONES*1

def calc_TWOS(dice):
    return q_TWOS*2

def calc_THREES(dice):
    return q_THREES*3

def calc_FOURS(dice):
    return q_FOURS*4

def calc_FIVES(dice):
    return q_FIVES*5

def calc_SIXES(dice):
    return q_SIXES*6

def calc_FULL_HOUSE(dice):
    _max=max([q_ONES, q_TWOS, q_THREES, q_FOURS, q_FIVES, q_SIXES])
    _min=min(filter(lambda x: x>0, [q_ONES, q_TWOS, q_THREES, q_FOURS, q_FIVES, q_SIXES]))
    return (_max==3 and _min==2)*sum(dice)

def calc_FOUR_OF_A_KIND(dice):
    return ((q_ONES>=4)*1 + (q_TWOS>=4)*2+ (q_THREES>=4)*3 + (q_FOURS>=4)*4 + (q_FIVES>=4)*5 + (q_SIXES>=4)*6)*4

def calc_LITTLE_STRAIGHT(dice):
    return (q_ONES == q_TWOS == q_THREES == q_FOURS == q_FIVES == 1) * 30
 
def calc_BIG_STRAIGHT(dice):
    return (q_TWOS == q_THREES == q_FOURS == q_FIVES == q_SIXES == 1) * 30

def calc_CHOICE(dice):
    return sum(dice)




def score(dice, category):
    global q_ONES, q_TWOS, q_THREES, q_FOURS, q_FIVES, q_SIXES
    q_ONES=dice.count(1)
    q_TWOS=dice.count(2)
    q_THREES=dice.count(3)
    q_FOURS=dice.count(4)
    q_FIVES=dice.count(5)
    q_SIXES=dice.count(6)
 
 
    cat_swither={
        YACHT : calc_YACHT,
        ONES : calc_ONES,
        TWOS : calc_TWOS,
        THREES : calc_THREES,
        FOURS : calc_FOURS ,
        FIVES : calc_FIVES ,
        SIXES : calc_SIXES ,
        FULL_HOUSE : calc_FULL_HOUSE ,
        FOUR_OF_A_KIND : calc_FOUR_OF_A_KIND ,
        LITTLE_STRAIGHT : calc_LITTLE_STRAIGHT ,
        BIG_STRAIGHT : calc_BIG_STRAIGHT ,
        CHOICE : calc_CHOICE ,
        }
 
    return cat_swither[category](dice)

if __name__ == '__main__':  
    print score([5, 3, 3, 5, 3], FULL_HOUSE)
    print q_ONES, q_TWOS, q_THREES, q_FOURS, q_FIVES, q_SIXES
