from curses.ascii import isdigit


def compute_sum_of_list(lst):
    sum = 0
    for each in lst:
        if each.isnumeric():
            sum += each
    return sum
