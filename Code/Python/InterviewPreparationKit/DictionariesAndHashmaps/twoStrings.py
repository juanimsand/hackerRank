
# Problem

#* Given two strings, determine if they share a common substring. A substring may be as small as one character.
# Example:
# s1 = 'and'
# s2 = 'art'
# These share the common substring a.
# s1 = 'be'
# s2 = 'cat'
# These do not share a substring.
# 
# Function Description:
# Complete the function twoStrings in the editor below.
# twoStrings has the following parameter(s):
# string s1: a string
# string s2: another string
# Returns:
# string: either YES or NO#

def twoStrings(s1, s2):
    # Write your code here
    print("s1", s1)
    print("s2", s2)
    for letter in s1:
        print(letter)
        if s2.find(letter) == -1:
            #print("didnt find it!")
            continue
        else:
            return "YES"
    return "NO"

