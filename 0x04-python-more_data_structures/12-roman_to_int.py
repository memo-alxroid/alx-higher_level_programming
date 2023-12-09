#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    result = 0
    roman_dict = {"M": 1000, "C": 100, "D": 500, "L": 50,
                  "V": 5, "X": 10, "I": 1}
    roman_dict_subtractive = {"IV": 4, "IX": 9, "XL": 40,
                              "XC": 90, "CD": 400, "CM": 900}
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman_dict_subtractive:
            result += roman_dict_subtractive[roman_string[i:i + 2]]
            i += 2  # Increment by 2 since we've processed two characters
        else:
            result += roman_dict[roman_string[i]]
            i += 1  # Increment by 1 for single characters
    return result
