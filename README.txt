CS 325 Project 1
================
To test the programs against as specified input filename: Ensure that all of the required files are in the same directory. 

**The required files are:**

1. changeAlgorithms.py 	(contains the three algorithms)*
2. main.py 				(runs max subarray algorithms on arrays in MSS_Problems.txt)* 
3. input_filename.text	(contains the arrays and targets)
  
From the command line, run the program by entering: 
	python main.py input_filename.txt

Once the program has completed execution, a file called input_filenamechange.txt will have been generated. This text file contains the results of each algorithm for each of the provided coin denominations and targets from input_filename.

Additionally, to generate minimum coins and timing data for the greedy and DP algorithms you can run the command: 
	python expStats.py 
This command will output minimum coins and timing data for Problems 4-6 of the project specification
based on hardcoded coin denominations for each problem and ranges of target amounts. 
The following file names correspond to the defined algorithms and questions:
Question 4:
* Q4Greedy.csv
* Q4DP.csv
Question 5:
* Q5Greedy_A1_V1.csv
* Q5Greedy_A1_V2.csv
* Q5DP_A1_V1.csv
* Q5DP_A1_V2.csv
* Q5Greedy_A2_V1.csv
* Q5Greedy_A2_V2.csv
* Q5DP_A2_V1.csv
* Q5DP_A2_V2.csv
Question 6:
* Q6Greedy.csv
* Q6DP.csv

To generate minimum coins and timing data for the slow, greedy and DP algorithms (over a smaller range of A) you can run the command:
	python expStats2.py
This command will output minimum coins and timing data for the coin denominations from Problems 4-6 of the project specification
based on smaller hard coded set of target Amounts. 
The following file names correspond to the defined algorithms and questions:
Question 4:
* Q4withslow.csv	
Question 5:
* Q5withSlow.csv	
Question 6:
* Q6withSlow.csv