def max_heapify(arr):
    '''
    Utility: Constructs a max_heap from the given array.
    '''

    for i in range(len(arr)):
        j = i
        while j>0:
            #find out the parent for the element
            element = arr[j]
            parent = arr[(j-1)//2]
            if (element>parent):
                arr[j] = parent
                arr[(j-1)//2] = element
            #Move to the parent index and repeat the check.
            j = (j-1)//2
    return arr


def heapsort(arr):
    '''
    Utility: Sorts the arr in asc order using max_heapify function
    '''
    heapified_arr = max_heapify(arr)
    for k in range(len(heapified_arr)-1, 0, -1):
        first_element = heapified_arr[0]
        #swapping first and last element
        heapified_arr[0] = heapified_arr[k]
        heapified_arr[k] = first_element
        #since we swapped the last element, we need to heapify [0,k] heapify again.
        heapified_arr = max_heapify(heapified_arr[0:k])+heapified_arr[k:]
    return heapified_arr

arr0 = []
print("Heapsorting ",arr0, " = ", heapsort(arr0))

arr1 = [3, 4, 0, 1, 2]
print("Heapsorting ",arr1, " = ", heapsort(arr1))

arr2 = [7,9,2,4,6,1,0]
print("Heapsorting ",arr2, " = ", heapsort(arr2))

arr2 = [6,5,4,3,2,1]
print("Heapsorting ",arr2, " = ", heapsort(arr2))