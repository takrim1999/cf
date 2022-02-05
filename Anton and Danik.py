import sys
game = sys.stdin.readlines()[1][:-1]
if game.count("A") > game.count("D"):
    print("Anton")
elif game.count("A") < game.count("D"):
    print("Danik")
elif game.count("A") == game.count("D"):
    print("Friendship")
else:
    print("DIE")