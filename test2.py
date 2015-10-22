# def changeslow(K,coins):
#    if K == 0:
#        return 0
#    result = float("inf") #set value to high initially
#
#    #for each i(coin at i-th) < K (target amount)
#    #find the minimum for sublist K-i and keep result
#    for coin in coins:
#        if coin <= K:
#            result = min(result, changeslow(K - coin,coins) + 1)
#    return result

def changeslow(K,coins):
    minCoins = K
    if K in coins:
        print("base: K="+str(K)+", returning 1 to last call")
        return 1
    else:
        for coin in coins:
            if coin<=K:
                print("minCoins="+str(minCoins)+" VS calling on="+str(K) +"-"+str(coin) +"="+ str(K-coin))
                minCoins = min(minCoins,1+changeslow(K-coin,coins))
    return minCoins

coin_list = [1,2,3]
target_amount = 5

print changeslow(target_amount,coin_list)


def changedp(amount, coins):
    min_coins = [[0 for x in range(len(coins))] for y in range(amount + 1)]  # amt+1 because we want a left-most zero column
    coins_used = [[0 for x in range(len(coins))] for y in range(amount + 1)]  # amt+1 because we want a left-most zero column
    for a in range(1,amount+1):
        j=0
        col_min=float("inf")
        bool_coin = False
        for j, d in enumerate(coins):
            if d <= a: #change possible
                if (min_coins[a - d][j] + 1) <= col_min:
                    col_min = min_coins[a][j] = min_coins[a - d][j] + 1
                    sub_mincoin = d
                    sub_minpos = j
                    bool_coin = True
            for x in range(j+1,len(coins)):
                min_coins[a][x] = col_min
        if bool_coin:
            for y in range(len(coins)):
                coins_used[a][y]=coins_used[a-sub_mincoin][y] #transfer the column and what it used in that column to make up the min
            coins_used[a][sub_minpos] +=1
    print(coins_used[a])
    print min_coins[a][j]

# c1=[1, 5, 10, 25, 50]
# a1=75
# c2=[1, 10, 21, 50]
# a2=63
# c3=[1, 2, 4, 8, 16]
# a3=120
# c4=[1,2,4,8]
# a4=15
# changedp(a1, c1)
# changedp(a2, c2)
# changedp(a3, c3)
#
# changedp(a4, c4)
