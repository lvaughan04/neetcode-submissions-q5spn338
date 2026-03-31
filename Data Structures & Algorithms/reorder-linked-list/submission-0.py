# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return
        ## first get to the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## now since we are in the middle we are going to reverse slow
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        ## now merge the two lists together
        ## slow is the reversed list but prev is the head of that list so we will use that value
        curr = head
        while curr and prev:
            tmpCurr = curr.next
            tmpReverse = prev.next
            curr.next = prev
            curr.next.next = tmpCurr
            curr = tmpCurr
            prev = tmpReverse
        if curr:
            curr.next = prev 
        