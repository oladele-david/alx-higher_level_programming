#!/usr/bin/python3
def multiple_returns(sentence):
    my_turple = ()
    if sentence is None:
        return None
    else:
        my_turple = len(sentence), sentence[0]
    return my_turple
