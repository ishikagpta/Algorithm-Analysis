import bigo
import timeit
import random

# tests functions from bigo.py to show time complexity
def __main__():

    # stores the value to be passed to create range for various find methods
    list_vals = []
    # lists store run time for various input sizes for the functions in bigo.py
    list_1, list_2, list_3, list_4 = [], [], [], []

    # creates values ranging from 100000 to 200001 with an interval of 10000
    for n in range(100000, 200001, 10000):
        list_vals.append(n)
        l = []
        for i in range(n):
            data = i
            l.append(data)

        # random.shuffle makes the list l an unsorted list
        random.shuffle(l)
        # generates a sorted list
        s_arr = list(range(0, n))

        val = random.randint(1, n + 1)

        t = timeit.Timer(lambda: bigo.find1(l, val))
        time = t.timeit(100)
        list_1.append(time)
        print(f' BigO.find1 took {time} ms, for a list of {n} values')

        t = timeit.Timer(lambda: bigo.find2(l, val))
        time = t.timeit(100)
        list_2.append(time)
        print(f' BigO.find2 took {time} ms, for a list of {n} values')

        t = timeit.Timer(lambda: bigo.find3(l, val))
        time = t.timeit(100)
        list_3.append(time)
        print(f' BigO.find3 took {time} ms, for a list of {n} values')

        t = timeit.Timer(lambda: bigo.find4(s_arr, val))
        time = t.timeit(100)
        list_4.append(time)
        print(f' BigO.find4 took {time} ms, for a list of {n} values')

    # printing the run time for each func from bigo.py for various input sizes
    for i in range(len(list_1)):
        print(list_vals[i], end=":   ")
        print(list_1[i], end=":")
        print(list_2[i], end=":")
        print(list_3[i], end=":")
        print(list_4[i])