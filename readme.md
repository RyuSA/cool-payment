# cool-purchase

## Valuables

### - Given
- your wallet
- Yen

### - Input
- price

### - Output
- your payment

> the number of coins/bills in your wallet should be minimized

## Algorithm

### variables

- coin_list : [3, 0, 2, 0, 1, 0, 0, 0, 0] = 123yen
- coin_set : {1:3, 5:0, 10:2, 50:0, 100:1, 500:0, 1000:0, 5000:0, 10000:0} = 123yen

- Wallet :
  - inside : coin_set of this wallet ; {1:xx, 5::xx, 10:xx,...}
  - is_payable(price) : return True if this wallet can pay price
  - show_my_wallet() : print all inside of this wallet
  - __init__(my_before_wallet) : my_before_wallet is a coin_list and added into wallet.inside

### functions

- breakdown(price) : breakdown(123) = [1,2,3]
- list_set(coin_list) : return coin_set of coin_list
- set_list(coin_set) : return coin_list of coin_set

### Mathematical description
Let "before wallet" be your wallet before your purchase.
I want to find such int "after wallet" that
<img src="https://latex.codecogs.com/gif.latex?after\&space;wallet&space;=&space;min\{&space;\&hash;(p):&space;before\&space;wallet&space;\geq&space;p&space;\&space;and\&space;price&space;\geq&space;p&space;\}" title="after\ wallet = min\{ \#(p): before\ wallet \geq p \ and\ price \geq p \}" />

> #(integer) means the number of coins/bills of integer
