def prime_num(n):
    #n=2であったら「素数」
    if n == 2:
        return True
        
    #nが2より小さい　or　偶数であれば「素数ではない」
    if (n < 2) or (n % 2 == 0):
        return False
        
    #nを2~(n-1)までの数で割り、あまりが0となるパターンがあれば「素数ではない」
    for i in range(2,n):
        if n % i == 0:
            return False
    #「if n % i == 0:」に引っかからずfor文が終われば「素数」
    return True

for n in range(101):            #1〜100までの数を素数判定する
        print("{} {}".format(n,prime_num(n)))