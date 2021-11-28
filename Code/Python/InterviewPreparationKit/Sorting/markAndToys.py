
# Problem

#* Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
# Note Each toy can be purchased only once.
# Example:
# prices = [1, 2, 3, 4]
# k = 7
# The budget is 7 units of currency. He can buy items that cost [1, 2, 3] for 6, or [3, 4] for  units. The maximum is 3 items.
# Function Description:
# Complete the function maximumToys in the editor below.
# maximumToys has the following parameter(s):
# int prices[n]: the toy prices
# int k: Mark's budget
# Returns:
# int: the maximum number of toys#

def maximumToys(prices, k):
    # Write your code here
    # Amount spended
    amountSpended = 0
    # Toys bought
    toys = 0
    # Sorting the list
    prices.sort()
    for p in prices:
        if (p+amountSpended) < k:
            toys+=1
            amountSpended+=p
        else:
            return toys
    return toys

prices= [1,2,3,4]
maximumToys(prices, len(prices))