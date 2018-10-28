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

# ================= Area to code in  ===================
# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    data_node = DoublyLinkedListNode(data)
    if head.data >= data_node.data:
        data_node.next = head
        head.prev = data_node
        head = data_node
        return head
    currNode = head
    prevNode = currNode.prev 
    while currNode != None:
        if currNode.data >= data_node.data:
            data_node.next,data_node.prev  = currNode, prevNode
            prevNode.next = data_node
            currNode.prev = data_node
            break 
        prevNode = currNode
        currNode = currNode.next
    else:
        prevNode.next = data_node
        data_node.prev = prevNode 
    return head


#====================End Of the area ==================

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
