# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(repeat):
    maxc = None
    maxlen = 0
    pre = None
    repeatNum = 0
    for element in repeat:
        if pre == element:
            repeatNum += 1
        else:
            pre = element
            repeatNum = 1

        if repeatNum > maxlen:
            maxlen = repeatNum
            maxc = pre
    return maxc







#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2])

print longest_repetition([2,2,3,3,3])

