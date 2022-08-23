#
# Solution for Fuel Injection Perfection:
# Find lowest number of -1, +1 or /2 operations for any positive integer to reach 1.
#
# Time O(log(n))
# Space O(n)
#
# Idea: Eliminate 1's in least significant bit position of n's binary representation
# 0b....0 -> divide by 2
# 0b..101 -> subtract 1, then >=2x division by 2
# 0b..001 -> add 1, then division by 2
# 0b..011 -> add 1, then >=2x division by 2
#
# special case: n = 3 or 0b101 -> subtract 1, then division by 2

def solution(n):
    n = int(n)
    steps = 0
    while (n > 1): 
        if (n & 1 == 0): # divisible by 2
            n = n >> 1 # bitshift to the right; equal to division by 2
        elif (n % 4 == 1 or n == 3): # n = 0b..101 or n = 3
            n = n - 1
        else:
            n = n + 1
        steps = steps + 1
    return steps
        
if __name__ == "__main__":
    print(solution(6))
    print(solution('4'))  # 2: 4 -> 2 -> 1
    print(solution('15'))  # 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1