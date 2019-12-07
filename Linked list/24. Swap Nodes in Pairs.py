"""
使用递归来解决该题，递归三部曲：
（1）终止条件：当递归到链表为空或者链表只剩一个元素；
（2）返回值：返回给上一层递归的值是已经交换完后的子链表；
（3）单次过程：假设待交换的俩节点分别为head和next，相当于是一个含三个节点的链表交换前两个节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second






