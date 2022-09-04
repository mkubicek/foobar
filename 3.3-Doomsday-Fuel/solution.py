#
# Solution for Doomsday Fuel:
# Get probabilities for reaching absorbing states (final states).
#
# Time O(n^3) -> np.linalg.det
# Space O(n)
#
# Calculated using some absorbing markov chain linalg magic (https://en.wikipedia.org/wiki/Absorbing_Markov_chain):
# 1) Divide probability matrix p in the form
#    P= Q  R
#       0  I
# 2) Calculate 
#    ((I_dim(Q) - Q) ^ -1) * R
#    -> First row gives the probabilities for reaching absorbing states

import numpy as np

def solution(m):
    # determine indexes for transient and absorbing states
    transient_states_idx = [idx for idx, state in enumerate(m) if sum(state) != 0]
    absorbing_states_idx = [idx for idx, state in enumerate(m) if sum(state) == 0]

    # special case: state 0 is final state
    if sum(m[0]) == 0:
        return [1] + [0] * (len(absorbing_states_idx) - 1) + [1]

    # pack all transient state transition probabilities into numpy matrix 
    m = np.matrix(m, dtype=float)[transient_states_idx, :]
    # find common denominator by multiplying the denominators of each transition probability row
    denominator = np.prod(m.sum(1))
    # create proper probability matrix by dividing by denominator of each transition probability row
    prob = m / m.sum(1)
    # divide into Q and R
    Q = prob[:, transient_states_idx]
    R = prob[:, absorbing_states_idx]
    I = np.identity(len(transient_states_idx))
    N = (I - Q) ** (-1)
    result = (N[0] * R * denominator / np.linalg.det(N))
    result = result.round().astype(int).A1
    gcd = np.gcd.reduce(result)
    result = np.append(result, result.sum())
    return (result / gcd).astype(int).tolist()

if __name__ == "__main__":
    #print(solution([[0]]))
    #print(solution([[0, 1, 2, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    #print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))