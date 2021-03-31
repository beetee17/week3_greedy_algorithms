# python3
import sys


def compute_min_refills(distance, tank, stops):
    """You are going to travel to another city that is located 𝑑 miles away from your home city.
    Your car can travel at most 𝑚 miles on a full tank and you start with a full tank.
    Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city.
    What is the minimum number of refills needed?

    Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚.
    The third line specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛

    Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank,
    and there are gas stations at distances stop1 , stop2 , . . . , stop𝑛 along the way, output the minimum number of refills needed.
    Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.

    Constraints
    1 ≤ 𝑑 ≤ 10^5
    1 ≤ 𝑚 ≤ 400
    1 ≤ 𝑛 ≤ 300.0 < stop1 < stop2 < ··· < stop𝑛 < 𝑑."""

    i = 0
    refills = 0
    stops.append(distance)  # add destination as the last stop

    while True:
        # print("checking stop {}, {}m away".format(i, stops[i]))
        if stops[i] < tank:  # stop is reachable on a full tank

            if (stops[i] == stops[-1]):  # if this is the last stop, no more refills needed
                return refills

            else:  # check the next stop
                i += 1

        elif stops[i] == tank:  # just nice, refill here!

            if (stops[i] == stops[-1]):  # if this is the last stop, no more refills needed
                return refills

            refills += 1
            # print("refill at stop {}".format(i))

            distance_travelled = stops[i]

            stops = stops[i + 1:]  # remove all stops up to the (i+1)th stop

            # reset distances between stops (wrt to refill stop)
            stops = [x - distance_travelled for x in stops]
            i = 0  # reset pointer

        else:  # stop is too far away, refill at previous stop (i-1)

            if i == 0:
                return -1  # the first stop is too far away and impossible to reach

            refills += 1  # refill at the (i-1)th stop
            # print("refill at stop {}".format(i))

            distance_travelled = stops[i - 1]
            stops = stops[i:]  # remove all stops up to the ith stop

            # reset distances between stops (wrt to refill stop)
            stops = [x - distance_travelled for x in stops]

            i = 0  # reset pointer


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
