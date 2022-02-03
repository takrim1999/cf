import sys
matrix = []
for i in range(5):
    try:
        j = sys.stdin.readline().split().index("1")
        k = i
    except:
        pass    

print(abs(2-j)+abs(2-k))