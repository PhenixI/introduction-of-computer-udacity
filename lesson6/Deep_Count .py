# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

# It is not necessary to understand how is_list works. It returns True if the
# input is a List, and returns False otherwise.

def deep_count(p):
	num = 0;
	if not is_list(p):
		return 0
	else:
		num += len(p)
		for p0 in p:
			num += deep_count(p0)
		return num

def deep_count(p):
	sum = 0
	for e in p:
		sum = sum + 1
		if is_list(e):
			sum = sum+deep_count(e)
	return sum
