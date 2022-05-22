"""
Write a function that reverses the Linked List
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    p1 = head
    p2 = None
    while p1.next != None:
        nextNode = p1.next
        p1.next = p2
        p2 = p1
        p1 = nextNode
    p1.next = p2
    head = p1
    return head
