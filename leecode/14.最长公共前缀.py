'''
输入: ["flower","flow","flight"]
输出: "fl
'''

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        # aa = min(strs, key=len) 求list中长度最小
        if not strs: return ""
        sum = 0
        xyz = zip(*strs)
        for i in xyz:
            if len(set(i)) > 1:
                break
            sum += 1
        return strs[0][:sum]
a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
