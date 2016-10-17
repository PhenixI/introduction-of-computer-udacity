# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    num = ord(letter)
    num += 1
    if num <= ord('z'):
        return chr(num)
    else:
        return 'a'
