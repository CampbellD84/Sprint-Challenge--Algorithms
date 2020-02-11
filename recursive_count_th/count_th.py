'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    search_param = "th"
    param_len = len(search_param)
    word_len = len(word)

    if word_len == 0 or word_len < param_len:
        return 0

    if word[:param_len] == search_param:
        return count_th(word[param_len - 1:]) + 1

    return count_th(word[param_len - 1:])
