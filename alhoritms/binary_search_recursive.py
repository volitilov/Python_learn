def binary_search_recursive(a_list, item):
    """Performs recursive binary search of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return '{item} was not found in the list'.format(item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return '{item} found'.format(item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)



def r_b_s(mas, item, start, stop):
    if start > stop: return False
    else:
        mid = (start + stop) // 2
        if item == mas[mid]: return mid
        elif item < mas[mid]:
            return r_b_s(mas, item, start, mid -1)
        else:
            return r_b_s(mas, item, mid + 1, stop)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::
mas = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
start = 0
stop = len(mas) - 1
item = 81

x = r_b_s(mas, item, start, stop)

if x == False:
    print('Item', item, '- Not Found!')
else:
    print('Item', item, '- Found at index', x)