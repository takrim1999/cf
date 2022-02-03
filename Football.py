import sys
team = sys.stdin.readline()
if ("0000000" in team) or ("1111111" in team):
    print("YES")
else:
    print("NO")