import sys
name = set(sys.stdin.readline()[:-1])
if len(name)%2 == 0:
    print("CHAT WITH HER!")
elif len(name)%2==1:
    print("IGNORE HIM!")