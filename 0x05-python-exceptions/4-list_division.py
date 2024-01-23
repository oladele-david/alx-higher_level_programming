#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            result = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)

    return (result_list)
