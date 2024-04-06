import random

NOT_ODD = {4,5,9,11,12,13,14,18,19,20,24,25,29,30,34,35,39,41,42,43,46,47,48,51,52,53,56,57,58,61,62,63,66,67,68,71,72,73,76,77,78,80,84,85,88,89,90,94,95,98,99,100}
ODD = {i for i in range(1, 100) if i not in NOT_ODD}


def solve(x):
    ans=0
    for ele in range(0, len(x)):
        if x[ele] in NOT_ODD:
            ans = ans + x[ele]
    return ans


def makeSequence():
    not_odds = random.sample(NOT_ODD, 3)
    odds = random.sample(ODD, random.randint(2,7))
    temp = not_odds + odds
    random.shuffle(temp)
    return temp
