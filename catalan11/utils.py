import random
CATALAN = [1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440,9694845]


def solve(index):
    index = int(index)
    ans = CATALAN[index-2]+1
    return ans


def chooseIndex():
    index = random.randint(8, 17)
    return index
