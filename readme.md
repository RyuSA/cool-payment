# cool-purchase

## purpose
支払いの時、例えば499円の支払いであるとき、いくら払うだろうか？499円ぴったり、もしくは500円玉一枚、はたまた別の物か……

よくある「お釣りの最小化アルゴリズム」の解でいえば、499円で出すのが最適であるというだろう。
……これでは本末転倒ではないのか？結局、14枚もの硬貨を手渡すことになるのだから……

そこで、「支払いとお釣りの最小化アルゴリズム」に挑戦してみようと考えた
以下、がんばってみた証である……

In your purchase, if the amount is 499 yen, how much do you gonna pay?
just 499-yen? or 500-yen? or other?

what is called "minimized-change algorithm" returns 499-yen, which doesn't make sense; 14 coins in total.

So I tried to create "minimized Pay-Change algorithm" below.

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

### Mathematical description
Let my_before_wallet be your wallet before your purchase.
I want to find such int my_after_wallet that
<img src="https://latex.codecogs.com/gif.latex?my_after_wallet = min{#(p) :my_before_wallet >= p and p <= price}"/>

> #(integer) means the number of coins/bills of integer
