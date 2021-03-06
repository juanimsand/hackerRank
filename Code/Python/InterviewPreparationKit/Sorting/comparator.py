
# Problem

#* Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:
# name: a string.
# score: an integer.
# Given an array of n Player objects, write a comparator that sorts them in order of decreasing score. If 2 or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.
# In short, when sorting in ascending order, a comparator function returns -1 if a < b, 0 if a=b, and 1 if a > b.
# Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.
# 
# Output Format:
# You are not responsible for printing any output to stdout.
# Locked stub code in Solution will instantiate a Checker object, use it to sort the Player array, and print each sorted element.#

class Checker:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self) -> str:
        pass
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.name > b.name:
            return 1
        else:
            return -1