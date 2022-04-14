import sys
pas = [str(x)[:-1] for x in sys.stdin.readlines()[1:]]
lst = []
prob = 0
for i in pas:
    prob = prob - int(i.split()[0])
    lst.append(prob)
    prob = prob + int(i.split()[1])
    lst.append(prob)
print(max(lst))