import time
import math
import matplotlib.pyplot as plt
import random
from operator import add

no_of_digits = 100

def one_itr():
    time_taken = []
    input_list = []
    # input_list = random.uniform(1, 99999999999999999999, 1000)

    for i in range(0,no_of_digits, 10):
        input_list.append(int(random.uniform(1, 10)*float((10**i))))
        
    print(input_list)

    for idx, num in enumerate(input_list):
        start = time.process_time()
        # num = input("Enter the number: ")
        num = int(num)
        print(f"No of digits = {idx+1}")
        factors = []

        while num % 2 ==0:
            factors.append(2)
            num = num/2

        #above while method strips the even part of the number. Now check for odd factors
        divisor=3 #start dividing from 3
        while(divisor<=math.sqrt(num)+1):
            while num%divisor == 0:
                factors.append(divisor)
                num = num/divisor #we will do the same process for the remainder again.
            divisor += 2 #since we don't have to check for even divisors

        if num!=1:
            factors.append(int(num))

        elapsed = time.process_time() - start
        time_taken.append(elapsed)
        print(factors)
        print(f"Time taken = {round(elapsed, 5)} seconds.")
    return time_taken



no_of_itr = 10
tot_time = no_of_digits*[0]
for i in range(no_of_itr):
    time_for_itr = one_itr()
    print(len(time_for_itr))
    tot_time = list(map(add, tot_time, time_for_itr))

print(tot_time)
#plot
x_val = [i for i in range(10)]
y_val = [(total_time/no_of_itr) for total_time in tot_time ]
# plt.xticks(x_val)
plt.plot(x_val, y_val)
plt.plot(x_val, y_val, 'or')
plt.plot(x_val, [math.sqrt(x) for x in x_val])
plt.plot(x_val, [math.sqrt(x)*x**2*0.0001 for x in x_val])
plt.show()
