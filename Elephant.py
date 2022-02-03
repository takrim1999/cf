import sys
dis = int(sys.stdin.readline())
if dis<5:
    print(1)
elif (dis>5) and (dis%5==0):
    print(int(dis/5))
elif (dis>5) and (dis%5!=0):
    print(int(dis/5)+1)
else:
    print(1)