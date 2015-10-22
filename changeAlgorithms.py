# !/usr/bin/env python
# title          :main.py
# description    :
# author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
# creation date  :
# last modified  :
# usage          :
# notes          :
# python_version :2.6.6
# ==============================================================================


def bruteforce(V,K):
        if K in V:
            return 1
        else:
            min_coins = float("inf")
            for j in range(1,K):
                num_coins1 = num_coins2 = 0
                num_coins1 += bruteforce(V,j)
                num_coins2 += bruteforce(V,K-j)
                #print("j=" + str(j) + "n1 = "+str(num_coins1)+" n2="+str(num_coins2))
                coin_count = num_coins1 + num_coins2
                if coin_count < min_coins:
                    min_coins = coin_count
            return min_coins

def changegreedy(coins, amount):
    min_coins = 0
    coins_used = [0] * len(coins)

    i = len(coins) - 1
    for coin in reversed(coins):
        while coin <= amount:
            amount -= coin
            min_coins += 1
            coins_used[i] += 1
        i -= 1
    print coins_used
    print min_coins

def changedp(coins, amount):
    #to initialize and append min coins for value of 0
    minCoins = []
    minCoins.append(0)
    #to initialize an 2d array to store coins used for different amounts
    coinsUsed = [[0 for x in range(len(coins))] for y in range(amount + 1)]

    for amt in range(1, amount + 1):
        subproblem_min = amt

        i = 0
        sub_min_coin = amount + 1
        for coin in coins:
            #if the amount is equal to a coin value, the min is 1
            if coin == amt:
                subproblem_min = 1
                coinsUsed[amt][i] = 1
                break

            if coin < amt:
                prev_target = amt - coin
                if (minCoins[prev_target] + 1) < subproblem_min:
                    subproblem_min = minCoins[prev_target] + 1
            i += 1
        minCoins.append(subproblem_min)

    print minCoins[amount]
    print coinsUsed[amount]
