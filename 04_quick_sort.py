import random

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(elem, A=[]):
    pivot = elem
    low = 0
    high = len(A) - 1
    i = low
    j = high
    while i <= j:
        while i <= high and A[i] <= pivot:
            i += 1
        while j > low and A[j] > pivot:
            j -= 1
        if i < j:
            swap(A, i, j)
            i += 1
            j -= 1
    swap(A, A.index(pivot), j)
    return j

def QuickSort(A, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        pivot = A[pivot_index]

        pos = partition(pivot, A)
        QuickSort(A, low, pos-1)
        QuickSort(A, pos+1, high)
    return A

arr = [6, -2, -10, 5, 4, 11, 15, 5]
print("The sorted array is-", QuickSort(arr, 0, len(arr)-1))