def minIncrementForUnique(A):
    # 贪心算法
    A.sort()
    count = 0
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            count += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
    return count

print(minIncrementForUnique([1,3,3,4,4]))