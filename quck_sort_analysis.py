import random
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

#swap the two given indices of an array
def swap(arr, l, r):
    left_item = arr[l]
    right_item = arr[r]
    arr[l] = right_item
    arr[r] = left_item
    return arr

#This function returns the index of the pivot element, which will divide the array into two halves.
#arr = given array
#pivot = pivot element
#l = left cursor
#r = right cursor
def partition(arr):
    pivot = arr[0]
    l = 0
    r = len(arr)-1
    while(l<r):
        # print("Details for this loop:")
        # print(arr)
        # print("l = ", l)
        # print("r = ", r)
        #increment l until an element greater than pivot is found
        while(arr[l]<=pivot and l<r):
            l = l+1
            # print("l updated to ", l)
        #decrement right cursor until an element lower than pivot is found
        while(arr[r]>pivot and r>=l):
            r = r-1
            # print("r updated to ", r)

        #if such elements are found
        if(l < r):
            arr = swap(arr, l ,r)
            # print('Inner swap')
        
    arr = swap(arr, 0, r) #since pivot = arr[0]
    # print('Pivot swap')
    # print('Result = ', arr)
    pivot_index = r
    return arr, pivot_index


#quicksort function
def quicksort(arr):
    if(len(arr)==0 or len(arr)==1):
        return arr
    arr, pivot_index = partition(arr)
    first_arr = quicksort(arr[0:pivot_index])
    second_arr = quicksort(arr[pivot_index+1:])
    return first_arr+[arr[pivot_index]]+second_arr


# minimum range of random numbers
lowerBound = 0;
 
# maximum range of random numbers
upperBound = 1000;
 
# minimum size of reqd array
minSize = 10;
 
# maximum size of reqd array
maxSize = 1000000;

# size = random.randrange(0, maxSize - minSize) + minSize;
size = 1000000
array = [0]*size;

print(size);

for j in range(size):
    array[j] = int(random.uniform(0, upperBound - lowerBound) + lowerBound);

# print("Starting for ", array);
print(quicksort(array));
