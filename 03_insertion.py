def insertion_sort(A=[]):
    for j in range(1,len(A)):
        key = A[j]
        i = j -1
        while (i>=0 and A[i]>key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

arr = [6, 2, 10, 5, 4, 11, 15]
print("The sorted array is- ",insertion_sort(arr))