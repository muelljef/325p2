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

def changeslow(coins, amount):
    print coins
    print amount
