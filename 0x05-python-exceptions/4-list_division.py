#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            res = a / b
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except (ZeroDivisionError):
            print("division by 0")
            res = 0
        except (IndexError):
            print("out of range")
            res = 0
        finally:
            result.append(res)
    return result
