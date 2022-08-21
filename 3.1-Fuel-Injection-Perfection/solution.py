#
# Solution for Fuel Injection Perfection:
# Find lowest number of -1, +1 or /2 operations for any positive integer to reach 1.
#
# Time O(log(n))
# Space O(n)
#

import math


def timesDivisibleByTwo(n):
    steps = 0
    while (n % 2 == 0):
        n = n // 2
        steps = steps + 1
    return steps, n


def solution(n):
    n = int(n)
    steps = 0
    while (n > 1):
        if (n % 2 == 0):
            (steps_temp, n) = timesDivisibleByTwo(n)
            steps = steps + steps_temp
        else:
            (steps_plus_1, n_plus_1) = timesDivisibleByTwo(n + 1)
            (steps_minus_1, n_minus_1) = timesDivisibleByTwo(n - 1)
            if (n_plus_1 == 1 and n_minus_1 == 1):
                steps = steps + min(steps_plus_1, steps_minus_1) + 1
                n = 1
            elif (steps_plus_1 > steps_minus_1):
                steps = steps + steps_plus_1 + 1
                n = n_plus_1
            else:
                steps = steps + steps_minus_1 + 1
                n = n_minus_1
    return steps


if __name__ == '__main__':
    print(solution(6))
    assert solution(23) == 6
    assert solution(95) == 8
    print(solution('4'))  # 2: 4 -> 2 -> 1
    print(solution('15'))  # 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
    last = 1
    for i in range(1001):
        new = solution(i)
        if (abs(new - last) > 1):
            print("found abnomaly")
        last = new
        print("{} {}".format(i, solution(i)))
