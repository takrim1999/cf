import sys
count = 0
money_list = [int(x) for x in sys.stdin.readlines()[1][:-1].split()]
taken_list = []
while sum(taken_list) <= sum(money_list):
    m = max(money_list)
    taken_list.append(m)
    money_list.remove(m)
    count = count + 1 
print(count)