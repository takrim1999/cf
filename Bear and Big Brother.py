n = input("").split()
a = int(n[0])
b = int(n[1])
count = 0
while a<=b:
    a = a*3
    b = b*2
    count = count + 1
print(count)
