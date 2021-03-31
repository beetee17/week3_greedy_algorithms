# Uses python3
import re
from itertools import permutations, combinations
from itertools import product
import sys


def hasBetterDigits(a, b):
    # Safe move: a has better digits than b if the number when
    # a is concatenated to b is greater/equal to the opposite
    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        return True
    return False


def largest_number(a):
    # write your code here
    res = ""
    a_copy = a.copy()

    while a_copy:
        # print(a_copy)
        best_num = 0

        for num in a_copy:

            if hasBetterDigits(num, best_num):

                best_num = num
                # print('curr best_num', best_num)

        # print('best_num is', best_num)

        res += str(best_num)
        # print('removing', best_num, 'from list\n')
        a_copy.remove(best_num)

    return res


def largest_number_brute_force(a):

    a = list(map(str, a))  # convert all int to str
    digits = []
    for num in a:
        for digit in num:
            digits.append(digit)

    all_possible = permutations(digits)

    all_possible = sorted(set(map(int, ["".join(x)
                                        for x in all_possible])), reverse=True)

    for permutation in map(str, all_possible):

        finds = []
        # print(permutation)

        for num in a:
            i = 0
            find = []
            while permutation.find(num, i) != -1:

                match_at = permutation.find(num, i)
                i = match_at + 1

                find.append((match_at, match_at + len(num) - 1))
            finds.append(find)
        # print(finds)

        possible = True

        for x in finds:
            if not x:
                possible = False
                break

        if possible:

            combinations = list(product(*finds))
            # print('all combinations', combinations)
            sorted_combinations = []

            for c in combinations:

                sorted_combination = sorted(c, key=lambda x: x[0])
                sorted_combinations.append(sorted_combination)

            START = 0
            END = 1

            # print('sorted combinations', sorted_combinations)

            for c in sorted_combinations:

                valid = True

                for i in range(len(c)-1):
                    # print('checking if', c[i], 'overlaps', c[i+1])
                    if c[i][END] >= c[i+1][START]:
                        # print('invalid: overlap found')
                        valid = False
                        break

                if valid:
                    # print('valid permutation: no overlaps')
                    return permutation


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    # To test greedy against brute force with RNG cases
    # while True:

    #     import random
    #     test_len = random.randint(1, 4)
    #     test_case = []
    #     for i in range(test_len):
    #         test_case.append(random.randint(1, 99))

    #     a = test_case

    #     print(a)
    #     greedy = largest_number(a)
    #     b_f = largest_number_brute_force(a)
    #     print('greedy', greedy)
    #     print('brute force', b_f)
    #     print('\n')
    #     if greedy != b_f:
    #         print('INCORRET')
    #         break
