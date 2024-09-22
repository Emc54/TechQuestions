"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self == 0:
            return "" 
        return f"val = {self.next} {self.val}"

def addTwoNumbers(
    l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:

    lout = ListNode(0)
    current = lout

    carry = False
    while l1 or l2:

        val1 = val2 = 0
        if l1:
            val1 = l1.val
        if l2:
            val2 = l2.val

        local_sum = val1 + val2 + 1 if carry else val1 + val2
        carry=False

        if local_sum >= 10:
            local_sum %= 10
            carry = True

        current.next = ListNode(local_sum)
        current = current.next

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
     
    if carry:
        current.next = ListNode(1)
    return lout.next


l1 = ListNode(2, next=ListNode(4,next=ListNode(3)))
l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))

print(addTwoNumbers(l1,l2))
print(l1)
 
