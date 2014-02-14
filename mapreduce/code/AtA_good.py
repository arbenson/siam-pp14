partial_sum = zeros(n, n)
def map(key, val):
    partial_sum += val.T * val
    if key == last_key:
        yield (0, partial_sum)

def reduce(key, vals):
    yield (0, sum(vals))
