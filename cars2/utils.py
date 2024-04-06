import random




def solve(x):
    # x is a list having 2 hexadecimal strings 
    num1 = int(x[0], 16)
    num2 = int(x[1],16)
    ans = abs(num1-num2)
    # ans = 17
    return ans


def makeSequence():
    # one = format(random.randint(2560,4095),"x").upper() #a00 fff
    # two = format(random.randint(2560,4095),"x").upper()
    a ,b = random.sample(range(2560,4096),2)
    one = format(a,"x").upper()
    two = format(b,"x").upper()
    my_hex_list = [one,two]
    return my_hex_list
    
