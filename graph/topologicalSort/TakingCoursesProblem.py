class Solution(object):

    """
    You are given an array prerequisites where prerequisites[i] = [a, b]
    indicates that you must take course b first if you want to take course a.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
    Return a valid ordering of courses you can take to finish all courses. If there are many valid answers,
    return any of them. If it's not possible to finish all courses, return an empty array.
    """
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

            result = []
            # initialize the adj list
            adjList = [[] for _ in range(numCourses)]
            # iterate over the dependencies
            for curr, pre in prerequisites:
                # [0 ,1] -> 0 points to 1 as pre
                adjList[curr].append(pre)

            # to keep a record of the cycle and visited.
            cycle, visited = set(), set()

            # define the dfs function inside so that it has access to the local variable
            def dfs(curr):
                # if the node is in cycle, then return False
                if curr in cycle:
                    return False
                # the node is already visited and not in cycle, then skip
                if curr in visited:
                    return True
                # add the node to cycle
                cycle.add(curr)
                # make a recursive call for it's adj nodes
                for adjNode in adjList[curr]:
                    if not dfs(adjNode):
                        return False
                        # remove from cycle
                cycle.remove(curr)
                # add as a successful visit
                visited.add(curr)
                # append to the result
                result.append(curr)

            for curr in range(numCourses):
                if dfs(curr) == False:
                    return []
            return result




