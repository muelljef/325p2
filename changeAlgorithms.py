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


def changegreedy(coins, amount):
    minCoins = 0
    coinsUsed = [0] * len(coins)

    i = len(coins) - 1
    for coin in reversed(coins):
        while coin <= amount:
            amount -= coin
            minCoins += 1
            coinsUsed[i] += 1
        i -= 1
    print coinsUsed
    print minCoins

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
