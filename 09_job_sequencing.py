def job_sequencing(A, t):
    n = len(A)

    for i in range(n):
        for j in range(n-i-1):
            if A[j][2] < A[j+1][2]:
                A[j], A[j+1] = A[j+1], A[j]

    result = [False] * t
    job = [-1] * t

    for i in range(len(A)):
        for j in range(min(t-1, A[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = A[i][0]
                break

    max_profit = 0
    for i in range(len(A)):
        if A[i][0] in job:
            max_profit += A[i][2]

    return job, max_profit

arr = [['J1',2,20],
       ['J2',2,15],
       ['J3',1,10],
       ['J4',3,5],
       ['J5',3,1]]
print("The maximum profit Job sequence is--\t",job_sequencing(arr,3)[0])
print(f"Maximum Profit: {job_sequencing(arr,3)[1]}")