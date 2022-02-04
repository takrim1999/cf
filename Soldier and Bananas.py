import sys
number = sys.stdin.readline().split()
ans = (int(number[0])*int((int(number[2])*(int(number[2])+1))/2)) - int(number[1])
if ans<0:
    print(0)
else:
    print(ans)