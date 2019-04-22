import random

east = [
        {'name': 'Duke', 'confchamp': True ,'rpi': .673 , 'titles': 5, 'power5': True, 'seed': 1},
        {'name': 'NDSU', 'confchamp': True ,'rpi': .498 , 'titles': 0, 'power5': False, 'seed': 16},
        {'name': 'VCU', 'confchamp': True ,'rpi': .602 , 'titles': 0, 'power5': False, 'seed': 8},
        {'name': 'UCF', 'confchamp': False ,'rpi': .608 , 'titles': 0, 'power5': False, 'seed': 9},
        {'name': 'Mississippi St.', 'confchamp': False ,'rpi': .603 , 'titles': 0, 'power5': True, 'seed': 5},
        {'name': 'Liberty', 'confchamp': True ,'rpi': .554 , 'titles': 0, 'power5': False, 'seed': 12},
        {'name': 'Virginia Tech', 'confchamp': False ,'rpi': .614 , 'titles': 0, 'power5': True, 'seed': 4},
        {'name': 'Saint Louis', 'confchamp': True ,'rpi': .546 , 'titles': 0, 'power5': False, 'seed': 13},
        {'name': 'Maryland', 'confchamp': False ,'rpi': .606 , 'titles': 0, 'power5': True, 'seed': 6},
        {'name': 'Belmont', 'confchamp': False ,'rpi': .581 , 'titles': 0, 'power5': False, 'seed': 11},
        {'name': 'LSU', 'confchamp': False ,'rpi': .632 , 'titles': 0, 'power5': True, 'seed': 3},
        {'name': 'Yale', 'confchamp': True ,'rpi': .572 , 'titles': 0, 'power5': False, 'seed': 14},
        {'name': 'Louisville', 'confchamp': False ,'rpi': .590 , 'titles': 0, 'power5': True, 'seed': 7},
        {'name': 'Minnesota', 'confchamp': False ,'rpi': .581 , 'titles': 0, 'power5': True, 'seed': 10},
        {'name': 'Michigan State', 'confchamp': True ,'rpi': .651 , 'titles': 0, 'power5': True, 'seed': 2},
        {'name': 'Bradley', 'confchamp': True ,'rpi': .502 , 'titles': 0, 'power5': False, 'seed': 15}
    ]

south = [
    {'name': 'Virginia', 'confchamp': False ,'rpi': .658 , 'titles': 0, 'power5': True, 'seed': 1},
    {'name': 'Gardner-Webb', 'confchamp': True ,'rpi': .520 , 'titles': 0, 'power5': False, 'seed': 16},
    {'name': 'Ole Miss', 'confchamp': False ,'rpi': .555 , 'titles': 0, 'power5': True, 'seed': 8},
    {'name': 'Oklahoma', 'confchamp': False ,'rpi': .584 , 'titles': 0, 'power5': True, 'seed': 9},
    {'name': 'Wisconsin', 'confchamp': False ,'rpi': .602 , 'titles': 6, 'power5': True, 'seed': 5},
    {'name': 'Oregon', 'confchamp': True ,'rpi': .586 , 'titles': 0, 'power5': True, 'seed': 12},
    {'name': 'Kansas State', 'confchamp': False ,'rpi': .616 , 'titles': 0, 'power5': True, 'seed': 4},
    {'name': 'UC Irvine', 'confchamp': True ,'rpi': .562 , 'titles': 0, 'power5': False, 'seed': 13},
    {'name': 'Villanova', 'confchamp': True ,'rpi': .616 , 'titles': 0, 'power5': False, 'seed': 6},
    {'name': 'Saint Marys', 'confchamp': True ,'rpi': .581 , 'titles': 0, 'power5': False, 'seed': 11},
    {'name': 'Purdue', 'confchamp': False ,'rpi': .630 , 'titles': 0, 'power5': True, 'seed': 3},
    {'name': 'Old Dominion', 'confchamp': True ,'rpi': .557 , 'titles': 0, 'power5': False, 'seed': 14},
    {'name': 'Cincinnati', 'confchamp': True ,'rpi': .622 , 'titles': 0, 'power5': False, 'seed': 7},
    {'name': 'Iowa', 'confchamp': False ,'rpi': .574 , 'titles': 0, 'power5': True, 'seed': 10},
    {'name': 'Tennessee', 'confchamp': False ,'rpi': .649 , 'titles': 0, 'power5': True, 'seed': 2},
    {'name': 'Colgate', 'confchamp': True ,'rpi': .546 , 'titles': 0, 'power5': False, 'seed': 15}
]
midwest = [
    {'name': 'UNC', 'confchamp': False ,'rpi': .656 , 'titles': 6, 'power5': True, 'seed': 1},
    {'name': 'Iona', 'confchamp': True ,'rpi': .485 , 'titles': 0, 'power5': False, 'seed': 16},
    {'name': 'Utah State', 'confchamp': True ,'rpi': .598 , 'titles': 0, 'power5': False, 'seed': 8},
    {'name': 'Washington', 'confchamp': False ,'rpi': .584 , 'titles': 0, 'power5': True, 'seed': 9},
    {'name': 'Auburn', 'confchamp': True ,'rpi': .628 , 'titles': 0, 'power5': True, 'seed': 5},
    {'name': 'New Mexico State', 'confchamp': True ,'rpi': .575 , 'titles': 0, 'power5': False, 'seed': 12},
    {'name': 'Kansas', 'confchamp': False ,'rpi': .654 , 'titles': 0, 'power5': True, 'seed': 4},
    {'name': 'Northeastern', 'confchamp': True ,'rpi': .569 , 'titles': 0, 'power5': False, 'seed': 13},
    {'name': 'Iowa State', 'confchamp': True ,'rpi': .594 , 'titles': 0, 'power5': True, 'seed': 6},
    {'name': 'Ohio State', 'confchamp': False ,'rpi': .563 , 'titles': 0, 'power5': True, 'seed': 11},
    {'name': 'Houston', 'confchamp': False ,'rpi': .650 , 'titles': 0, 'power5': False, 'seed': 3},
    {'name': 'Georgia State', 'confchamp': True ,'rpi': .573 , 'titles': 0, 'power5': False, 'seed': 14},
    {'name': 'Wofford', 'confchamp': True ,'rpi': .610 , 'titles': 0, 'power5': False, 'seed': 7},
    {'name': 'Seton Hall', 'confchamp': False ,'rpi': .575 , 'titles': 0, 'power5': False, 'seed': 10},
    {'name': 'Kentucky', 'confchamp': False ,'rpi': .650 , 'titles': 0, 'power5': True, 'seed': 2},
    {'name': 'Abilene Christian', 'confchamp': True ,'rpi': .524 , 'titles': 0, 'power5': False, 'seed': 15}
    ]
west = [
    {'name': 'Gonzaga', 'confchamp': False ,'rpi': .647 , 'titles': 0, 'power5': False, 'seed': 1},
    {'name': 'Fairleigh Dickinson', 'confchamp': True ,'rpi': .494 , 'titles': 0, 'power5': False, 'seed': 16},
    {'name': 'Syracuse', 'confchamp': False ,'rpi': .576 , 'titles': 0, 'power5': True, 'seed': 8},
    {'name': 'Baylor', 'confchamp': False ,'rpi': .570 , 'titles': 5, 'power5': True, 'seed': 9},
    {'name': 'Marquette', 'confchamp': False ,'rpi': .594 , 'titles': 5, 'power5': False, 'seed': 5},
    {'name': 'Murray State', 'confchamp': True ,'rpi': .584 , 'titles': 0, 'power5': False, 'seed': 12},
    {'name': 'Florida State', 'confchamp': False ,'rpi': .644 , 'titles': 0, 'power5': True, 'seed': 4},
    {'name': 'Vermont', 'confchamp': True ,'rpi': .558 , 'titles': 0, 'power5': False, 'seed': 13},
    {'name': 'Buffalo', 'confchamp': True ,'rpi': .637 , 'titles': 0, 'power5': False, 'seed': 6},
    {'name': 'Arizona State', 'confchamp': False ,'rpi': .582 , 'titles': 0, 'power5': True, 'seed': 11},
    {'name': 'Texas Tech', 'confchamp': False ,'rpi': .629 , 'titles': 0, 'power5': True, 'seed': 3},
    {'name': 'Northern Kentucky', 'confchamp': True ,'rpi': .540 , 'titles': 0, 'power5': False, 'seed': 14},
    {'name': 'Nevada', 'confchamp': False ,'rpi': .606 , 'titles': 0, 'power5': False, 'seed': 7},
    {'name': 'Florida', 'confchamp': False ,'rpi': .573 , 'titles': 0, 'power5': True, 'seed': 10},
    {'name': 'Michigan', 'confchamp': False ,'rpi': .640 , 'titles': 0, 'power5': True, 'seed': 2},
    {'name': 'Montana', 'confchamp': True ,'rpi': .551 , 'titles': 0, 'power5': False, 'seed': 15}
]



#algorithms
def randnum(t1, t2):
    n = random.randrange(0, 2)
    
    if n == 0:
       return t1
    else:
        return t2

def rpi(t1, t2):
    weigting1 = t1['rpi']
    weigting2 = t2['rpi']
    
    if weigting1 > weigting2:
        return t1
    else:
        return t2

def rpi_plus(t1, t2):
    weigting1 = t1['rpi']
    weigting2 = t2['rpi']

    if t1['power5'] and t1['confchamp'] == True:
        weigting1 += .05
    if t2['confchamp'] == True:
        weigting2 += .05
        
    if weigting1 > weigting2:
        return t1
    else:
        return t2

def play_round(teams):
    winners = []
    
    for a in range(len(teams)//2):
        b = len(teams) - 1 - a
        w = rpi_plus(teams[a], teams[b])
        winners.append(w)

    return winners


# tourney
print ('-------------West Region------------------')
while len(west) > 1:
    west = play_round(west)

    for team in west:
        print (team['name'])
    print()    

print ('-------------East Region------------------')
while len(east) > 1:
    east = play_round(east)

    for team in east:
        print (team['name'])
    print()

print ('-------------Midwest Region------------------')

while len(midwest) > 1:
    midwest = play_round(midwest)

    for team in midwest:
        print (team['name'])
    print()

print ('-------------South Region------------------')

while len(south) > 1:
    south = play_round(south)

    for team in south:
        print (team['name'])
    print()
    
    
print('-------------Final Four------------------')
print ('The Winner of the East Region is...' + east[0]['name'])
print ('The Winner of the West Region is...' + west[0]['name'])
print ('The Winner of the South Region is...' + south[0]['name'])
print ('The Winner of the Midwest Region is...' + midwest[0]['name'])

final_four = east + south + midwest + west

while len(final_four) > 1:
    final_four = play_round(final_four)

    for team in final_four:
        print (team['name'])
    print()

    



























   
