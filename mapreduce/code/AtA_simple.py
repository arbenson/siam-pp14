def map(key, val):
    # .T --> Python NumPy transpose
    yield (0, val.T * val)

def reduce(key, vals):
    yield (0, sum(vals))
