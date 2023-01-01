case=int(input(""))
while case>0:
    word=input("")
    if len(word)>10:
        a=int(len(word)-1)
        print(word[0] + str(a-1) + word[a])
    else:
        print(word)
    case=case-1
