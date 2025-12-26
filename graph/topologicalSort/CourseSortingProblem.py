from typing import List


class CourseSortingProblem:
    def findCourseOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        #create the adjacency list : course -> [dependency1, dependency2]
        preReq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        #sets to check if already visited and detect cycles
        visited, cycle= set(), set()

        #do dfs call for each node
        def dfs(crs):
            # if the node is in cycle return false
            if crs in cycle:
                return False
            # if the node is already processed/visited return true
            if crs in visited:
                return True
            # if the node is not cycle and not visited
            cycle.add(crs)
            for pre in preReq[crs]:
                #if a cycle was detected
                if dfs(pre) == False:
                    return False
                #remove from the cycle
                cycle.remove(crs)
                #add to the visited for skipping processing
                visited.add(crs)
                #append to output as the course path
                output.append(crs)
                return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output






        return output
