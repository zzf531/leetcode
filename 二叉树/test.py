
def twoSum(nums, target):
	a = len(nums)
	print(a)
	for i in range(0, a):
		for j in range(i+1, a):
			if nums[j] + nums[i] == target:
				return[i,j]


print(twoSum([3,2,4], 5))
