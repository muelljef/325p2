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

def write_to_csv(file_name, x, y, time, alg_name):
    title = alg_name + ", "
    with open(file_name, 'wb') as csvfile:
        statswriter = csv.writer(csvfile)
        csvfile.write(title)
        statswriter.writerow(x)
        csvfile.write(title)
        statswriter.writerow(y)
        csvfile.write(title)
        statswriter.writerow(time)
    print " >>>>> done! Results written to", file_name


def append_to_csv(file_name, x, y, time, alg_name):
    title = alg_name + ", "
    with open(file_name, 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        csvfile.write(title)
        statswriter.writerow(x)
        csvfile.write(title)
        statswriter.writerow(y)
        csvfile.write(title)
        statswriter.writerow(time)
    print " >>>>> done! Results written to", file_name

def generate_statistics(Amt, coins, file_name, alg_name, algorithm, bool_slow=0, bool_append=0):
    min_coins = []
    alg_time = []
    for a in Amt:
        #print "\n"+str(alg_name)
        total_time = 0
        start = time.clock()
        if bool_slow:
            solution = algorithm(coins, a, [])
            min_coins.append(len(min(solution, key=len)))
        else:
            min_coins.append(algorithm(coins,a))
        elapsed = time.clock() - start
        total_time += elapsed
        alg_time.append(total_time/10.0)
    if bool_append:
        append_to_csv(file_name, Amt, min_coins, alg_time, alg_name)
    else:
        write_to_csv(file_name, Amt, min_coins, alg_time, alg_name)

"""
########## QUESTION 4 ##########
V=[1,5,10,25,50]
A = generate_list(5, 250, 5)
generate_statistics(A, V, '2 - Q4Greedy.csv', 'Greedy-Question4', changeAlgorithms.changegreedy)
generate_statistics(A, V, '2 - Q4DP.csv', 'DP-Question4', changeAlgorithms.changedp)
generate_statistics(A, V, '2 - Q4Slow.csv', 'Slow-Question4', changeAlgorithms.changeslow, 1)
"""

########## QUESTION 5 ##########
V1 = [1,2,6,12,24,48,60]
V2 = [1,6,13,37,150]
A1 = generate_list(2,100,2)

def print_result_for_comparison(coins,A,greedy,dp):
    for a in A:
        print "\n--Greedy--"
        greedy(coins,a)
        print "--DP--"
        dp(coins,a)

generate_statistics(A1, V1, '2 - Q5.csv', 'Q5 - greedy - V1', changeAlgorithms.changegreedy)
generate_statistics(A1, V2, '2 - Q5.csv', 'Q5 - greedy - v2', changeAlgorithms.changegreedy, 0, 1)
generate_statistics(A1, V1, '2 - Q5.csv', 'Q5 - dp - v1', changeAlgorithms.changedp, 0, 1)
generate_statistics(A1, V2, '2 - Q5.csv', 'Q5 - dp - v2', changeAlgorithms.changedp, 0, 1)
generate_statistics(A1, V1, '2 - Q5.csv', 'Q5 - slow - v1', changeAlgorithms.changeslow, 1, 1)
generate_statistics(A1, V2, '2 - Q5.csv', 'Q5 - slow - v2', changeAlgorithms.changeslow, 1, 1)

"""
########## QUESTION 6 ##########
V3=[1] + generate_list(2,30,2)
#print V3
generate_statistics(A1, V3, 'Q6Greedy.csv', 'Greedy-Question6', changeAlgorithms.changegreedy)
generate_statistics(A1, V3, 'Q6DP.csv', 'DP-Question6', changeAlgorithms.changedp)


########## QUESTION 7 ##########
"""
