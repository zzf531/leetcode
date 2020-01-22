class Solution:
    def fib(self, N: int) -> int:
        l = [0, 1]
        for i in range(2, 31):
            l.append(l[i-1] + l[i-2])
        return l[N]

    def fib2(self, N: int) -> int:
        A = [0, 1]
        for i in range(N - 1):
            A.append(A[-1] + A[-2])
        return A[N]
