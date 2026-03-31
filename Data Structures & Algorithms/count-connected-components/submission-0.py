class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visited = set()
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)
            for value in adj[node]:
                if value in visited:
                    continue
                dfs(value)
            

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res