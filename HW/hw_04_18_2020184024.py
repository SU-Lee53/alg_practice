import random

random.seed('class_04')
BIN_SIZE = 25
nums = [ random.randint(2, 9) for _ in range(30) ]
print(nums)

#bin = [ 1, 2, 3 ]
bins = [ bin ]

def bin_free(bin):
    return BIN_SIZE - sum(bin)

def bin_can_hold(bin, size):
    return bin_free(bin) >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

def first_fit(size):
    for b in bins:
        if bin_can_hold(b, size):
            return b
    return new_bin()

def next_fit(size):
    if len(bins) > 0 and bin_can_hold(bins[-1], size):
        return bins[-1]
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE
    for b in bins:    # 담을 수 있으면서 가장 작은 공간이 남아있는 통을 찾음
        if bin_can_hold(b, size) and bin_free(b) < smallest_size:
            smallest_bin = b
            smallest_size = bin_free(b)
    return smallest_bin if smallest_bin is not None else new_bin()

def worst_fit(size):
    largest_bin = None
    largest_size = 0
    for b in bins:
        if bin_can_hold(b, size) and bin_free(b) > largest_size:
            largest_bin = b
            largest_size = bin_free(b)
    return largest_bin if largest_bin is not None else new_bin()

for fit_func in [first_fit, next_fit, best_fit, worst_fit]:
    bins = []
    for num in nums:
        bin = fit_func(num)
        bin.append(num)
    print(f'Function: <<{fit_func.__name__}>>')
    print(bins)

