def Max_Heapify(A,i, heapsize):
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2

    if l <= heapsize and A[l] > A[largest]:
        largest = l
    if r <= heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Max_Heapify(A,largest, heapsize)

def Asc_heap_sort(A):
    n = len(A) - 1
    heapsize = n
    
    for i in range(n//2, -1, -1):  
        Max_Heapify(A, i, heapsize)
    for i in range(n, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        Max_Heapify(A, 0, heapsize)
    return A

arr = [41, 32, 12, 19, 17, 8, 29, 171]
print("The sorted array in Ascending order is- ", Asc_heap_sort(arr))

def Min_Heapify(A,i, heapsize):
    smallest = i
    l = 2 * i + 1  
    r = 2 * i + 2

    if l <= heapsize and A[l] < A[smallest]:
        smallest = l
    if r <= heapsize and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        Min_Heapify(A,smallest, heapsize)

def Desc_heap_sort(A):
    n = len(A) - 1
    heapsize = n
    
    for i in range(n//2, -1, -1):  
        Min_Heapify(A, i, heapsize)
    for i in range(n, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        Min_Heapify(A, 0, heapsize)
    return A

arr = [41, 32, 12, 19, 17, 8, 29, 171]
print("\n\nThe sorted array is- ", Desc_heap_sort(arr))