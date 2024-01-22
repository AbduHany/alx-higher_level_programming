def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            a += 1
        return x
    except IndexError:
        return a
    finally:
        print()
