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

    output_filename = str(file_name)
    output_filename = output_filename.replace(".txt", "change.txt")
    with open(output_filename, "w") as of:
        test_case_num = 1
        for i in range(0, len(arrays), 2):
            of.write("Test case " + str(test_case_num) + "\n")

            of.write("brute force - recursive \n")
            solution = [sol for sol in changeAlgorithms.changeslow(arrays[i], arrays[i+1][0], [])]
            coins_array_pos = (test_case_num - 1) * 2
            soln_usedcoins = [0] * len(arrays[coins_array_pos])
            for coin_value in min(solution, key=len):
                for index, value in enumerate(arrays[coins_array_pos]):
                    if (coin_value == value):
                        soln_usedcoins[index] += 1

            of.write(str(soln_usedcoins) + "\n")
            of.write(str(len(min(solution, key=len))) + "\n")

            of.write("dynamic \n")
            coins = arrays[i]
            amount = arrays[i+1][0]
            soln_mincoin, soln_usedcoins = changeAlgorithms.changedp(coins, amount)
            of.write(str(soln_usedcoins) + "\n")
            of.write(str(soln_mincoin) + "\n")

            of.write("greedy \n")
            soln_mincoin, soln_usedcoins = changeAlgorithms.changegreedy(coins, amount)
            of.write(str(soln_usedcoins) + "\n")
            of.write(str(soln_mincoin) + "\n")

            of.write("\n")
            test_case_num += 1
