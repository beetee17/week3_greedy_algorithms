# Uses python3
import sys


def optimal_summands(n):
    """You are organizing a funny competition for children. As a prize fund you have π candies. 
    You would like to use these candies for top π places in a competition with a natural restriction 
    that a higher place gets a larger number of candies. To make as many children happy as possible, 
    you are going to find the largest value of π for which it is possible.

    Task. The goal of this problem is to represent a given positive integer π as a sum of as many 
    pairwise distinct positive integers as possible. That is, to find the maximum π such that π 
    can be written as π1+π2+Β·Β·Β·+ππ, where π1, ... , ππ are positive integers and ππ  ΜΈ= ππ 
    for all 1 β€ π < π β€ π.

    Input Format
    The input consists of a single integer π
    Constraints
    1 β€ π β€ 10^9 
    Output Format
    In the first line, output the maximum number π such that π can be represented as a sum of π 
    pairwise distinct positive integers. In the second line, output π pairwise distinct 
    positive integers that sum up to π (if there are many such representations, output any of them)."""

    summands = []

    a = 1
    while n - a >= 0:
        summands.append(a)
        n -= a
        a += 1

    if n != 0:
        summands[-1] += n

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
