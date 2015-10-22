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
    with open(file_name, 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(x)
        statswriter.writerow(y)
    print " >>>>> done! Results written to", file_name

V=[1,5,10,25,50]
A = generate_list(2010,2200,5)

min_coins = []
for amt in A:
    #print "\n--Slow--"
    #solution = [sol for sol in changeAlgorithms.changeslow(V,amt,[])]
    #print min(solution, key=len)
    #print len(min(solution, key=len))
    print "\n--Greedy--"
    min_coins.append(changeAlgorithms.changegreedy(V,amt))

write_to_csv('stats1',A,min_coins)

# for amt in A:
#     print "--DP--"
#     changeAlgorithms.changedp(V,amt)
#     write_to_csv('stats2',amt,)
#
# V1 = [1,2,6,12,24,48,60]
# A = generate_list(2000,2200,1)
#
# for amt in A:
#     print "\n--Greedy--"
#     changeAlgorithms.changegreedy(V1,amt)
#     write_to_csv('stats3',amt,)
#
# for amt in A:
#     print "--DP--"
#     changeAlgorithms.changedp(V1,amt)
#     write_to_csv('stats4',amt)
#
# V2 = [1,6,13,37,150]
#

