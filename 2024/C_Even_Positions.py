import sys


def countCost(array):
    last = len(array) - 2
    prev = last - 1
    cost = 0
    while not prev < 0:
        if array[prev] == ")":
            # array[last] = "("
            cost += 1
        else:
            # array[last] = ")"
            cost += 3
        prev -= 2
        last -= 2
    if prev < 0:
        cost += 1
        # array[last] = "("
    # print(cost)
    # return "".join(array)
    return cost


inp = "".join(sys.stdin.readlines()).strip().split("\n")[2::2]
for i in inp:
    print(countCost(list(i)))

# print(countCost(list("_)")))
