#CIS 1051 Section 9
#Linh Nguyen

import random
"""
games = int(input("Games? "))
def AveragePigTurns(games):
    turntotal = 0
    AverageTurns = 0
    score = 0
    dice = 0
    for i in range(games):
        while (score + turntotal) < 100 and turntotal < 20 and dice != 1:
            dice = random.randint(1,6)
            AverageTurns += 1
            score += dice
            turntotal += 1
        score = 0
        turntotal = 0
        dice = 0
    return AverageTurns/games
    
print("Average Turns:", AveragePigTurns(games))"""

games = int(input("Games? "))
def holdAt20_Or_GoalGame():
    turn = 0
    total = 0
    score = 0
    for i in range(games):
        while total < 20 or total + score < 100:
            roll = random.randint(1,6)
            #print("Roll:", roll)
            total = total + roll
            if roll == 1:
                total = 0
                turn += 1
                #print('Turn total:', total)
                #print('New score:', score)
            elif total >= 20 or total + score >= 100:
                score += total
                turn += 1
                #print('Turn total:', total)
                #print('New score:', score)
    return turn/games
print(holdAt20_Or_GoalGame())
