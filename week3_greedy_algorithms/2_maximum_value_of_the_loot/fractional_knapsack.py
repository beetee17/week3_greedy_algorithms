# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

    Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.

    The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers vi and wi—the value
    and the weight of 𝑖-th item, respectively.

    1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑊 ≤ 2·10^6; 0 ≤ vi ≤ 2·10^6, 0 < wi ≤ 2·10^6 for all 1 ≤ i ≤ n. All the numbers are integers.

    Output Format. Output the maximal value of fractions of items that fit into the knapsack.

    The absolute value of the difference between the answer of your program and the optimal value should be at most 10^-3
    To ensure this, output your answer with at least four digits after the decimal point(otherwise your answer, while
    being computed correctly, can turn out to be wrong because of rounding issues)"""

    VALUE = 0
    WEIGHT = 1
    value = 0.0

    curr_capacity = capacity

    v_w = [(values[i], weights[i]) for i in range(len(values))]

    v_w = sorted(v_w, key=lambda x: x[VALUE] / x[WEIGHT], reverse=True)

    while curr_capacity > 0 and v_w:
        # terminate loop when knapsack is full or no more items left to take
        item = v_w[0]
        if item[WEIGHT] <= curr_capacity:
            # Take all of most valuable (by ratio) item
            v_w.remove(item)
            curr_capacity -= item[WEIGHT]
            value += item[VALUE]
        else:
            # take as much as possible
            fraction_taken = curr_capacity / item[WEIGHT]
            value_taken = fraction_taken * item[VALUE]
            value += value_taken
            curr_capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # print(data)

    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
