
# Problem

#* A left rotation operation on an array shifts each of the array's elements  unit to the left.
# For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
# Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
# Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
#
# Function Description:
# Complete the function rotLeft in the editor below.
# rotLeft has the following parameter(s):
#
# int a[n]: the array to rotate
# int d: the number of rotations
#
# Returns:
# int a'[n]: the rotated array#

# Complete the rotLeft function below.
def rotLeft(a, d):
    sortedArray = a[d:len(a)] + a[0:d]
    print(sortedArray)
    sortedArrayToStr = []
    for i in sortedArray:
        sortedArrayToStr.append(str(i))
    print(sortedArrayToStr)
    return sortedArrayToStr