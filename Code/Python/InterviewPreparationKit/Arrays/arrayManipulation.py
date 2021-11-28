
# Problem

#* Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in the array.
# 
# Example:
# n = 10
# queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
#
# Queries are interpreted as follows:
# a b k
# 1 5 3
# 4 8 7
# 6 9 1
# 
# Add the values of k between the indices a and b inclusive:
# 
# index->	 1 2 3  4  5 6 7 8 9 10
#           [0,0,0, 0, 0,0,0,0,0, 0]
#           [3,3,3, 3, 3,0,0,0,0, 0]
#           [3,3,3,10,10,7,7,7,0, 0]
#           [3,3,3,10,10,8,8,8,1, 0]
# 
# The largest value is 10 after all operations are performed.
# 
# Function Description:
# Complete the function arrayManipulation in the editor below.
# arrayManipulation has the following parameters:
# int n - the number of elements in the array
# int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
# Returns:
# int - the maximum value in the resultant array#

# Example input:
#   6 3
#   2 5 2
#   1 4 5
#   3 6 3

# [0, 0, 0, 0, 0, 0]
# [0, 2, 2, 2, 2, 0]
# [5, 7, 7, 7, 2, 0]
# [5, 7, 10, 10, 5, 3]


# This solution is working fine but it´s not the best one since we need to searched in the whole array for determine
# the max value.
def arrayManipulation(n, query):
    initList = [0]*n
    for q in query:
        #print(q)
        for i in range(q[0]-1, q[1]):
            initList[i] += q[2]
    return max(initList)

n = 6
query = [[2, 5, 2], [1, 4, 5], [3, 6, 3]]
arrayManipulation(n, query)
