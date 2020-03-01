def hammingDistance(x, y):
    # return bin(x ^ y).count('1')
    a = x ^ y
    count = 0
    while a:
        # if a & 1:
        #     count += 1
        # a = a >> 1
        count += 1  # 布赖恩·克尼根算法
        a = a & (a-1)
    return count


print(hammingDistance(4, 6))
