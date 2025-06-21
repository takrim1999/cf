n = input("").split()
a = int(n[0])
b = int(n[1])
n = a*b
if a%2!=0 and b%2!=0:
    print(int((n-1)/2))
else:
    print(int(n/2))
