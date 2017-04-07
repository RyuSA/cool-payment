from Wallet import Wallet

def breakdown(int_vec):
    return list(map(lambda x : int(x) , str(int_vec)))

# NOT YET
def Duty_algorithm(init,price):
    # ans = {#coin : how}
    ans = {}
    count = 0
    my_wallet = Wallet(init)
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
