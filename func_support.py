import sys

def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

def count_size(x):
    sizeofitems = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sizeofitems += sys.getsizeof(key)
                sizeofitems += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                sizeofitems += sys.getsizeof(item)
    return sizeofitems

def get_vars(x):
    lst = []
    for vars in x:
        if vars.startswith("__") == 0:
            lst.append(vars)
    return lst