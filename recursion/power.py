def pow(x,n):
    if n==0:
        return 1
    else:
        return pow(x, n-1)*x
    
x= 10
power = 5
print("Power of 2", pow(x,power))