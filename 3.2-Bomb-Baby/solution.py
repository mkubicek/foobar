# 
# Solution for Bomb Baby:
# Returns lowest number of (x, y) -> (x + y, y) or (x, y) -> (x, y + x) operations 
# to reach a certain number pair, starting from (1, 1). If no such sequence of operations exist, return "impossible".
# 
# Time O(log(n))
# Space O(1) 
#

def solution(x, y):
    x = int(x)
    y = int(y)
    steps = 0
    
    while (x >= 1 and y >= 1):
        if (x > y):    
            div = x // y
            if (y == 1):
                div = div - 1
            steps = steps + div
            x = x - div * y
        else:
            div = y // x
            if (x == 1):
                div = div - 1
            steps = steps + div
            y = y - div * x
    
        if (x == 1 and y == 1):
            return str(steps)
        
    return "impossible"

if __name__ == "__main__":
    print(solution(4, 7))
    print(solution(2, 1))
    print(solution(10**49, 6))