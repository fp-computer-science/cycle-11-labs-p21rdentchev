# Ryan Dentchev

lst = ['a', 'b', 'c']


def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = 2 * v
    return lst


print(double_stuff(lst))
