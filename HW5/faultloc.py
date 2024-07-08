import sys
import operator
import math
from collections import defaultdict

def check_if_num(num):
    return num == '#####' or num == '-'

def extract_data(line):
    return line.split(':')[0].split(' ')[-1], int(line.split(':')[1].split(' ')[-1])


if __name__ == '__main__':

    line_nums = []
    num_failed_files = 0
    passed_num = defaultdict(int)
    failed_num = defaultdict(int)


    for fname in sys.argv[1:]:
        file = open(fname, 'r')
        lines = file.read().split('\n')
        file.close()

        if 'fail' in fname:
            num_failed_files += 1

        for line in lines:
            if not line:
                continue

            num_visits, line_num = extract_data(line)

            if check_if_num(num_visits):
                continue
            
            if line_num not in line_nums:
                line_nums.append(line_num)

            if 'pass' in fname:
                passed_num[line_num] += 1
            elif 'fail' in fname:
                failed_num[line_num] += 1

    oshas = {}
    for line in line_nums:

        osha = failed_num[line] / math.sqrt(
            num_failed_files * (
                failed_num[line] + passed_num[line]))

        oshas[line] = osha


    sorted_by_keys = sorted(
        oshas.items(), key=operator.itemgetter(0), reverse=False)

    sorted_oshas = sorted(
        sorted_by_keys, key=operator.itemgetter(1), reverse=True)

    print(sorted_oshas[:100])
