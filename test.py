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

def shift_multiply(a, b):
    # Assuming two 32 bit string inputs
    ans= "0"*32
    
    for i in range(0, 32):
        if b[31-i]=="1":
            temp= a+"0"*(i)
            ans= adder(ans, temp)

    # returning a n bit bin string
    return ans

a= "0"*27
a+= "11101"
b= "0"*27
b+= "10111"

num1= int(a, 2)
num2= int(b, 2)

print(shift_multiply(a, b))
print(len(shift_multiply(a, b)))
print(num1)
print(num2)
print(num1*num2)
print(int(shift_multiply(a, b), 2))