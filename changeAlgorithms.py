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

def changeslow(coins, amount):
    print coins
    print amount

def