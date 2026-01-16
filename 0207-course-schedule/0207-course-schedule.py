class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        
        self.adj = [[] for _ in range(n)]
        for i,j in pre:
            self.adj[i].append(j)

        self.vis = [0]*n
        for i in range(n):
            if self.vis[i] == 0:
                if self.dfs(i):
                    return False
        return True

    def dfs(self, u):
        self.vis[u] = 2

        for v in self.adj[u]:
            if self.vis[v] == 2: #cycle formed
                return True

            if self.vis[v] == 0 and self.dfs(v):
                return True

        self.vis[u] = 1
        return False
        #0->1
        #0->1->0