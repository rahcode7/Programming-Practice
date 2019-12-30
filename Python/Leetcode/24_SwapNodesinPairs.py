## Problem - https://leetcode.com/problems/swap-nodes-in-pairs/


## Create Linked List 

class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.headval = None 

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.next


## Insert List elements
l1 = LinkedList()
l1.headval = ListNode("1")
n2 = ListNode("2")
l1.headval.next = n2
n3 = ListNode("3")
n2.next = n3
n4 = ListNode("4")
n3.next = n4
n5 = ListNode("5")

#print(l1.headval)
print(l1.listprint())
#print(n2.val,n3.val,n4.val)


## Swap Linked list elements
class Solution:
    def swapPairs(head:ListNode) -> ListNode:
        singleListNode =head
        ListNode = head
        while singleListNode is not None:
             if singleListNode.next is None:
                    return(ListNode)
             temp = singleListNode.val
             nextListNode = singleListNode.next
             singleListNode.val = nextListNode.val 
             nextListNode.val = temp
             singleListNode = nextListNode.next
             print(singleListNode)
        return(ListNode)


Solution.swapPairs(l1.headval)
print(l1.listprint())