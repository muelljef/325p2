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


def changeslow(coins, amount, used_list):
    if sum(used_list) == amount: #sum of the list is the amount
        yield used_list
    elif sum(used_list) > amount:
        pass
    elif coins == []:
        pass
    else:
        for coin in changeslow(coins, amount, used_list+[coins[0]]):
            yield coin
        for coin in changeslow(coins[1:], amount, used_list):
            yield coin

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
    return min_coins, coins_used

def changedp2(coins, amount):
    # to initialize min coins with index corresponding to amount
    min_coins = [0]
    # to initialize an 2d array to store coins used for different amounts
    # first index corresponds to amount, 2nd index to coins
    coins_used = [[0 for x in range(len(coins))] for y in range(amount + 1)]

    for amt in range(1, amount + 1):
        subproblem_min = amt
        i = 0
        bool_coin = False
        for coin in coins:
            # if the amount is equal to a coin value, the min is 1
            if coin == amt:
                bool_coin = False
                # setting to zero because we add one later
                subproblem_min = 0
                for y in coins_used[amount]:
                    y = 0
                coins_used[amt][i] = 1
                break

            if coin < amt:
                prev_target = amt - coin
                if (min_coins[prev_target]) < subproblem_min:
                    subproblem_min = min_coins[prev_target]
                    sub_mincoin = coin
                    sub_minpos = i
                    bool_coin = True
            i += 1

        min_coins.append(subproblem_min + 1)
        if bool_coin:
            for x in range(len(coins)):
                coins_used[amt][x] = coins_used[amt - sub_mincoin][x]
            coins_used[amt][sub_minpos] += 1
    return min_coins[amount], coins_used[amount]

def changedp(coins,amount):
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
    return min_coins[a][j], coins_used[a]
