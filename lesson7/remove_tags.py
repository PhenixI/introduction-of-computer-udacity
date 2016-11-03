# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(list_str):
    start = list_str.find('<')
    while start != -1:
        end = list_str.find('>',start)
        list_str = list_str[0:start] + " "+list_str[end+1:]
        start = list_str.find('<')
    return list_str.split()
