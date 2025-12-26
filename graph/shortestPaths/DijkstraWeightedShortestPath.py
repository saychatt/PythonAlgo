import heapq


class DijkstraWeightedShortestPath:

    """
        https://neetcode.io/courses/advanced-algorithms/14
        # Given a connected graph represented by a list of edges, where
        # edge[0] = src, edge[1] = dst, and edge[2] = weight,
        # find the shortest path from src to every other node in the
        # graph. There are n nodes in the graph.
        # O(E * logV), O(E * logE) is also correct.
    """
    @staticmethod
    def shortestPath(edges, n, src):

        #initialize the adjacency list
        adjList = {}
        for  i in range (1, n+1):
            adjList[i] = []
        for source, dest, weight in edges:
            adjList[source].append([dest, weight])

        #list of shortest path from source
        shortestPathMap = {}

        #initialize the min heap
        minHeap = [[0, src]]

        while minHeap:
            #pop the min cost node
            weight1, node1 = heapq.heappop(minHeap)

            #add this candidate if not already present in the shortestPathList
            if node1 in shortestPathMap:
                continue
            shortestPathMap[node1] = weight1

            #find all the adjacent nodes and add them to the min heap
            #note: you have to add the previous weight from the source
            for node2, weight2 in adjList[node1]:
                heapq.heappush(minHeap, [weight1 + weight2, node2])

        return shortestPathMap

