def bubble_sort(A):
    count = 0 
    for i in range(len(A)-1):
        flag = 0
        for j in range(len(A)-i-1):
            count += 1 
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                flag = 1
        if flag == 0:
            break
    print("No. of comparisons = ",count)
    return A

arr = [99, 1, 2, 3, 4, 5, 6, 7]
print("The sorted array is- ",bubble_sort(arr))