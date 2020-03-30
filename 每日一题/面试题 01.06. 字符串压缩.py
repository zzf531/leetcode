class Solution(object):
    def compressString(self, S):
        K = S +'1'
        lenght = len(K) -1
        string = ''
        count = 1
        for i in range(lenght):
            if K[i] == K[i+1]:
                count += 1
            else:
                string += K[i] + str(count)
                count = 1
        return string if len(string) < len(S) else S


a = Solution()
print(a.compressString("abbccd"))