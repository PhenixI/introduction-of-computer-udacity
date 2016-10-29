# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]


def add_to_index(index,keyword,url):
    index_len = len(index)
    i = 0
    while i<index_len:
        if index[i][0]== keyword:
            index[i][1].append(url)
            return
        i+=1
    index.append([keyword,[url]])
