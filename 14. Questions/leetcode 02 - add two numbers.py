# add two numbers | leetcode 02 | https://leetcode.com/problems/add-two-numbers/
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains 
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        res = ListNode()  # Initialize a result linked list.
        head = res  # Create a reference to the head of the result linked list.
        carry = 0  # Initialize a variable to hold the carry.
        while l1 is not None or l2 is not None:
            # Determine the values of the current nodes and handle cases where one list is shorter than the other.
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            # Calculate the sum of the values from both linked lists along with the carry from the previous step.
            this_val = val1 + val2 + carry
            # Calculate the digit to add to the result linked list and update the carry for the next step.
            this_digit = this_val % 10
            carry = this_val // 10
            # Update the value of the current node in the result linked list.
            res.val = this_digit
            # Move to the next nodes in the input linked lists if they exist.
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            # If there are more digits to process, create a new node in the result linked list.
            if l1 is not None or l2 is not None:
                res.next = ListNode()
                res = res.next
        # If there is a carry left, create a new node to accommodate it.
        if carry > 0:
            res.next = ListNode(carry)
        return head  # Return the head of the result linked list.

