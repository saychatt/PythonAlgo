import heapq
from collections import deque, Counter
from typing import List


class HeapProblems:


    """
    You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
    Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
    The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
    Return the minimum number of CPU cycles required to complete all tasks.
    Example 1:
    Input: tasks = ["X","X","Y","Y"], n = 2
    Output: 5 Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

    Example 2:
    Input: tasks = ["A","A","A","B","C"], n = 3
    Output: 9
    Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

    """
    @staticmethod
    def leastInterval(tasks: List[str], n: int) -> int:

        time = 0
        # count the values of occurrence of each task: A-> 2, B -> 3
        occurrenceMap = Counter(tasks)
        maxHeap = []
        q = deque()

        # put them in max-heap to retrieve the highest occurring task
        for count in occurrenceMap.values():
            # no max heap, make the count negative
            maxHeap.append(-count)

        # rearrange the heap for max heap
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            # check if the max heap exists
            if maxHeap:
                # this is decrement as the numbers are -ve
                taskOccurrence = 1 + heapq.heappop(maxHeap)
                # if the occurrence is 0, then add it back to q for processing
                # add the time in which it can be processed.
                if taskOccurrence != 0:
                    q.append([taskOccurrence, time + n])
            #check in the q if the element in the head can be popped and
            # put back in the heap, if it's the suited time.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
