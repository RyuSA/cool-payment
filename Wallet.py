class Wallet:
    coins = [1,5,10,50,100,500,1000,5000,10000]
    # my_before_wallet = [1yen , 5yen, ..., 1k-yen, 5k-yen, 10k-yen]
    # don't care 2k-yen bill
    inside = {}
    def __init__(self, my_before_wallet):
        if len(self.coins) != len(my_before_wallet):
            print("my_before_wallet is illigal")

        for one in range(len(self.coins)):
            self.inside[self.coins[one]] = my_before_wallet[one]

    def show_my_wallet(self):
        print("Now, your wallet has ...")
        for one in self.coins:
            print(one, end="")
            print(" Yen : " , end="")
            print(self.inside[one])
        print("the number of coins/bills =  : ", end="")
        print(sum(self.inside.values()))
        print("The total value of my wallet = " , end="")
        print(sum(map(lambda x : x*self.inside[x], self.coins)))
