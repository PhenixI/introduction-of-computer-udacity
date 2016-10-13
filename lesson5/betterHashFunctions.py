# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    sum = 0
    for e in keyword:
        sum += ord(e)

    return sum % buckets
