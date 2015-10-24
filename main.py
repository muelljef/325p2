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

import changeAlgorithms
import sys
import os.path

if len(sys.argv) != 2:
    print "--ERROR: Incorrect number of arguments--"
    print "  Program expects: main.py file_name.txt"
    print "  Please try again."
elif os.path.isfile(sys.argv[1]) is False:
    print "--ERROR: " + str(sys.argv[1]) + " is not a valid file--"
    print "  Program expects: main.py file_name.txt"
    print "  Please try again."
else:
    file_name = sys.argv[1]
    testCaseNum = 1
    arrays = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("\n", "")
            mss = line.split(",")
            mss = [int(i) for i in mss]
            arrays.append(mss)
            testCaseNum += 1
    f.close()

    for i in range(0, len(arrays)):
        print arrays[i]
    print "\n"

    test_case_num = 1
    for i in range(0, len(arrays), 2):
        print "Test case %s" % test_case_num

        print "brute force - recursive"
        solution = [sol for sol in changeAlgorithms.changeslow(arrays[i], arrays[i+1][0], [])]
        print min(solution, key=len)
        print len(min(solution, key=len))

        print "dynamic"
        coins = arrays[i]
        amount = arrays[i+1][0]
        print changeAlgorithms.changedp(coins, amount)

        print "greedy"
        print changeAlgorithms.changegreedy(arrays[i], arrays[i+1][0])

        print "\n"
        test_case_num += 1

