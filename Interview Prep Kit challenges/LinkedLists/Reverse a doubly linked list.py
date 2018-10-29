#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# ================ CODE HERE =================
# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    reversedLList = DoublyLinkedList()
    currNode = head
    while currNode is not None:
        tempNode = DoublyLinkedListNode(currNode.data)
        insertToReversed(reversedLList, tempNode)
        currNode = currNode.next
    return reversedLList.head
def insertToReversed(LList,Node):
    if LList.tail is None:
        LList.tail = Node
    else: 
        LList.head.prev = Node
        Node.next = LList.head 
    LList.head = Node

    
# =================================
if __name__ == '__main__':
    # UNCOMMENT COMMENTED CODE TO GET THE ORIGINAL FROM HACKERRANK
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        # print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')

    # fptr.close()
