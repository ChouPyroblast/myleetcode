# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        node1=l1
        node2=l2
        node3 = ListNode(0)
        current_node=ListNode(0)
        current_node.next=node3
        while True:
            if node1 is None and node2 is None and not c:
                current_node.next = None
                break
            current_node=current_node.next
            sum = 0
            if node1 is not None:
                sum += node1.val
                node1=node1.next
            if node2 is not None:
                sum += node2.val
                node2=node2.next
            sum += c
            if sum >=10:
                c =1
                sum -= 10
            else:
                c=0
            current_node.val=sum
            next_node=ListNode(0)
            current_node.next=next_node
            
            
        return node3
            
