import math
from cmath import log

fp = open('data/rosalind_prob.txt')
DNAGC = fp.readline(1000)
prob = fp.readline(1000)
# DNAGC = []
# prob = []
print(DNAGC, prob)
probs = []
for x in range(0,len(prob),6):
    probs.append(float(prob[x:x+6]))
print(probs)
def probGC(prob):
    return prob/2

def probAT(prob):
    return (1-prob)/2
com_logs = []
for i in probs:
    a = 1
    b = 0
    for x in DNAGC:
        b+=1
        print(a)
        if b > len(DNAGC)-1:
            break
        else:
            if x == 'A' or x == 'T':
                a *= probAT(i)
            else:
                a *= probGC(i)

    print(a)
    com_logs.append(math.log(a,10))
print(*com_logs)