
# Problem

#* You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.
# Example:
#
# arr = [1, 4, 16, 64] r = 4
# There are [1, 4, 16] and [4, 16, 64] at indices (0, 1, 2) and (1, 2, 3). Return 2.
#
# Function Description:
# Complete the countTriplets function in the editor below.
# countTriplets has the following parameter(s):
# int arr[n]: an array of integers
# int r: the common ratio
# Returns:
# int: the number of triplets#

def countTriplets(arr, r):
    dic = {}
    #print(dic)
    dic_k = dic.keys()
    #print(dic_k)
    for e in arr:
        if e == 1:
            if e in dic_k:  # the number e already in the dic
                dic[e] += 1
            else:   # the number e is not in the dic
                dic[e] = 1
        if (e % r) == 0:
            if e in dic_k:  # the number e already in the dic
                dic[e] += 1
            else:   # the number e is not in the dic
                dic[e] = 1
    #print(dic)  # {1:1, 2:3, 4:2, 6:1}
    # Sorting the dictionary by key
    dic_item = dic.items()
    sorted_items = sorted(dic_item) # [(1, 1), (2, 3), (4, 2), (6, 1)]
    triplets = 0
    i = 0
    print(sorted_items)
    print(sorted_items[0][0])
    while i < len(sorted_items) - 2:
        if sorted_items[i+1][0] == (sorted_items[i][0]*r):
            if sorted_items[i+2][0] == (sorted_items[i+1][0]*r):
                triplets += (sorted_items[i][1]*sorted_items[i+1][1]*sorted_items[i+2][1])
        i+=1
    return print(triplets)

arr = [1, 2, 2, 2, 4, 4, 6]
r = 2
arr = [1, 5, 5, 25, 125]
r = 5
countTriplets(arr, r)