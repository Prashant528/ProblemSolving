

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
        #increment l until an element greater than pivot is found
        while(arr[l]<=pivot and l<r):
            l = l+1
        #decrement right cursor until an element lower than pivot is found
        while(arr[r]>pivot and r>=l):
            r = r-1
        #if such elements are found
        if(l < r):
            arr = swap(arr, l ,r)        
    arr = swap(arr, 0, r) #since pivot = arr[0]
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

arr = [0, 835, 701, 876, 462, 812, 146, 392, 956, 902, 946, 0]
print(quicksort(arr))