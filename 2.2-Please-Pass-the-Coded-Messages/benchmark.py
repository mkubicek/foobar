import itertools
import random
import sys

def a(digits):
    """
    Return largest number that can be formed by provided digits and is divisible by 3.
    """
    digits.sort(reverse=True)
    for r in range(len(digits), 1, -1):
        for perm in itertools.combinations(digits, r):
            if(sum(perm) % 3 == 0):
                return int(''.join(map(str,perm)))
    return 0

def b(L):
	L.sort(reverse=True)
	
	# Defining and initializing additional working variables
	Lmod3 = []
	Lmod3 = [0 for k in range(len(L))]
	cnt1 = 0
	pos1 = [0, 0]
	cnt2 = 0
	pos2 = [0, 0]
	
	# Compute L mod 3 and save up to two elements whose remainder is 1 and up to two elements whose remainder is 2
	for r in range(len(L) - 1, -1, -1):
		Lmod3[r] = L[r] % 3
		if(Lmod3[r] == 1 and cnt1 < 2):
			pos1[cnt1] = r
			cnt1 = cnt1 + 1
		elif(Lmod3[r] == 2 and cnt2 < 2):
			pos2[cnt2] = r
			cnt2 = cnt2 + 1
		else:
			pass
	    
	total = sum(Lmod3)
	# Only three scenarios can occur: (total % 3) == 0, (total % 3) == 1 or (total % 3) == 2
	if(total % 3 == 0):
		return int(''.join(map(str,L)))
	elif (total % 3 == 1):
		if(cnt1 > 0):
			L.remove(L[pos1[0]])
			return int(''.join(map(str,L)))
		elif(cnt2 > 1):
			L.remove(L[pos2[0]])
			L.remove(L[pos2[1]])
			return int(''.join(map(str,L)))
		else:
			return 0
	else:
		if(cnt2 > 0):
			L.remove(L[pos2[0]])
			return int(''.join(map(str,L)))
		elif(cnt1 > 1):
			L.remove([pos1[0]])
			L.remove(L[pos1[1]])
			return int(''.join(map(str,L)))
		else:
			return 0

def c(digits):
    digits.sort(reverse=True)
    # variables to hold index of digits with %3 remainder 1 and 2
    r1_a = None
    r1_b = None
    r2_a = None
    r2_b = None
    modulo3 = [digit % 3 for digit in digits]
	
	# Compute L mod 3 and save up to two elements whose remainder is 1 and up to two elements whose remainder is 2
    for i in range(len(digits) - 1, -1, -1):
        if(modulo3[i] == 1 and (r1_a is not None or r1_b is not None)):
            if r1_a is not None:
                r1_a = i
            elif r1_b is not None:
                r1_b = i
            else:
                pass
        elif(modulo3[i] == 2 and (r2_a is not None or r2_b is not None)):
            if r2_a is not None:
                r2_a = i
            elif r2_b is not None:
                r2_b = i
            else:
                pass
        else:
            pass
    
    total = sum(modulo3)
    # Only three scenarios can occur: (total % 3) == 0, (total % 3) == 1 or (total % 3) == 2
    if(total % 3 == 0):
        return int(''.join(map(str,digits)))
    elif (total % 3 == 1):
        if(r1_a is not None):
            del digits[r1_a]
            if(len(digits) > 0):
                return int(''.join(map(str, digits)))
            return 0
        elif(r2_a is not None and r2_b is not None):
            del digits[r2_a]
            del digits[r2_a]
            if(len(digits) > 0):
                return int(''.join(map(str, digits)))
            return 0
        else:
            return 0
    else:
        if(r2_a is not None):
            del digits[r2_a]
            if(len(digits) > 0):
                return int(''.join(map(str, digits)))
            return 0
        elif(r1_a is not None and r1_b is not None):
            del digits[r1_a]
            del digits[r1_b]
            if(len(digits) > 0):
                return int(''.join(map(str, digits)))
            return 0
        else:
            return 0

if __name__ == '__main__':
    import timeit
    inputs = ['2100292407616905611', '0475942439666624275']
    for input in inputs:
        input = map(int,list(input))
        print("Input: " + str(input))
        print(timeit.timeit("a(" + str(input) + ")", setup="from __main__ import a"))
        print(timeit.timeit("b(" + str(input) + ")", setup="from __main__ import b"))
        print(timeit.timeit("c(" + str(input) + ")", setup="from __main__ import c"))