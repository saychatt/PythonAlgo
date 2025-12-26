import heapq
from typing import List


class KClosestPointsFromOrigin:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxHeap, (dist, x, y))
            if len(maxHeap) > k:
                #pop the max value if the k length exceeds after push
                heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            result.append([x,y])

        return result