class Solution:
    def majorityElement(self, nums):
        mc = len(nums) // 2
        for num in nums:
            cont = sum(1 for elem in nums if elem == num)
            if cont > mc:
                return num

    def setElement(self, nums):
        mc = len(nums) // 2
        numa = set(nums)
        for num in numa:
            if nums.count(num) > mc:
                return num

    def sortElement(self, nums):
        print(len(nums))
        nums.sort()
        print('排序数组', nums)
        return nums[len(nums) // 2]


a = Solution()
print(a.majorityElement([2, 3, 3, 2, 3]))
print(a.setElement([1,2,2,3,3,3]))
print(a.sortElement([1,2,2,3,3,3,4,4,4,4]))
