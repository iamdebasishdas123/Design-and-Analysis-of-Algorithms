def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("How many terms of Fibonacci you want: ")) 
for i in range(n):
    print(fibo(i),end='')
    if i != n-1:
        print(", ",end='')

def dynamic_fibonacci(A,n):
    if n == 0:
        A[0] = 0
    elif n == 1:
        A[1] = 1
    else:
        A[n] = A[n-1] + A[n-2]
    return A[n]

print("\nDynamic Programming:--\n")
n = int(input("How many terms of Fibonacci you want: "))    
A = [0 for i in range(n+1)] 
  
for i in range(n):
    print(dynamic_fibonacci(A,i),end='')
    if i != n-1:
        print(", ",end='')