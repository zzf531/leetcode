from ListNode.List_node_Base import ListNode, generateList, printList

class Solution:
    # 遍历两遍

    def method3(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        start = pre
        end = pre

        while n:
            start = start.next
            n -= 1
        while start.next != None:
            start = start.next
            end = end.next
            print('+++', start.val, end.val)

        end.next = end.next.next
        print('___', start.val, end.val)
        return pre.next


if __name__ == '__main__':
    head = generateList([1, 2, 3, 4, 5, 6, 7])
    a = Solution()
    head2 = a.method1(head, 3)
    printList(head2)

'''
方法二: 使用双指针
由于头节点有可能被删除,故设置 pre 指针指向 head
设置快慢指针 前后指针 start, end, 指向 pre. 先让 end 走 n 步, 再将 start 和 end 一起移动.当 end.next 为 None时, 也就是 end 到了尾节点时, start 真好走到待删除节点的前一个节点.
此时 让 start.next = start.next.next, 即可删除 倒数第 n 个节点. 返回 pre.next 即可. 此处不返回 head 是因为 head 可能被删除.

作者：wd6
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-di-n-ge-jie-dian-pythonliang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
