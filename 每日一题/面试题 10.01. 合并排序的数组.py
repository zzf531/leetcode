class Solution(object):
    def merge(self, A, m, B, n):
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] > B[pb]:
                sorted.append(B[pb])
                pb += 1
            else:
                sorted.append(A[pa])
                pa += 1
        A[:] = sorted




print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))

class Solution2(object):
    def merge(self, A, m, B, n):
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted.append(A[pa])
                pa += 1
            else:
                sorted.append(B[pb])
                pb += 1
        A[:] = sorted