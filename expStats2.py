#!/usr/bin/env python
#title          :expStats.py
#description    :Script to capture runtime averages for change algorithms
#author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
#creation date  :22 October 2015
#last modified  :22 October 2015
#usage          :python expStats.py
#notes          :
#python_version :2.6.6
#==============================================================================

import changeAlgorithms
import time
import csv

#----------------------------------------------------------------
# UTILITY FUNCTIONS
#----------------------------------------------------------------


def generate_list(start, end, interval):
    """ returns a list of integers separated by interval from start to end inclusive"""
    arr = []
    v = start
    while v != (end+interval):
        arr.append(v)
        v += interval
    print " \n>>>>> Generating list"
    print arr
    return arr


def write_to_csv(file_name, x, y, time, alg_name, bool_append=0):
    amounts = "Amounts, "
    title = alg_name + ", "
    if bool_append:
        write_mode = 'ab'
    else:
        write_mode = 'wb'
    with open(file_name, write_mode) as csvfile:
        statswriter = csv.writer(csvfile)
        csvfile.write(amounts)
        statswriter.writerow(x)
        csvfile.write(title)
        statswriter.writerow(y)
        csvfile.write(title)
        statswriter.writerow(time)
    print " >>>>> done! ", alg_name, " Results written to ", file_name


def generate_statistics(Amt, coins, file_name, alg_name, algorithm, bool_slow=0, bool_append=0):
    min_coins = []
    alg_time = []
    for a in Amt:
        total_time = 0
        start = time.clock()
        if bool_slow:
            solution = algorithm(coins, a, [])
            min_coins.append(len(min(solution, key=len)))
        else:
            tmp_min_coins, tmp_used_coins = algorithm(coins,a)
            min_coins.append(tmp_min_coins)
        elapsed = time.clock() - start
        total_time += elapsed
        alg_time.append(total_time/10.0)
    write_to_csv(file_name, Amt, min_coins, alg_time, alg_name, bool_append)

########## QUESTION 4 ##########
V=[1, 5, 10, 25, 50]
A = generate_list(5, 250, 5)
generate_statistics(A, V, 'Q4withslow.csv', 'Greedy-Question4', changeAlgorithms.changegreedy)
generate_statistics(A, V, 'Q4withslow.csv', 'DP-Question4', changeAlgorithms.changedp, 0, 1)
generate_statistics(A, V, 'Q4withslow.csv', 'Slow-Question4', changeAlgorithms.changeslow, 1, 1)

########## QUESTION 5 ##########
V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]
A1 = generate_list(2, 70, 2)


def print_result_for_comparison(coins, A, greedy, dp):
    for a in A:
        print "\n--Greedy--"
        greedy(coins, a)
        print "--DP--"
        dp(coins, a)

generate_statistics(A1, V1, 'Q5withSlow.csv', 'greedy-V1', changeAlgorithms.changegreedy)
generate_statistics(A1, V1, 'Q5withSlow.csv', 'dp-v1', changeAlgorithms.changedp, 0, 1)
generate_statistics(A1, V1, 'Q5withSlow.csv', 'slow-v1', changeAlgorithms.changeslow, 1, 1)

generate_statistics(A1, V2, 'Q5withSlow.csv', 'greedy-v2', changeAlgorithms.changegreedy, 0, 1)
generate_statistics(A1, V2, 'Q5withSlow.csv', 'dp-v2', changeAlgorithms.changedp, 0, 1)
generate_statistics(A1, V2, 'Q5withSlow.csv', 'slow-v2', changeAlgorithms.changeslow, 1, 1)


########## QUESTION 6 ##########
A3 = generate_list(2, 70, 2)
V3 = [1] + generate_list(2, 30, 2)
# print V3
generate_statistics(A3, V3, 'Q6withSlow.csv', 'Greedy-Question6', changeAlgorithms.changegreedy)
generate_statistics(A3, V3, 'Q6withSlow.csv', 'DP-Question6', changeAlgorithms.changedp, 0, 1)
generate_statistics(A3, V3, 'Q6withSlow.csv', 'Slow-Question6', changeAlgorithms.changeslow, 1, 1)

