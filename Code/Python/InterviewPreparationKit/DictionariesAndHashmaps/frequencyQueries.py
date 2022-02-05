
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

def freqQueries(queries):
    dic={}
    arrayReturned=[]
    found=False
    for operation, value in queries:
        if operation == 1:  # check if value exists on dic and add 1
            if dic.get(value) != None:
                dic[value]+=1
            else:
                dic[value]=1
        elif operation == 2:
            if dic.get(value):
                dic[value]-=1
        else:   # operation == 3
            for i in dic.values():
                if i == value:
                    arrayReturned.append(1)
                    found = True
                    break
            if not found:
                arrayReturned.append(0)
            found=False
        #print(operation, value)
    print(arrayReturned)
    return arrayReturned

def freqQuery2(queries):
    dic1={}
    dic2={}
    arrayReturned=[]
    found=False
    for operation, value in queries:
        if operation == 1:  # check if value exists on dic and add 1
            if dic1.get(value) != None:
                dic1[value]+=1
            else:
                dic1[value]=1
            # Now add 1 to dic2[dic1[value]]
            if dic2.get(dic1[value]) != None:
                dic2[dic1[value]]+=1
            else:
                dic2[dic1[value]]=1
            # And remove 1 from dic2[dic1[value]-1]
            if dic2.get(dic1[value]-1) != None:
                dic2[dic1[value]-1]-=1
        elif operation == 2:
            if dic1.get(value):
                if dic1[value] > 0:
                    dic1[value]-=1
                    # Now remove 1 from dic2[dic1[value]+1]
                    if dic2.get(dic1[value]+1) != None:
                        dic2[dic1[value]+1]-=1
                    # And add 1 to dic2[dic1[value]]
                    if dic2.get(dic1[value]) != None:
                        dic2[dic1[value]]+=1
                    else:
                        dic2[dic1[value]]=1
        else:   # operation == 3
            for i in dic2.keys():
                if (i == value) and (dic2[i] > 0):
                    arrayReturned.append(1)
                    found = True
                    break
            if not found:
                arrayReturned.append(0)
            found=False
        #print(operation, value)
    #print(arrayReturned)
    return arrayReturned

queries=[(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
queries2=[(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2),]
freqQueries2(queries2)