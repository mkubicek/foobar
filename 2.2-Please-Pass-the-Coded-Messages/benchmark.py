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

if __name__ == '__main__':
    import timeit
    a_slowest = []
    b_slowest = []
    while True:
        digits = [random.randint(0, 9) for i in range(19)]
        a_time = timeit.timeit("a(" + str(digits) + ")", setup="from __main__ import a")
        a_slowest.append((a_time, "".join(map(str, digits))))
        a_slowest.sort(reverse=True)
        a_slowest = a_slowest[:10]
        print("a: " + str(a_slowest))
        
        b_time = timeit.timeit("b(" + str(digits) + ")", setup="from __main__ import b")
        b_slowest.append((b_time, "".join(map(str, digits))))
        b_slowest.sort(reverse=True)
        b_slowest = b_slowest[:10]
        print("b: " + str(b_slowest))