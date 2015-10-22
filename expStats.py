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
def generate_array(start, end, interval):
    arr = []
    v = start
    while v != (end + interval):
        arr.append(v)
        v += interval
    print arr
    return arr

V = generate_array(2010,2200,5)
V1 = [1,2,6,12,24,48,60]
V2


