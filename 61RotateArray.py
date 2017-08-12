# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        l=ListNode(0)
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        if length==0:
            return 
        point=head
        for i in range(length-k%length-1):
            point=point.next
        
        l.next=point.next
        point.next=None
        
        start=l
        while start.next:
            start=start.next
        
        start.next=head
        l=l.next
        return l
        
        
            
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        