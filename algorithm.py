from Wallet import Wallet,coins

# 12345 -> [1,2,3,4,5]
def breakdown(int_vec):
    return list(map(lambda x : int(x) , str(int_vec)))

def list_set(coin_list):
    temp = {}
    for many, coin in zip(coin_list,coins):
        temp[coin] = many
    return temp

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

# show coin_list as 1yen : xx, 5yen : xx,...
def show_coin_list(coin_list):
    for index,coin in enumerate(coins):
        print(coin,end="")
        print("yen: " , end="")
        print(coin_list[index])

# NOT YET
def Duty_algorithm(init,price):
    # ans is a coin_set
    ans = {}
    for coin in coins:
        ans[coin] = 0

    count = 0
    my_wallet = Wallet(init)
    # breakdown price
    price = breakdown(price)

    for index,p in enumerate(price):
        if p > 9:
            price[index+1] += 1
            continue
        elif p == 0 :
            continue
        else :
            if p < 5 :
                pay5()
                pay10()
                payP()

print(get_change(123))
