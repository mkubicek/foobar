#
# Naive solution for Please Pass the Coded Messages
# Time O(n*log(n) + n! + (n-1)! + ..)
# Space O(n)
#
import itertools

def solution(digits):
    """
    Return largest number that can be formed by provided digits and is divisible by 3.
    """
    digits.sort(reverse=True)
    for r in range(len(digits), 0, -1):
        for perm in itertools.combinations(digits, r):
            if(sum(perm) % 3 == 0):
                return int(''.join(map(str,perm)))
    return 0

if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
    assert solution([3, 1, 4, 1]) == 4311
    assert solution([3, 1, 4, 1, 5, 9]) == 94311