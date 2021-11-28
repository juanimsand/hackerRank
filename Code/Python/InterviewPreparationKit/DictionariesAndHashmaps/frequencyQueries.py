
# Problem

#* You are given q queries. Each query is of the form two integers described below:
# - 1x: Insert x in your data structure.
# - 2y: Delete one occurence of y from your data structure, if present.
# - 3z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.
# Example:
# 
# queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
# 
# The results of each operation are:
# 
# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# 
# Return an array with the output: [0, 1].
# Function Description:
# Complete the freqQuery function in the editor below.
# freqQuery has the following parameter(s):
# int queries[q][2]: a 2-d array of integers
# Returns:
# - int[]: the results of queries of type 3#