#main function for merging
def merge(arr1, arr2):
    # i = len(arr1)
    # j = len(arr2)
    new_arr = []
    i = 0
    j = 0
    #compare and insert into new array
    while i<len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i = i+1
        elif arr1[i] > arr2[j]:
            new_arr.append(arr2[j])
            j = j+1
    #for remaining elements
    while i<len(arr1):
        new_arr.append(arr1[i])
        i = i+1
    while j<len(arr1):
        new_arr.append(arr2[j])
        j = j+1
    return new_arr

#function to mergesort
def mergesort(array):
    if(len(array)==1 or len(array)==0):
        return array
    
    mid = len(array)//2
    arr1  = mergesort(array[0:mid])
    arr2 = mergesort(array[mid:])
    return merge(arr1, arr2)

arr = [0]
print(mergesort(arr))