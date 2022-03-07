"""
Estimate e using limit thm.
"""

import math

for k in range(1,20):
    n = 10**k
    print("k is : ", k)
    limit = (1 + (1/n))**n
    error = (abs((math.exp(1) - limit)) / math.exp(1))
    #value= math.exp(limit)
    print("       error: ",error)
    print("    estimate:", limit)
    #print("e^limit",value)



e = math.exp(1)
print(e)
