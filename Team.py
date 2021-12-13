n = int(input(""))
count = 0
for i in range(n):
    if input("").count("1") >1:
        count = count + 1
print(count)
