from tempfile import tempdir

from list.single.Node import Node


class SinglyLinkedList(object):
    def __init__(self, node = None):
        self.head = node
        self.length = 0

    def getLength(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    #insert the node at first
    def insertAtFirst(self, val):
        newNode = Node()
        newNode.setData(val)
        #check if empty
        if self.head is None:
            self.head = newNode
        else: #make the new node point to current node and make it head
            newNode.next = self.head
            self.head = newNode
        return self.head

    #print the node values
    def printNodeVal(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    #get the node at the current point
    def getNodeAt(self, param):
        current = self.head
        count = 0
        while current is not None:
            if count == param:
                return current
            else:
                count += 1
                current = current.next
        if current is None:
            raise Exception("Node not found")

    #insert value at the last
    def insertAtLast(self, val):
        newNode = Node()
        newNode.setData(val)
        # check if empty
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def removeNodeAt(self, index):
        #check for the exception conditions
        if index < 0:
            raise IndexError("Index must be greater than or equal to 0")
        if self.head is None:
            raise Exception("List is empty")

        #initialize the pointer positions
        currentNode = self.head
        previousNode = None

        #if the removal is the first node of the list
        if index == 0:
            self.head = self.head.next
            return
        currentPosition = 0

        #remove the node from the index
        while currentPosition < index and currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        #check if the index is out of bounds
        if index > currentPosition:
            raise IndexError("Index out of range")
        #arrange make the new attachment
        previousNode.next = currentNode.next
        #dislodge the current node
        currentNode.next = None

    def getKthLastNode(self, k):
        if k < 0 or k > self.getLength():
            raise IndexError("k must be greater than or equal to 0 or less than length")
        kthNode = self.head
        for _ in range(0, self.getLength() - k):
            kthNode = kthNode.next
        return kthNode

        # 2 pointer approach
        # take the leading node to kth position
        # for _ in range(1,k):
        #     leadingNode = leadingNode.next
        # #if the list was of single length then return the 1st node
        # if leadingNode is None:
        #     return kthNode
        # while leadingNode.next is not None:
        #     kthNode = kthNode.next
        #     leadingNode = leadingNode.next
        # return kthNode

    def reverseKNodes(self, k):
        dummy = Node(0, self.head)
        #one node before the group
        groupPrev = dummy
        headSet = False

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            #reverse the group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp  = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            #set the head first time
            if not headSet:
                self.head = kth
                headSet = True
            groupPrev = tmp

    def merge2SortedLists(self, list2):
        dummy = Node(0, None)
        tail = dummy
        l1, l2 = self.head, list2.head
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        self.head = dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

















