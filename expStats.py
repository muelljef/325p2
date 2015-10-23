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

def write_to_csv(file_name,x,y):
    with open(file_name, 'wb') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(x)
        statswriter.writerow(y)
    print " >>>>> done! Results written to", file_name

def generate_statistics(A, coins, file_name, alg_name, algorithm):
    min_coins = []
    for amt in A:
        print "\n"+str(alg_name)
        min_coins.append(algorithm(V,amt))
    write_to_csv(file_name,A,min_coins)

########## QUESTION 4 ##########
V=[1,5,10,25,50]
A = generate_list(2010,2200,5)
generate_statistics(A, V, 'Q4Greedy.csv', 'Greedy-Question4', changeAlgorithms.changegreedy)
generate_statistics(A, V, 'Q4DP.csv', 'DP-Question4', changeAlgorithms.changedp)

########## QUESTION 45 ##########
V1 = [1,2,6,12,24,48,60]
V2 = [1,6,13,37,150]
A1 = generate_list(2000,2200,1)
A2 = generate_list(10000,10100,1)
generate_statistics(A1, V1, 'Q5Greedy_A1_V1.csv', 'Greedy-Question5V1', changeAlgorithms.changegreedy)
generate_statistics(A1, V2, 'Q5Greedy_A1_V2.csv', 'Greedy-Question5V2', changeAlgorithms.changegreedy)
generate_statistics(A1, V1, 'Q5DP_A1_V1.csv', 'DP-Question5V1', changeAlgorithms.changedp)
generate_statistics(A1, V2, 'Q5DPA1_V2.csv', 'DP-Question5V2', changeAlgorithms.changedp)

#if above runs too slowly
#generate_statistics(A2, V1, 'Q5Greedy_A2_V1.csv', 'Greedy-Question5', changeAlgorithms.changegreedy)
#generate_statistics(A2, V2, 'Q5DP_A2_V2.csv', 'DP-Question5', changeAlgorithms.changedp)
#generate_statistics(A2, V1, 'Q5Greedy_A2_V1.csv', 'Greedy-Question5', changeAlgorithms.changegreedy)
#generate_statistics(A2, V2, 'Q5DP_A2_V2.csv', 'DP-Question5', changeAlgorithms.changedp)

########## QUESTION 6 ##########
V3=[1] + generate_list(2,30,2)
#print V3
generate_statistics(A1, V3, 'Q6Greedy.csv', 'Greedy-Question6', changeAlgorithms.changegreedy)
generate_statistics(A1, V3, 'Q6DP.csv', 'DP-Question6', changeAlgorithms.changedp)

