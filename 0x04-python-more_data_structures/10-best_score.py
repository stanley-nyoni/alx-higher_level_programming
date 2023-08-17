#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        high_score_key = max(a_dictionary, key=a_dictionary.get)
        return high_score_key
    else:
        return None
