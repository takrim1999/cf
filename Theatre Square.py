n = input("").split()
m = int(n[1])
a = int(n[2])
n = int(n[0])
if n%a!=0:
    n = int(n/a) + 1
else:
    n = n/a
if m%a!=0:
    m = int(m/a) + 1
else:
    m = m/a
print(int(n*m))