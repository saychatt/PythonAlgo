from list.single.SinglyLinkedList import SinglyLinkedList

import unittest

class TestSinglyLinkedList(unittest.TestCase):

    def testLengthOfSinglyLinkedList(self):
        myList = SinglyLinkedList()
        self.assertEqual(0, myList.getLength())
        for i in [1,2,3,4,5]:
            myList.insertAtFirst(i)
        self.assertEqual( 5, myList.getLength())

    def testGetNodeAt(self):
        myList = SinglyLinkedList()
        #test with empty list
        with self.assertRaises(Exception):
            myList.getNodeAt(0)
        for i in [1, 2, 3, 4, 5]:
            myList.insertAtLast(i)
        #test the end
        self.assertEqual(5, myList.getNodeAt(4).getData())
        #test the beginning
        self.assertEqual(1, myList.getNodeAt(0).getData())
        #test the end
        self.assertEqual(3, myList.getNodeAt(2).getData())
        #test out of bounds
        with self.assertRaises(Exception):
            myList.getNodeAt(5)

    def testListOrder(self):
        myList = SinglyLinkedList()
        for i in [1,2,3,4,5]:
            myList.insertAtFirst(i)
        k = 0
        for i in [5,4,3,2,1]:
            currNode = myList.getNodeAt(k)
            k = k+1
            self.assertEqual(currNode.getData(), i)

    def testInsertAtFirst(self):
        myList = SinglyLinkedList()
        myList.insertAtFirst(1)
        self.assertEqual(1, myList.getNodeAt(0).getData())
        myList.insertAtFirst(2)
        self.assertEqual(2, myList.getNodeAt(0).getData())

    def testInsertAtLast(self):
        myList = SinglyLinkedList()
        myList.insertAtLast(1)
        self.assertEqual(1, myList.getNodeAt(0).getData())
        myList.insertAtLast(2)
        self.assertEqual(2, myList.getNodeAt(1).getData())

    def testRemovalWhenEmptyOrNegative(self):
        myList = SinglyLinkedList()
        #throws exception when there is nothing to remove
        with self.assertRaises(Exception):
            myList.removeNodeAt(0)
        with self.assertRaises(IndexError):
            myList.removeNodeAt(-1)

    def testRemovalFromFirstNode(self):
        myList = SinglyLinkedList()
        #init the list
        for i in [1,2,3,4,5]:
            myList.insertAtLast(i)
        #remove the node from first
        myList.removeNodeAt(0)
        #check the whole list
        for i in [2, 3, 4, 5]:
            self.assertEqual(i, myList.getNodeAt(i-2).getData())

    def testRemovalFromMiddle(self):
        myList = SinglyLinkedList()
        # init the list
        for i in [1, 2, 3, 3, 4]:
            myList.insertAtLast(i)

        #check remove node from the middle
        myList.removeNodeAt(2)
        for i in [1, 2, 3, 4]:
            self.assertEqual(i, myList.getNodeAt(i-1).getData())

        #check remove node from the last
        myList.removeNodeAt(3)
        for i in [1, 2, 3]:
            self.assertEqual(i, myList.getNodeAt(i-1).getData())

    def testRemovalOutOfIndex(self):
        myList = SinglyLinkedList()
        # init the list
        for i in [1, 2, 3, 4]:
            myList.insertAtLast(i)
        with self.assertRaises(IndexError):
            myList.removeNodeAt(4)

    #write a program to get kth last element in the list
    # example if 62, 42, 13, 666 getKthLastElement(2) is 13
    # Input: 1 -> 2 -> 3 -> 4, N = 3
    # Output: 2
    # Explanation: Node 2 is the third node from the end of the linked list.
    # Input: 35 -> 15 -> 4 -> 20, N = 4
    # Output: 35
    # Explanation: Node 35 is the fourth node from the end of the linked list.
    def testGetKthLastNode(self):
        myList = SinglyLinkedList()
        for i in [1,2,3,4,5,6]:
            myList.insertAtLast(i)
        self.assertEqual(4, myList.getKthLastNode(3).getData())
        self.assertEqual(5, myList.getKthLastNode(2).getData())
        self.assertEqual(1, myList.getKthLastNode(6).getData())
        #test for out of range
        self.assertRaises(IndexError, myList.getKthLastNode, 7)

        #test for 1 element
        myList = SinglyLinkedList()
        myList.insertAtLast(1)
        self.assertEqual(1, myList.getKthLastNode(1).getData())

    def testKthNodeRevers(self):
        myList = SinglyLinkedList()
        for i in [1,2,3,4,5,6,7,8]:
            myList.insertAtLast(i)
        myList.reverseKNodes(3)
        k = 0
        for i in [3,2,1,6,5,4,7,8]:
            currNode = myList.getNodeAt(k)
            k += 1
            self.assertEqual(currNode.getData(), i)

    def testMergeSortedList(self):
        myList1 = SinglyLinkedList()
        for i in [1,2,4]:
            myList1.insertAtLast(i)

        myList2 = SinglyLinkedList()
        for i in [1, 3, 5]:
            myList2.insertAtLast(i)

        myList1.merge2SortedLists(myList2)
        k=0
        for i in [1,1,2,3,4,5]:
            currNode = myList1.getNodeAt(k)
            k += 1
            self.assertEqual(currNode.getData(), i)
