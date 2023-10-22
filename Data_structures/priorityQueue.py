
def insert(arr, element):
    '''
    Utility: Percolates the element in the incorrect minheap array to build a correct one.
    '''
    #The index of element that is to be inserted.
    element_idx = len(arr)
    arr.append(element)
    while element_idx>0:
        #find out the parent for the element
        parent = arr[(element_idx-1)//2]
        if (element<parent):
            #swap element and parent
            arr[element_idx] = parent
            arr[(element_idx-1)//2] = element
        #Move to the parent index and repeat the check.
        element_idx = (element_idx-1)//2
    return arr

def first(arr):
    '''
    Utility: Return the  first element in the priority queue.
    '''
    if(len(arr)==0):
        return None
    return arr[0]

def remove_first(arr):
    '''Utility: Remove and return the first element in the priority queue.'''
    if(len(arr)==0):
        return None, []
    first_element = arr[0]
    #put the last element on top
    arr[0] = arr[-1]
    #create a new array without the last element
    arr_new = arr[0:-1]
    limit = len(arr_new)
    new_pos = 0
    child1 = 2*new_pos+1
    child2 = 2*new_pos+2
    #percolate
    while (child1<limit or child2<limit) and (arr_new[new_pos]<arr_new[child1] or arr_new[new_pos]>arr_new[child2]):
        #finding the smallest child
        if(arr_new[child1]<arr_new[child2]):
            min_child = child1
        else:
            min_child = child2
        #swap the parent with min_child
        temp = arr_new[min_child]
        arr_new[min_child] = arr_new[new_pos]
        arr_new[new_pos] = temp
        #update the min_child to parent and update the next children index.
        new_pos = min_child
        child1 = 2*new_pos+1
        child2 = 2*new_pos+2
    return first_element, arr_new

#Assumption: The input array is heap as stated in the question.
arr0 = [0,1,5,2,3,6]
print("After inserting 2:", insert(arr0, 2))
print("The first element = ", first(arr0))
first_element,new_arr = remove_first(arr0)
print("The first element = ", first_element)
print("New array after removal = ", new_arr)

#Assumption: The input array is heap as stated in the question.
arr0 = []
print("The first element = ", first(arr0))
first_element,new_arr = remove_first(arr0)
print("The first element = ", first_element)
print("New array after removal = ", new_arr)
print("After inserting 2:", insert(arr0, 2))