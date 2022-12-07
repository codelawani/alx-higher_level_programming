#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    new_dict = dict(sorted(a_dictionary.items(), key = lambda item: item[1]))
    last_key = list(new_dict.keys())[-1]
    return last_key
