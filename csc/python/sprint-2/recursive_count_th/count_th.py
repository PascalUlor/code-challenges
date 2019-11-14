'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    if word == "":
        return 0

    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
    # pass


print(count_th('thousandth'))

"""
1. check if word exist
    a. if it exist create a list from the word input
    b. if it doesn't exist end program
2. compare letters in word two at a time to see if it satifies condition
3. if step two returns True add + 1 else count + 0
4. remove one letter at a time from word
5. repeate step 1 to 4
"""
