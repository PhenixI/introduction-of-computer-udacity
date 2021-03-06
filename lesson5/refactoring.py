# 6. In video 28. Update, it was suggested that some of the duplicate code in
# lookup and update could be avoided by a better design.  We can do this by
# defining a procedure that finds the entry corresponding to a given key, and
# using that in both lookup and update.

# Here are the original procedures:

def hashtable_com(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return bucket,entry
    return bucket,[]
    
def hashtable_update(htable, key, value):
    bucket,entry = hashtable_com(htable,key)
    if entry == []:
        bucket.append([key,value])
    else:
        entry[1] = value

def hashtable_lookup(htable, key):
    bucket,entry = hashtable_com(htable,key)
    if entry == []:
        return None
    else:
        return entry[1]

def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

# Whenever we have duplicate code like the loop that finds the entry in
# hashtable_update and hashtable_lookup, we should think if there is a better way
# to write this that would avoid the duplication. We should be able to rewrite
# these procedures to be shorter by defining a new procedure and rewriting both
# hashtable_update and hashtable_lookup to use that procedure.

# Modify the code for both hashtable_update and hashtable_lookup to have the same
# behavior they have now, but using fewer lines of code in each procedure.  You
# should define a new procedure to help with this. Your new version should have
# approximately the same running time as the original version, but neither
# hashtable_update or hashtable_lookup should include any for or while loop, and
# the block of each procedure should be no more than 6 lines long.
