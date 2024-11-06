def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(elem, A):
    pivot = elem
    low = 0
    high = len(A) - 1
    i = low
    j = high
    while i <= j:
        while i <= high and A[i][0] <= pivot[0]: 
            i += 1
        while j > low and A[j][0] > pivot[0]:     
            j -= 1
        if i < j:
            swap(A, i, j)
            i += 1
            j -= 1
    swap(A, A.index(pivot), j)
    return j

def QuickSort(A, low, high):
    if low < high:
        pivot_index = high
        pivot = A[pivot_index]

        pos = partition(pivot, A)
        QuickSort(A, low, pos-1)
        QuickSort(A, pos+1, high)
    return A

# Input array with original indices
arr = [(3, 0), (3, 1), (2, 2), (1, 3), (8, 4)]

# Sort the array using Quicksort
sorted_arr = QuickSort(arr, 0, len(arr) - 1)

# Check stability: Extract indices of elements with the same value
ind = [index for value, index in sorted_arr if value == 3]

# Verify if the relative order of 5s is preserved
is_stable = (ind == sorted(ind))

print("Sorted array:", [value for value, index in sorted_arr])
print("The sort is stable:", is_stable)