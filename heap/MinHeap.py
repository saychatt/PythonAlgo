class MinHeap:

    def __init__(self):
        self.heap = [0]


    def push(self, val):
        self.heap.append(val)
        i = len(self.heap)-1

        #percolate up
        while self.heap[i] < self.heap[i // 2]:
            #swap with parent
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //=2

    def pop(self):
        i = len(self.heap) - 1
        if i == 0:
            return None
        if i == 1:
            return self.heap.pop()

        #take the first element
        result = self.heap[1]
        #swap with the last one to the head
        self.heap[1] = self.heap.pop()
        i = 1
        self.minHeapify(i)
        #return the head
        return result

    def minHeapify(self, i):
        # percolate down
        while 2 * i < len(self.heap):
            ## if there is a right node
            if ((2 * i + 1 < len(self.heap) and
                 #if the right child is smaller
                 self.heap[2 * i + 1] < self.heap[2 * i]) and
                    #if the element is smaller than the right child
                    self.heap[2 * i + 1] < self.heap[i]):
                # swap with right child, as the right child is the smallest
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                # swap with left child, since it's smaller
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break

    #heapify any array
    def minHeapifyArray(self, arr):
        arr.append(arr[0])
        self.heap = arr

        cur = (len(self.heap)-1) // 2

        while cur > 0:
            self.minHeapify(cur)
            cur -=1

        return self.heap[1:]





