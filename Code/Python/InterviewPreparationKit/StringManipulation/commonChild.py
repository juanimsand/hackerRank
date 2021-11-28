
# Problem

#* A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
# Example:
# s1 = ABCD
# s2 = ABDC
# These strings have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Return 3.
# Function Description:
# Complete the commonChild function in the editor below.
# commonChild has the following parameter(s):
# string s1: a string
# string s2: another string
# Returns:
# int: the length of the longest string which is a common child of the input strings#

def commonChild(s1, s2):
    # Extracting length from s1
    l = len(s1)
    # Need 1 index per string
    i = 0
    j = 0
    biggerChild = 0
    s1LastIndexEqual=0
    master=1    # This represent with string is being recorrido (s1:1, s2:2)
    # While i or j are minor than strings s1 and s2 length (that is the same) keep working
    while((i < l) and (j < l)):
        if s1[i] == s2[j]:
            i+=1
            j+=1
            biggerChild+=1
            s1LastIndexEqual=i
        else:
            if master == 1:
                if (i+1) == l: # Then we should switch to s2
                    i=s1LastIndexEqual
                    j+=1
                    master=2
                else:
                    i+=1
            else:
                if (j+1) == l:
                    return biggerChild
                else:
                    j+=1
        print('Keep working....')
        print('i: ', i)
        print('j: ', j)
    return print('biggerChild', biggerChild)


def commonChild2(s1,s2):
    l = len(s1)
    biggerChild=0
    # Recorro el segundo string parado en un indice del primero
    # Cuando encuentro una letra coincidente, aumento el indice del primero
    s1Index=0
    s2Index=0
    while(s1Index < l):
        for s2char in s2[s2Index:]:
            if s1[s1Index] == s2char:
                biggerChild+=1
                s2Index+=1
                if s2[l-1] == s2char:
                    return print(biggerChild)
                break
        s1Index+=1
    
    
    return print(biggerChild)


string1='abcdefgh'
string2='abdkqope'
commonChild(string1, string2)
#commonChild2(string1, string2)