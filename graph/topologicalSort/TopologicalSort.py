
def constructAdjList(V, edges):
    adjList = [ [] for i in range(V)]
    for it in edges:
        adjList[it[0]].append(it[1])
    return adjList


def topologicalSortUtil(v, adjList, visited, stack):
    visited[v] = True;
    #go to the adjacent vertexes
    for it in adjList[v]:
        if not visited[it]:
            topologicalSortUtil(it, adjList, visited, stack)
    #push it in the stack
    stack.append(v)


def topologicalSort(V, edges):
    # define the stack
    stack = []
    visited = [False] * V

    adjList = constructAdjList(V, edges)
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adjList, visited, stack)
    # return the reversed stack
    return stack[::-1]


if __name__ == "__main__":
    v = 6
    edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

    ans = topologicalSort(v, edges)

    print(" ".join(map(str, ans)))
