# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            head = None
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            n = head
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    n.next = list1
                    list1 = list1.next
                else:
                    n.next = list2
                    list2 = list2.next
                n = n.next
            if list1 != None:
                n.next = list1
                return head
            if list2 != None:
                n.next = list2
                return head

            


        