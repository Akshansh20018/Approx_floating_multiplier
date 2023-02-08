import random

a_lst= []
b_lst= []
res_apox_lst= []
res_accu_lst= []
error_lst= []

for tata in range (0, 100):
    a_lst.append(random.randint(0, 255))
    b_lst.append(random.randint(0, 255))

for tata in range (0, 100):
    a = a_lst[tata]
    b = b_lst[tata]
    h = 8

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
    

    def decimal_converter(num):
        while num > 1:
            num /= 10
        return num
    
    #places 
    bin_a = float_bin(a, places = 50)
    bin_b = float_bin(b, places = 50)
    print(bin_a)
    print(bin_b)

    ka = bin_a.find(".") - 1
    kb = bin_b.find(".") - 1
    bin_a = bin_a.replace(".", "")
    bin_b = bin_b.replace(".", "")
    bin_a = bin_a[0]+"."+bin_a[1:]
    bin_b = bin_b[0]+"."+bin_b[1:]
    bin_a = bin_a[:9]
    bin_b = bin_b[:9]
    print(bin_a)
    print(bin_b)
    print("ka = " + str(ka))
    print("kb = " + str(kb))
    s = 2**h
    print(s)

    Ya = 0
    cnt = -1
    for i in bin_a[2:]:
        Ya += int(i) * 2**cnt
        cnt -= 1
    print(Ya)

    Yb = 0
    cnt = -1
    for i in bin_b[2:]:
        Yb += int(i) * 2**cnt
        cnt -= 1
    print(Yb)

    Yapx = 0
    for i in range(1,s+1):
        if ((i-1)/s) <= Ya <= (i/s):
            print(i)
            Yapx = (2*i-1)
            Yapx /= 2*s
            break

    Ybpx = 0
    for i in range(1,s+1):
        if ((i-1)/s) <= Yb <= (i/s):
            Ybpx = (2*i-1)
            Ybpx /= 2*s
            break
    print(Yapx)
    print(Ybpx)

    mul_appx = 2**(ka+kb) * (1+Ya+Yb+(Yapx*Ybpx)) 
    mul_acc = a*b
    print(mul_appx)
    print(mul_acc)
    error= (abs(mul_appx-mul_acc)/mul_acc)*100
    print("Error: ", error)
    res_apox_lst.append(mul_appx)
    res_accu_lst.append(mul_acc)
    error_lst.append(error)

for tata in range (0, 100):
    print("Number 1:", a_lst[tata], "Number 2:", b_lst[tata])
    print("Approx Result:", res_apox_lst[tata])
    print("Accurate Result", res_accu_lst[tata])
    print("Percentage Error:", error_lst[tata])
    print()