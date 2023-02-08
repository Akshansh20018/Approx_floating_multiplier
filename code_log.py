import math

a= float(input("Enter Number 1: "))
b= float(input("Enter Number 2: "))

log_a= math.log(a, 2)
log_b= math.log(b, 2)

log_tot= log_a + log_b

ans= 2**(log_tot)

print("Ans: ", a*b)
print("Using log: ", ans)