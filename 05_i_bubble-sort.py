def bubble_sort(A):
    count = 0 
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            count += 1 
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                flag = 1
    print("No. of comparisons = ",count)
    return A

arr = [78, 2, 5, 23, 76, 12, 17]
print("The sorted array is- ",bubble_sort(arr))