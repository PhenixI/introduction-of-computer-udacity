# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in 
# the correct bucket), with the correct 
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable,key,value):
    # your code here
    hashedTable = hashtable_get_bucket(htable,key)
    hashedTable.append([key,value])   
    return htable  
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
