#!/usr/bin/python3
def multiple_returns(sentence):
    """
    return a tuple with the length of a string and its first char
    .....
    parameter
    =========
    sentence: input sentence
    """
    len_str = len(sentence)
    if len_str == 0:
        sentence[0] = None
    return((len_str, sentence[0]))
