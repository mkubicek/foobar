#
# Solution for Doomsday Fuel:
# 
# Matrix multiplication code: https://www.programiz.com/python-programming/examples/multiply-matrix
# Matrix inverse, gaussian elimination code: https://stackoverflow.com/a/61741074
#
from fractions import Fraction

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def multiply(X, Y):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def solution(m):
    denominators = [sum(x) for x in m]
    final_states = denominators.count(0)
    Q = [x[:len(m)-final_states] for x in m[:len(m)-final_states]]
    R = [x[len(m)-final_states:] for x in m[:len(m)-final_states]]
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            Q[i][j] = Fraction(Q[i][j], denominators[i])
    for i in range(len(R)):
        for j in range(len(R[0])):
            R[i][j] = Fraction(R[i][j], denominators[i])
    
    # I - Q
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            if i == j:
                Q[i][j] = Fraction(1, 1)
            else:
                Q[i][j] = Q[i][j] * -1
    
    P = multiply(inverse(Q), R)[0]

    max_denominator = max([x.denominator for x in P])
    common_denominator = max_denominator
    for denominator in [x.denominator for x in P]:
        if common_denominator % denominator != 0:
            common_denominator = common_denominator * denominator
            
    for idx, prob in enumerate(P):
        P[idx] = P[idx].numerator * (common_denominator // P[idx].denominator)
    P.append(common_denominator)
    
    return P

if __name__ == "__main__":
    print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))