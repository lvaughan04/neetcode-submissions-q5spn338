class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        ## essentially the approach i would use is to build out the graph and run a dfs to go through the nodes
        ## once i reach a node add it to a visited set, and if i ever visit a node twice then i return false
        visited = set()

        adjList = [[] for i in range(n)]
        for u , v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, prevVal):
            visited.add(node)
            for neighbors in adjList[node]:
                if neighbors == prevVal:
                    continue
                if neighbors in visited:
                    return False
                dfs(neighbors, node) 
            return True
        
        res = dfs(0, 0) 
        return res and len(visited) == n
        
