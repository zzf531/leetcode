class Solution(object):
    # 本题的思路就是先判断给定整数x的正负情况，把符号首先给提取出来
    # 然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数
    def reverse(self, x):
        # 定义用来标记给定整数x的正负情况，若x>=0， 则flag=1；反之，则flag=-1
        flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        # 将abs(x)变成字符串
        x_str = str(abs_x)
        # 将字符串x_str反转
        reverse_x_str = x_str[::-1]
        # 最后恢复成整数
        reverse_x_int = int(reverse_x_str) * flag
        aa = reverse_x_int if -2 ** 31 <= reverse_x_int <= 2**31 - 1 else 0
        return aa


a = Solution()
print(a.reverse(120))
