
def topologicalSort(n, edges):
   adjList = {}

   #initialize the adjacency list
   for i in range(n):
       adjList[i] = []
   for srcNode, destNode in edges:
       adjList[srcNode].append(destNode)

   visitedSet = set()
   cycle = set()
   orderOfNodes = []
   #local dfs function
   def dfs(node):
       #return no-ops if visited
       if node in visitedSet:
           return
       if node in cycle:
           raise ValueError('Cycle detected. Cannot be topologically sorted.')
       visitedSet.add(node)
       #add to cycle
       cycle.add(node)
       #recursive call for each of the neighbor
       for neighbor in adjList[node]:
           dfs(neighbor)
       #post-order function to add the node
       orderOfNodes.append(node)
       #remove from cycle
       cycle.remove(node)
   #run dfs for each node as we don't know the head.
   for head in adjList:
       dfs(head)
   #return the reverse order
   orderOfNodes.reverse()
   return orderOfNodes

if __name__ == "__main__":
    v = 6
    edgesList = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
    ans = topologicalSort(v, edgesList)
    print(ans)

