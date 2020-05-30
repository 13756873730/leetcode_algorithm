class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        pre = None
        while head is not None:
            head_next = head.next
            head.next = pre
            pre = head
            head = head_next
        return pre


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    result = Solution().reverseList(head)
    while result is not None:
        print(result.val)
        result = result.next
    print(result)
    pass
