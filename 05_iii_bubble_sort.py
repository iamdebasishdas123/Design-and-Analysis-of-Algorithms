def bubble_sort(A):
    count = 0 
    m = len(A) - 1
    for i in range(len(A)-1):
        for j in range(m):
            count += 1 
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                m = j 
    print("No. of comparisons = ",count)
    return A

arr = [4, 3, 2, 1, 7, 8, 9, 10]
print("The sorted array is- ",bubble_sort(arr))