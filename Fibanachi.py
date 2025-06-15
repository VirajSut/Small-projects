def Fibanaci(n):
    n= int(n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    num1 = 1
    num2 = 2

    flip = True

    n-=2

    while(n!=0):
        if flip == True:
            num1 =num1 +num2
            flip =False
        else:
            num2 =num2+num1
            flip =True
        n -=1
    out =0
    if flip ==True:
        out =num2
    if flip ==False:
        out = num1
    
    return out
while True:
    num = input("How many")

    print(Fibanaci(num))
