import heapq
from typing import List


class GraphPathProblems:

    """
        https://neetcode.io/problems/network-delay-time/question
        You are given a network of n directed nodes, labeled from 1 to n.
        You are also given times, a list of directed edges where times[i] = (ui, vi, ti).
            ui is the source node (an integer from 1 to n)
            vi is the target node (an integer from 1 to n)
            ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
        You are also given an integer k, representing the node that we will send a signal from.

        Return the minimum time it takes for all of the n nodes to receive the signal.
        If it is impossible for all the nodes to receive the signal, return -1 instead.

        Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
        Output: 3

        Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
        Output: -1
    """

    @staticmethod
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #this is Dijkstra's algorithm.
        # returns map[node] -> time
        time = 0

        # times[i] = (ui, vi, ti) i.e. time is the weight of the edge
        # initialize the adjacency list
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = []
        for source, destination, time in times:
            adjList[source].append([destination, time])

        # put a min heap to extract the min time for each node
        # the time is the pivot value for the min heap
        minHeapByTime = [[0, k]]
        visit = set()

        while minHeapByTime:
            # pop the node with min time from the heap
            time1, node1 = heapq.heappop(minHeapByTime)

            # if the result already contains the shortest time ignore else add
            if node1 in visit:
                continue
            visit.add(node1)
            # as you are traversing the graph, the last time will be the last node
            time = time1

            # explore all the adjacent nodes of node1 and put them in the heap
            for node2, time2 in adjList[node1]:
                heapq.heappush(minHeapByTime, [time1 + time2, node2])

        # return the nodes with the shortest time
        return time if len(visit) == n else -1