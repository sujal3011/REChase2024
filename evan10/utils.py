import random


EVAN_NUMBERS = {2,9,10,12,35,37,38,49,50,52,56,135,139,141,142,149,150,153,154,156,163,165,166,169,170,172,177,178,180,184,195,197,198}
NON_EN = {i for i in range(1, 200) if i not in EVAN_NUMBERS}


def solve(x):
    ans = ''.join(map(lambda num: 'Y' if num in EVAN_NUMBERS else 'N', x))
    return ans


def makeSequence():
    evans = random.sample(EVAN_NUMBERS, random.randint(2, 5))
    non_evans = random.sample(NON_EN, 11 - len(evans))
    temp = evans + non_evans
    random.shuffle(temp)
    return temp
