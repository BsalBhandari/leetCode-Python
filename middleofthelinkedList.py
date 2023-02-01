class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head  
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

test = Solution()
print(test.middleNode([1, 2, 3, 4, 5, 6,7]))
'''
Output: 4
'''


