'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # reached end of string (base case)
    if len(word) == 0:
        return 0
    # if found 'th' return 1 + another call (base case)
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    # return recursive call
    else:
        return count_th(word[1:])

