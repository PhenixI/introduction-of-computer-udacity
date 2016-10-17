def shift_n_letters(letter, n):
    while n<0:
        n += 26
    num = ord(letter) + n
    if num < ord('z'):
        return chr(num)
    else:
        remind= num - ord('z')-1
        return chr(ord('a')+remind)
