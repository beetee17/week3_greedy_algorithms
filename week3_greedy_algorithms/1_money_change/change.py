# Uses python3
import sys


def get_change(m):
    """The goal in this problem is to find the minimum number of coins needed
    to change the input value (an integer) into coins with denominations 1, 5, and 10.
    The input consists of a single integer 𝑚
    1 ≤ 𝑚 ≤ 10
    Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚."""

    coins = 0
    while m > 0:
        if m == 0:
            return coins

        if m >= 10:
            coins += m // 10
            m = m % 10

        elif m >= 5:
            coins += m // 5
            m = m % 5

        else:
            coins += m
            m = 0

    return coins


if __name__ == "__main__":

    m = int(input())
    print(get_change(m))
