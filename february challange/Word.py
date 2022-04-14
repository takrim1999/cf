import sys
word = sys.stdin.readline()

u=0
l=0
for i in word:
    if i.isupper():
        u=u+1
    if i.islower():
        l=l+1
if u>l:
    print(word.upper())
else:
    print(word.lower())

# print(len(word))
# if updown(word)=="upper":

# print(updown(word).split("**"))