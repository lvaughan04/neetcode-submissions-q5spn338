class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## build the adjancency list
        adj = [[] for _ in range(numCourses)]
        for a , b in prerequisites:
            adj[a].append(b)
        
        visited, path = set(), set()
        res = []

        def dfs(node):
            ## cycle tracking algorithm
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            visited.add(node)
            res.append(node)
            return True


        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res