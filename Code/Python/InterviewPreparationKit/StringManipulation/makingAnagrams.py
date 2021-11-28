
# Problem

#* A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.
# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
# Example:
# a = cde
# b = dcf
# Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.
# Function Description:
# Complete the makeAnagram function in the editor below.
# makeAnagram has the following parameter(s):
# string a: a string
# string b: another string
# Returns:
# int: the minimum total characters that must be deleted#

def deletionsCounter(s1, s2):
    dic1={}
    dic2={}
    deletions = 0
    
    for c in s1:
        if c in dic1.keys():
            dic1[c] += 1
        else:
            dic1[c] = 1
    
    for c in s2:
        if c in dic2.keys():
            dic2[c] += 1
        else:
            dic2[c] = 1
    
    # At this point the 2 dics are ready.
    dic1pop = []
    for k in dic1.keys():
        if k in dic2.keys():
            if dic1[k] < dic2[k]:
                deletions += dic2[k] - dic1[k]
                dic2[k] = dic1[k]
            elif dic2[k] < dic1[k]:
                deletions += dic1[k] - dic2[k]
                dic1[k] = dic2[k]
        else:
            deletions += dic1[k]
            #create an array of keys that must be deleted from dic (pop inside a for loop is not good)
            # dic1.pop(k)
            dic1pop.append(k)

    for k in dic1pop:
        dic1.pop(k)
    
    dic2pop = []
    # at this moment dic2 has all the keys that dic1 has, but could has anothers, so i need to check
    for k in dic2.keys():
        if k not in dic1.keys():
            deletions += dic2[k]
            #dic2.pop(k)
            dic2pop.append(k)
    
    for k in dic2pop:
        dic2.pop(k)
    
    if len(dic1.keys()) != 0:
        return deletions
    else:
        return "The strings could not be anagrams only by deletion!!"
    
def main():
    qtydel = deletionsCounter(input1, input2)    
    print(qtydel)

input1='cde'
input2='dcf'
main()