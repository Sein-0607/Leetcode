# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        root = node

        if list1 is None or list2 is None:
            return list1 or list2

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
    
        node.next = list1 or list2
        
        return root.next
        # node = ListNode()
        # root = node

        # if list1 is None and list2 is None:
        #     return None

        # while list1 is not None and list2 is not None:
        #     if list1.val < list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
            
        #     node = node.next
    
        # return root