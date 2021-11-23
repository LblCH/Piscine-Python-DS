def data_types():
    a = 1
    b = '1'
    c = 1.1
    d = True
    e = [1, 2]
    f = {'a': 1, 'b': 2}
    g = (1, 2)
    i = {1, 2}
    print(
        f'[{type(a).__name__}, {type(b).__name__}, {type(c).__name__}, {type(d).__name__}, {type(e).__name__}, '
        f'{type(f).__name__}, {type(g).__name__}, {type(i).__name__}]'
    )


if __name__ == '__main__':
    data_types()
