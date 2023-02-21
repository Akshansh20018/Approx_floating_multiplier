import random

def leading_bit_decimal(num):
    cnt = 0
    while num > 1:
        num = num >> 1
        cnt += 1
    return cnt

def binary_to_float(binary):
    # Split the binary string into integer and fractional parts
    int_binary, frac_binary = binary.split(".")
    int_binary = int(int_binary, 2)
    frac_binary = frac_binary[::]

    # Convert the integer part to a float
    float_num = float(int_binary)

    # Convert the fractional part to a float
    for i, bit in enumerate(frac_binary):
        if bit == "1":
            float_num += 2 ** (-(i + 1))

    return float_num


def trunc_unit(ip, t):
    # Assuming ip is the 32 bit input
    # ip is assumed to be a string
    ip = ip + "0"*(32-len(ip))
    num= int(ip, 2)
    s= "1"*t+"0"*(32-t)
    temp= int(s, 2)
    ans= num&temp
    ans_bin= bin(ans)[2:]
    l= len(ans_bin)
    ans_fin= (32-l)*"0"+ans_bin
    return ans_fin

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
    if(carry == 1):
        ans = str(carry) + ans
    return (ans)

def float_bin(number):
    res = bin(number).lstrip("0b") 
    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
    
def float_to_binary(num):
    # Convert the float to a string to extract the integer and fractional parts
    str_num = str(num)
    int_part, frac_part = str_num.split(".")
    int_part = int(int_part)
    frac_part = float("0." + frac_part)

    # Convert the integer part to binary
    int_binary = bin(int_part)[2:]

    # Convert the fractional part to binary
    frac_binary = ""
    i = 0
    while frac_part > 0 and i < 32:
        frac_part = frac_part * 2
        if frac_part >= 1:
            frac_binary += "1"
            frac_part -= 1
        else:
            frac_binary += "0"
        i += 1

    # Return the combined binary representation of the integer and fractional parts
    return int_binary + "." + frac_binary

def approx(num,h):
    s = 2**h
    number = 0
    power = -1
    for i in num:
        number += int(i) * 2**power
        power -= 1
    for i in range(1,s+1):
        if ((i-1)/s) <= number <= (i/s):
            approx = (2*i-1)
            approx /= 2*s
    print(float_to_binary(approx))
    return float_to_binary(approx)[2:]+ "0"*(32-len(float_to_binary(approx)[2:]))

#places 
def getError(a,b,h,t):
    bin_a = float_bin(a)
    bin_b = float_bin(b)

    ka = leading_bit_decimal(a)
    kb = leading_bit_decimal(b)

    y_a = bin_a[1:]
    y_a = y_a + "0"*(32-len(y_a))
    y_b = bin_b[1:]
    y_b = y_b + "0"*(32-len(y_b))

    y_at = trunc_unit(y_a, t)
    y_bt = trunc_unit(y_b, t)

    y_at = binary_to_float("0."+y_at)
    y_bt = binary_to_float("0."+y_bt)

    y_apx = "0."+approx(y_a,h)
    y_bpx = "0."+approx(y_b,h) 

    y_apx = binary_to_float(y_apx)
    y_bpx = binary_to_float(y_bpx)

    num = (1 +y_at+y_bt + y_apx*y_bpx)*2**(ka+kb)
    return abs(num - a*b)/(a*b)


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

    h= 5
    t= 8
    error = getError(a,b,h,t)
    total_error += error

print("Average Error: ", total_error/tests)
