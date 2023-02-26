import os
import random
import re
import collections
import sys
import math
# import



########## Inputs ##########
global inputs

def input1():
    # Nested Testcase
    global inputs
    inputs = "".join(sys.stdin.readlines()).strip().split('\n')[2::2]
    return inputs
def input2():
    #Single String Testcase
    global inputs
    inputs = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
    return inputs
def input3():    
    #Single Integer Testcase
    global inputs
    inputs = [int(x) for x in "".join(sys.stdin.readlines()).strip().split()[1:]]
    return inputs
def input4():
    #single integer Inputs
    global inputs
    inputs = int(input(""))
    return inputs

########## Functions ##########

def one_to_all(array):
    result = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i!=j and i<j:
                result.append((array[i],array[j]))
    return result

def adjacent(array):
    result = []
    for i in range(len(array)-1):
        result.append((array[i],array[i+1]))
    return result

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
            break
        return True

########## Solution ##########
def main():
    

main()