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

def write_to_csv(file_name,x,y,time):
    with open(file_name, 'wb') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(x)
        statswriter.writerow(y)
        statswriter.writerow(time)
    print " >>>>> done! Results written to", file_name

def generate_statistics(Amt, coins, file_name, alg_name, algorithm):
    min_coins = []
    alg_time = []
    for a in Amt:
        #print "\n"+str(alg_name)
        total_time = 0   
        start = time.clock()
        tmp_min_coins, tmp_used_coins = algorithm(coins,a)
        min_coins.append(tmp_min_coins)
        elapsed = time.clock() - start
        total_time += elapsed
        alg_time.append(total_time/10.0)
    write_to_csv(file_name,Amt,min_coins, alg_time)

########## QUESTION 4 ##########
V=[1,5,10,25,50]
A = generate_list(2010,2200,5)
generate_statistics(A, V, 'Q4Greedy.csv', 'Greedy-Question4', changeAlgorithms.changegreedy)
generate_statistics(A, V, 'Q4DP.csv', 'DP-Question4', changeAlgorithms.changedp)

########## QUESTION 5 ##########
V1 = [1,2,6,12,24,48,60]
V2 = [1,6,13,37,150]
A1 = generate_list(2000,2200,1)
A2 = generate_list(10000,10100,1)

def print_result_for_comparison(coins,A,greedy,dp):
    for a in A:
        print "\n--Greedy--"
        greedy(coins,a)
        print "--DP--"
        dp(coins,a)
        
generate_statistics(A1, V1, 'Q5Greedy_A1_V1.csv', 'Greedy-Question5_A1_V1', changeAlgorithms.changegreedy)
generate_statistics(A1, V2, 'Q5Greedy_A1_V2.csv', 'Greedy-Question5_A1_V2', changeAlgorithms.changegreedy)
generate_statistics(A1, V1, 'Q5DP_A1_V1.csv', 'DP-Question5_A1_V1', changeAlgorithms.changedp)
generate_statistics(A1, V2, 'Q5DP_A1_V2.csv', 'DP-Question5_A1_V2', changeAlgorithms.changedp)

generate_statistics(A2, V1, 'Q5Greedy_A2_V1.csv', 'Greedy-Question5_A2_V1', changeAlgorithms.changegreedy)
generate_statistics(A2, V2, 'Q5Greedy_A2_V2.csv', 'Greedy-Question5_A2_V2', changeAlgorithms.changegreedy)
generate_statistics(A2, V1, 'Q5DP_A2_V1.csv', 'Greedy-Question5_A2_V1', changeAlgorithms.changedp)
generate_statistics(A2, V2, 'Q5DP_A2_V2.csv', 'Greedy-Question5_A2_V2', changeAlgorithms.changedp)

########## QUESTION 6 ##########
V3=[1] + generate_list(2,30,2)
#print V3
generate_statistics(A1, V3, 'Q6Greedy.csv', 'Greedy-Question6', changeAlgorithms.changegreedy)
generate_statistics(A1, V3, 'Q6DP.csv', 'DP-Question6', changeAlgorithms.changedp)


########## QUESTION 7 ##########


