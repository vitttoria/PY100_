dict_ = {}

a = list(range(0, 16))

for value in a:
    dict_['bin'] = bin(value)
    dict_['dec'] = int(value)
    dict_['hex'] = hex(value)
    dict_['oct'] = oct(value)
    print(dict_)
