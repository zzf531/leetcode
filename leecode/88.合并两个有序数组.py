class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        new_nums1 = nums1[:m]
        new_nums2 = nums2[:n]
        return sorted(new_nums1 + new_nums2)

    def merge2(self, nums1, m: int, nums2, n: int):
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1[:]


a = Solution()
print(a.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(a.merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
