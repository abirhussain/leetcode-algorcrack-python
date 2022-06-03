    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = ans = head
        cnt = 0
        while curr is not None:
            cnt = cnt + 1
            curr = curr.next
        mid = cnt//2
        while mid > 0:
            ans = ans.next
            mid = mid -1
        return ans
