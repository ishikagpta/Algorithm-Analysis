import copy

# find1 finds the val in an unsorted list l using linear search
def find1(l, val):
    for i in range(len(l)):
        if(l[i] == val):
            return True
    return False


# find2 makes a deep copy of the parameter list and then sorts the list using the built in sort method
# which it then performs a binary search on to find val
def find2(l, val):
    dl = copy.deepcopy(l)
    dl.sort()
    start = 0
    end = len(dl) - 1

    while start <= end:
        mid = (start + end) // 2
        if dl[mid] < val:
            start = mid + 1
        elif dl[mid] > val:
            end = mid - 1
        else:
            return True
    return False

# find3 finds the val in an unsorted list l using list.in method
def find3(l, val):
    if val in l:
        return True
    else:
        return False

# find4 finds the val in an sorted list l using binary search
def find4(l, val):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] > val:
            end = mid - 1
        elif l[mid] < val:
            start = mid + 1
        else:
            return True
    return False