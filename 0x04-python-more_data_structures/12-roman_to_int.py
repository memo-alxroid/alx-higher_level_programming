#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    result = 0
    roman_dict = {"M": 1000, "C": 100, "D": 500, "L": 50,
                  "V": 5, "X": 10,"I": 1}
    roman_dict_subtractive = {"IV": 4, "IX": 9, "XL":40,
                              "XC": 90, "CD": 400, "CM": 900}
    
    for i in range(0, len(roman_string),2):
        if i < len(roman_string) - 1:
            two_chars = roman_string[i] + roman_string[i + 1]
            if roman_dict_subtractive.__contains__(two_chars):
                result += roman_dict_subtractive[two_chars]
            elif roman_dict.__contains__(two_chars[0]):
                result += roman_dict[two_chars[0]]
            elif roman_dict.__contains__(two_chars[1]):
                result += roman_dict[two_chars[1]]
            else:
                result += 0
        else:
            result += roman_dict[roman_string[i]]
    return result
