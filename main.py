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


testCaseNum = 1
arrays = []
with open("Coin1.txt", "r") as f:
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
    print "dynamic"
    changeAlgorithms.changedp(arrays[i], arrays[i+1][0])
    print "greedy"
    changeAlgorithms.changegreedy(arrays[i], arrays[i+1][0])
    print "\n"
    test_case_num += 1

# def algorithmDisplayResults(algorithm, temp_array, recursive=0):
#             if recursive:
#                 i, j, max_sub_sum = algorithm(temp_array, 0, len(temp_array) - 1)
#             else:
#                 i, j, max_sub_sum = algorithm(temp_array)
#             return max_sub_sum, temp_array[i:j+1]
#
# print '\n'
# testCaseNum = 1
# with open("MSS_Results.txt", "w") as f:
#     for mss in arrays:
#         f.write("Test Case: " + str(testCaseNum) + "\n")
#         f.write( str(mss) + "\n" )
#         f.write("--------------------------------\n")
#         max_sum, max_subarray = algorithmDisplayResults(maxSumSubarray.enumeration, mss)
#         f.write("Algorithm 1 (sum, subarray): " + str(max_sum) + "   " + str(max_subarray) + "\n")
#         max_sum, max_subarray = algorithmDisplayResults(maxSumSubarray.better_enumeration, mss)
#         f.write("Algorithm 2 (sum, subarray): " + str(max_sum) + "   " + str(max_subarray) + "\n")
#         max_sum, max_subarray = algorithmDisplayResults(maxSumSubarray.max_subarray_recursive, mss, 1)
#         f.write("Algorithm 3 (sum, subarray): " + str(max_sum) + "   " + str(max_subarray) + "\n")
#         max_sum, max_subarray = algorithmDisplayResults(maxSumSubarray.linear_time, mss)
#         f.write("Algorithm 4 (sum, subarray): " + str(max_sum) + "   " + str(max_subarray) + "\n\n\n")
#         testCaseNum += 1
# f.close()
