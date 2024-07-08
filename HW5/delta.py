import os
import subprocess
import sys

if len(sys.argv) != 3:
    exit(1)

check_interest = sys.argv[2]
size_of_set = int(sys.argv[1])


def main():
    random = list(range(size_of_set))

    p = minimize(set(), random)

    # print(p)
    return sorted(list(p))


def minimize(p, random):

    # base case
    if len(random) == 1:
        return random

    p1, p2 = split(random)

    if is_interesting(p.union(p1)):
        return minimize(p, p1)
    if is_interesting(p.union(p2)):
        return minimize(p, p2)

    return set().union(minimize(p.union(p2), p1), minimize(p.union(p1), p2))

def is_interesting(split_set):
    command = check_interest
    for number in split_set:
        command += ' {}'.format(number)

    return subprocess.call(command, shell=True)


def split(random):
    half = len(random)//2
    return random[:half], random[half:]



if __name__ == "__main__":
    x = main()
    print(x)
