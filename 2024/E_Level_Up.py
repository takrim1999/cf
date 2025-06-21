import sys

playerLevel = 1


def match(monster, fight):
    monster = monster.split(" ")
    fight = fight.split(" ")
    print("Player Level", playerLevel)
    index, level = fight
    print(index)
    print(level)
    # monster = monster.split()
    # print(level, monsters[index - 1])


monsters, *fights = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
# for i in fights:
#     print(match(monsters, fights))
# print((fights))
for i in fights:
    print(match(monsters, i))
