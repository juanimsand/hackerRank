
# Problem

#* HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days.
# Example:
# expenditure = [10, 20, 30, 40, 50]
# d = 3
# On the first three days, they just collect spending data. At day 4, trailing expenditures are [10, 20, 30]. The median is 20 and the day's expenditure is 40. Because 40 > 2x20, there will be a notice.
# The next day, trailing expenditures are [20, 30, 40] and the expenditures are 50. This is less than 2x30 so no notice will be sent. Over the period, there was one notice sent.
# Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values.
# Function Description:
# Complete the function activityNotifications in the editor below.
# activityNotifications has the following parameter(s):
# int expenditure[n]: daily expenditures
# int d: the lookback days for median spending
# Returns:
# int: the number of notices sent#

def activityNotifications(expenditure, d):
    # Write your code here
    if d == len(expenditure):
        return print("Special case!")
    # Got an odd trailing days?
    odd = False if ((d % 2) == 0) else True
    # Initialization
    i = 0
    notification=0
    while (i+d) < len(expenditure):
        expenditureSorted = sorted(expenditure[i:i+d])
        print(expenditureSorted)
        if odd:
            median = expenditureSorted[(d//2)]
        else:
            median = ( expenditureSorted[(d//2)] + expenditureSorted[(d//2)-1] ) / 2
        if expenditure[i+d] >= (2*median):
            notification += 1
        i+=1
        #print(notification)
    return notification


# Sorting count algorithm!!

def sortingCount(arr):
    # Initialize count list
    countArr = [0 for i in range(max(arr)+1)]
    # Initialize sort output list
    sortArr = [0 for i in range(0, len(arr))]
    # Add count of elements from expediture to count list
    countingElements = 0
    for i in range (0, len(countArr)):
        countingElements += arr.count(i)
        countArr[i] = countingElements
    print("countArr: ", countArr)
    for j in arr:
        countArr[j]-=1
        sortArr[countArr[j]] = j
    print("sortArr: ", sortArr)
    return sortArr


def activityNotifications2(expenditure, d):
    # Write your code here
    if d == len(expenditure):
        return print("Special case!")
    # Got an odd trailing days?
    odd = False if ((d % 2) == 0) else True
    # Initialization
    i = 0
    notification=0
    while (i+d) < len(expenditure):
        #expenditureSorted = sorted(expenditure[i:i+d])
        expenditureSorted = sortingCount(expenditure[i:i+d])
        print(expenditureSorted)
        if odd:
            median = expenditureSorted[(d//2)]
        else:
            median = ( expenditureSorted[(d//2)] + expenditureSorted[(d//2)-1] ) / 2
        if expenditure[i+d] >= (2*median):
            notification += 1
        i+=1
        #print(notification)
    return notification

arr=[4, 2, 2, 8, 3, 3, 1]
#activityNotifications(arr, 5)      # Didn't pass some tests due timeout
activityNotifications2(arr, 5)      # This slution use sorting count algorithm which is explained above!
