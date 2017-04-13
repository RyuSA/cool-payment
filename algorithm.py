from Wallet import Wallet,coins
from itertools import product
from pulp import *
import sys
from time import time

def list_set(coin_list):
    return {coin : many for many, coin in zip(coin_list,coins)}

def set_list(coin_set):
    return coin_set.values

# return coin list of pay
def get_change(pay):
    ans = []
    for coin in reversed(coins):
        if pay > coin:
            ans.append(pay//coin)
            pay %= coin
        else :
            ans.append(0)
    ans.reverse()
    return ans

def list_price(coin_list):
    ans = 0
    for index,coin in enumerate(coins):
        ans += coin_list[index]*coin
    return ans

# show coin_list as 1yen : xx, 5yen : xx,...
def show_coin_list(coin_list):
    for index,coin in enumerate(coins):
        print(coin,end="")
        print("yen: " , end="")
        print(coin_list[index])

def Brute_algorithm(coin_list,price):
    """
    Input : coin_list = [1-yen, 5-yen,...10k-yen]
    price : price (integer)

    Example :
    coin_list = [2,1,5,0,4,1,2,0,0] -> 2957 yen
    price = 499
    """
    # ans is a coin_set
    min_ans = sys.maxsize
    all_coin_lists = [list(range(x+1)) for x in coin_list]

    for coin_list in product(*all_coin_lists):
        this_price = list_price(coin_list)
        if this_price >= price:
            temp = sum(get_change(this_price-price)) + sum(coin_list)
            if min_ans >= temp:
                min_pattern = coin_list[:]
                min_ans = temp
    return min_pattern

def Lp_solver(coin_list,price):
    if len(coin_list) != len(coins):
        print(coin_list,end="")
        print(" is illigal")
        return -1

    problem = LpProblem(sense=LpMinimize)
    pay = [LpVariable("PAY" + str(i),lowBound=0,cat=LpInteger) for i in range(len(coin_list))]
    change = [LpVariable("CHANGE" + str(i),lowBound=0,cat=LpInteger) for i in range(len(coin_list))]
    problem += lpSum(pay)+lpSum(change)
    problem += lpDot(pay,coins) - lpDot(change,coins) == price
    for coin,var in zip(coin_list,pay):
        problem += var <= coin
    if(problem.solve() == 1):
        return [int(value.value()) for value in pay]
    else :
        print("calc failed")
        return 0

test_case = [9,9,9,9,9,0,0,0,0]
price = 647

now = time()
for count in range(10):
    Lp_solver(test_case,price)
result = time() - now
print(result)

now = time()
for count in range(10):
    Brute_algorithm(test_case,price)
result = time() - now
print(result)
