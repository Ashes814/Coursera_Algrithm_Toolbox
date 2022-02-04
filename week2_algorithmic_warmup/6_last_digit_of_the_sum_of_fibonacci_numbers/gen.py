import sys
import os


n = int(sys.argv[1])

for i in range(n):
    #print("First n is: ")

    os.system('python3 fibonacci_sum_last_digit.py ' + str(i))