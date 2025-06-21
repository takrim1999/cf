import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
string = inp[0]
count = 0
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        count += 1
    else:
        
print(count + 1)
