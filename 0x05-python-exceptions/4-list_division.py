#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotients_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            quotients_list.append(quotient)
    return quotients_list
