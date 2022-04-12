# python3
import time
import sys

class Solver:
	def __init__(self, s):
		self.s = s
	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]

	def PolyHash(string, prime, multiplier):
		hash_value = 0
		for i in range(len(string) - 1, -1, -1):
			hash_value = (hash_value * multiplier + ord(string[i])) % prime
		return hash_value

# s = sys.stdin.readline()
s = 'trololo'
# q = int(sys.stdin.readline())
test_list = [(0,0,7), (2,4,3), (3,5,1), (1,3,2)]
solver = Solver(s)

t0 = time.time()
for i in test_list:
	# a, b, l = map(int, sys.stdin.readline().split())
	a,b,l = i

	print("Yes" if solver.ask(a, b, l) else "No")
print("Running Time", time.time()-t0)