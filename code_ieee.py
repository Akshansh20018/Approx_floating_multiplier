import random

def float_to_ieee(num):
    # Check if the number is negative
    if num < 0:
        sign_bit = 1
        num *= -1
    else:
        sign_bit = 0
    
    # Convert the number to binary
    integer_part = int(num)
    fractional_part = num - integer_part
    
    integer_binary = bin(integer_part)[2:]
    fractional_binary = ''
    
    while fractional_part != 0:
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += '1'
            fractional_part -= 1
        else:
            fractional_binary += '0'
    
    # Combine the integer and fractional binary parts
    binary = integer_binary + '.' + fractional_binary
    
    # Calculate the exponent and mantissa
    exponent = 0
    
    if '.' in binary:
        integer_bits, fractional_bits = binary.split('.')
        exponent = len(integer_bits) - 1
        mantissa = integer_bits[1:] + fractional_bits
    else:
        mantissa = binary[1:]
    
    # Add the bias to the exponent
    bias = 127
    exponent += bias
    
    # Convert the exponent to binary
    exponent_binary = bin(exponent)[2:].zfill(8)
    
    # Convert the mantissa to binary
    mantissa_binary = ''
    for i in range(23):
        if i < len(mantissa):
            mantissa_binary += mantissa[i]
        else:
            mantissa_binary += '0'
    
    # Combine the sign bit, exponent, and mantissa
    binary_string = str(sign_bit) + exponent_binary + mantissa_binary
    
    # Convert the binary string to hexadecimal
    hex_string = hex(int(binary_string, 2))[2:].zfill(8)
    
    return binary_string

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

def float_bin(number, places = 3):
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int (dec)
    res = bin(whole).lstrip("0b") + "."
    cnt = 0
    try:
        for x in range(places):
            whole, dec = str((decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole
            cnt+=1
    except:
        whole, dec = str(number).split(".")
        whole = int(whole)
        dec = int (dec)
        res = bin(whole).lstrip("0b") + "."
        for x in range(cnt):
            whole, dec = str((decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole
    return res
def bin_to_int(num):
    ans = 0
    for i in range(len(num)):
        ans += int(num[i])*(2**(len(num)-i-1))
    return ans

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
 
#places 
def getMultiply(a,b,h,t):
    a_sign = a[0]
    b_sign = b[0]
    a_exp = a[1:9]
    b_exp = b[1:9]
    a_mant = a[9:]
    b_mant = b[9:]

    ka = bin_to_int(a_exp) - 127 
    kb = bin_to_int(b_exp) - 127


    s = 2**h

    Ya = 0
    cnt = -1
    for i in a_mant:
        Ya += int(i) * 2**cnt
        cnt -= 1

    Yb = 0
    cnt = -1
    for i in b_mant:
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

    a_mant = a_mant[:t]
    b_mant = b_mant[:t]

    Ya = 0
    cnt = -1
    for i in a_mant:
        Ya += int(i) * 2**cnt
        cnt -= 1

    Yb = 0
    cnt = -1
    for i in b_mant:
        Yb += int(i) * 2**cnt
        cnt -= 1

    mul_appx = 2**(ka+kb) * (1+Ya+Yb+(Yapx*Ybpx)) 
    return mul_appx

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

a_lst= [5]
b_lst= [7]


res_apox_lst= []
res_accu_lst= []
error_lst= []
tests = pow(2,16)-1

for tata in range (0, tests):
    a_lst.append(random.randint(1, pow(2,16)-1) + random.random())
    b_lst.append(random.randint(1, pow(2,16)-1) +  random.random())

total_error_int = 0
total_error_float = 0
# (1.01 * 2^ka)
# (1.01 * 2^kb)

for tata in range (0, tests):
    a_float = float_to_ieee(a_lst[tata])
    b_float = float_to_ieee(b_lst[tata])

    h= 5
    t= 9
    mul_appx_float = getMultiply(a_float,b_float,h,t)
    mul_acc_float = a_lst[tata]*b_lst[tata]

    error_float = abs(mul_appx_float - mul_acc_float)/mul_acc_float
    
    total_error_float += error_float

print("Average Error(Float): ", 100*(total_error_float/tests))