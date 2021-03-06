def shift_n_letters(letter, n):
    while n<0:
        n += 26
    num = ord(letter) + n
    if num <= ord('z'):
        return chr(num)
    else:
        remind= num - ord('z')-1
        return chr(ord('a')+remind)


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string,n):
    resultstr=''
    # Your code here
    for l in string:
        if l>='a' and l<='z':
            r = shift_n_letters(l,n)
            resultstr += r
        else:
            resultstr += l
    return resultstr
    
