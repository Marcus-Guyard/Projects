
def sym(*args):
    args = list(args)
    n = len(args)
    sym_args = set()
    while len(args) > 1:
        args1 = args[0]
        args2 = args[1]
        sym_args = set(args1).symmetric_difference(args2)
        args[0] = sym_args
        args.remove(args2)
    return list(sym_args)

print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))