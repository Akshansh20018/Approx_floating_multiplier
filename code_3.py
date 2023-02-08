import random

def adder(num1,num2):
    carry = 0
    ans = ""
    max_len = max(len(num1),len(num2))
    num1 = (max_len-len(num1))*"0" + num1
    num2 = (max_len-len(num2))*"0" + num2
    # print(num1," ",num2)
    for i in range(max_len-1,-1,-1):
        a = int(num1[i])
        b = int(num2[i])
        Sum = carry ^ (a ^ b)
        ans = str(Sum) + ans
        carry = (((a ^ b)&carry)| ((a&b)))
        # print(a," ",b," ",carry," ",Sum," ",ans)
    ans = str(carry) + ans
    return (ans)

def float_bin(number):
    res = bin(number).lstrip("0b") 
    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
 
#places 
def getError(a,b,h,t):
    bin_a = float_bin(a)
    bin_b = float_bin(b)

    ka = len(bin_a)-1 
    kb = len(bin_b)-1
    bin_a = bin_a.replace(".", "")
    bin_b = bin_b.replace(".", "")
    bin_a = bin_a[0]+"."+bin_a[1:]
    bin_b = bin_b[0]+"."+bin_b[1:]
    bin_a = bin_a[:t+2]
    bin_b = bin_b[:t+2]
    s = 2**h

    Ya = 0
    cnt = -1
    for i in bin_a[2:]:
        Ya += int(i) * 2**cnt
        cnt -= 1

    Yb = 0
    cnt = -1
    for i in bin_b[2:]:
        Yb += int(i) * 2**cnt
        cnt -= 1

    Yapx = 0
    for i in range(1,s+1):
        if ((i-1)/s) <= Ya <= (i/s):
            Yapx = (2*i-1)
            Yapx /= 2*s
            break

    Ybpx = 0
    for i in range(1,s+1):
        if ((i-1)/s) <= Yb <= (i/s):
            Ybpx = (2*i-1)
            Ybpx /= 2*s
            break


    mul_appx = 2**(ka+kb) * (1+Ya+Yb+(Yapx*Ybpx)) 
    mul_acc = a*b
    return (abs(mul_appx-mul_acc)/mul_acc)*100

def trunc_unit(ip, t):
    # Assuming ip is the 32 bit input
    # ip is assumed to be a string

    num= int(ip, 2)

    s= "1"*t+"0"*(32-t)
    temp= int(s, 2)

    ans= num&temp

    ans_bin= bin(ans)[2:]
    l= len(ans_bin)
    ans_fin= (32-l)*"0"+ans_bin

    # returning a 32 bit bin string
    return ans_fin

def shift_multiply(a, b):
    # Assuming two 32 bit string inputs
    ans= "0"*32
    
    for i in range(0, 32):
        if b[31-i]=="1":
            temp= a+"0"*(i)
            ans= adder(ans, temp)

    # returning a n bit bin string
    return ans

def shifter(ka, kb, ans):
    # Assuming ka kb to be 32 bit string inputs

    k_tot= adder(ka, kb)
    tot_int= int(k_tot, 2)
    ans_fin= ans+("0"*tot_int)

    return ans_fin

a_lst= []
b_lst= []
res_apox_lst= []
res_accu_lst= []
error_lst= []
tests = pow(2,16)-1

for tata in range (0, tests):
    a_lst.append(random.randint(1, pow(2,8)-1))
    b_lst.append(random.randint(1, pow(2,8)-1))
total_error = 0
for tata in range (0, tests):
    a= a_lst[tata]
    b= b_lst[tata]

    h= 0
    t= 2
    error = getError(a,b,h,t)
    total_error += error

print("Average Error: ", total_error/tests)