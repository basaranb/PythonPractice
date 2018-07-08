import math

C=50
H=30
D=raw_input().split(",")
Q=[(str(round(math.sqrt(2*C*float(D[i])/H)))) for i in range (len(D))]
print (Q)
