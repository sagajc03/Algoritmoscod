#Algoritmo Quicksort
from time import time
import numpy as np

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

# lista = [4,5,1,2,3]
# lista = np.random.randint(10000,size=1000)
lista = [22,33,60,8,2,9,1,10,99,15,12,7,3,50,61,45,65,23,44,59,75,41,24,55,77,88,100,11,0,17]
print(lista)
t0 = time()
quicksort(0,len(lista)- 1,lista)

t1 = time()
print("lista ordenada", lista)
print("Tiempo: {0:f} segundos", format(t1-t0))

