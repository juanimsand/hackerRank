
# Problem

#* It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
# Each person wears a sticker indicating their initial position in the queue from 1 to n.
# Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
# One person can bribe at most two others.
# Determine the minimum number of bribes that took place to get to a given queue order.
# Print the number of bribes, or, if anyone has bribed more than two people, print 'Too chaotic'.
# Example
# q = [1, 2, 3, 4, 5, 6, 7, 8]
# If person 5 bribes person 4, the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8.
# Only 1 bribe is required. Print 1.
#
# q = [4, 1, 2, 3]
# Person 4 had to bribe 3 people to get to the current position. Print 'Too chaotic'.
# Function Description:
# Complete the function minimumBribes in the editor below.
# 
# minimumBribes has the following parameter(s):
# int q[n]: the positions of the people after all bribes
# Returns:
# No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than 2 people.#

def minimumBribes(q):
    totalBribes = 0
    #indice = 0
    initArray = list(range(1,len(q)+1))
    while len(initArray) > 1:
        x = initArray.index(q[0])
        if x > 2:
            return print('Too chaotic')
        elif x > 0:
            totalBribes += x
            initArray.remove(q[0])
            q.remove(q[0])
        else:
            initArray.remove(q[0])
            q.remove(q[0])
    return print(totalBribes)

#q = list([3, 1, 5, 4, 2])
#minimumBribes(q)