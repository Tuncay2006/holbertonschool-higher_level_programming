#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = None
    max_value = float('-inf')  # En küçük sayı ile başlatılır
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            max_key = key
    return max_key
