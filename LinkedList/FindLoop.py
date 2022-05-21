
"""
Write a function that takes in the head of a singly linked list that contains a loop
The function should return the node from which the loop originates.
If a Linked List has loop, then the tail points to a node in the list instead of None/NULL
"""

class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# O(n) time | O(n) space
def findLoop1(head):
    # Write your code here.
    lookup = {}
    temp = head
    while temp.next != None and id(temp.next) not in lookup:
        lookup[id(temp)] = 1
        temp = temp.next
    return temp.next


# O(n) time | O(1) space --> Optimized solution
def findLoop2(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
