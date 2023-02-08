import random

a_lst= []
b_lst= []
res_apox_lst= []
res_accu_lst= []
error_lst= []

# For 8-bit: 255
# For 16-bit: 65535
# For 32-bit: 4294967295

for tata in range (0, 100):
    a_lst.append(random.randint(1, 65535))
    b_lst.append(random.randint(1, 65535))

for tata in range (0, 100):
    a= a_lst[tata]
    b= b_lst[tata]

    h= 0
    t= 2
    s= 2**h

    bin_a= bin(a)[2:]
    bin_b= bin(b)[2:]

    ka= len(bin_a)-1
    kb= len(bin_b)-1

    ya, yb= 0, 0

    # if t+1<len(bin_a) and t+1<len(bin_b):
    #     ya= int(bin_a[1:t+1], 2)
    #     yb= int(bin_b[1:t+1], 2)
    # elif t+1<len(bin_a):
    #     ya= int(bin_a[1:t+1], 2)
    #     yb= int(bin_b[1:], 2)
    # elif t+1<len(bin_b):
    #     ya= int(bin_a[1:], 2)
    #     yb= int(bin_b[1:t+1], 2)
    # else:
    #     ya= int(bin_a[1:], 2)
    #     yb= int(bin_b[1:], 2)

    i, j= 1, 1

    temp= 1
    while(i<len(bin_a) and i<t+1):
        # print("Hi1")
        temp= temp/2
        if(bin_a[i]=='1'):
            ya+=temp
        i+=1

    temp= 1
    while(j<len(bin_b) and j<t+1):
        # print("Hi2")
        temp= temp/2
        if(bin_b[j]=='1'):
            yb+=temp
        j+=1

    yapx= 0
    ybpx= 0

    for i in range(0, s+1):
        if ya<(i/s):
            yapx= (i-1)/s
            break

    for i in range(0, s+1):
        if yb<(i/s):
            ybpx= (i-1)/s
            break
    
    # print(bin_b[0])
    # print(bin_b[0]=='1')

    aprox_pro= (2**(ka+kb))*(1+ya+yb+(yapx*ybpx))
    accur_pro= a*b
    error= (abs(aprox_pro-accur_pro)/accur_pro)*100

    res_apox_lst.append(aprox_pro)
    res_accu_lst.append(accur_pro)
    error_lst.append(error)

# for tata in range (0, 100):
#     print("Number 1:", a_lst[tata], "Number 2:", b_lst[tata])
#     print("Approx Result:", res_apox_lst[tata])
#     print("Accurate Result", res_accu_lst[tata])
#     print("Percentage Error:", error_lst[tata])
#     print()

error_tot= sum(error_lst)
error_avg= error_tot/100

print("Average Error:", error_avg)