import re
import sys
word = sys.stdin.readline().lower()
print("."+".".join(list(re.sub('[aeiouy]','',word)))[:-2])