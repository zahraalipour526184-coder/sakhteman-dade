from collections import deque

class Graph:
    def init(self, n, directed=False):                  #گراف با ماتریس مجاورت
        self.n = n
        self.directed = directed
        self.M = [[0]*n for _ in range(n)]

    def insert_edge(self, s, t):
        self.M[s][t] = 1
        if not self.directed:
            self.M[t][s] = 1

    def show(self):
        print("ماتریس مجاورت:")
        for row in self.M:
            print(" ".join(map(str, row)))

    def dfs(self, start, visited=None):
        if visited is None:
            visited = [False]*self.n
        visited[start] = True
        print(start, end=" ")
        for ne in range(self.n):
            if self.M[start][ne] and not visited[ne]:
                self.dfs(ne, visited)

    def bfs(self, start):
        visited = [False]*self.n
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            print(v, end=" ")
            for ne in range(self.n):
                if self.M[v][ne] and not visited[ne]:
                    visited[ne] = True
                    queue.append(ne)


class GraphList:                                   #گراف با لیست مجاورت
    def init(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def insert_edge(self, s, t):
        self.adj[s].append(t)
        if not self.directed:
            self.adj[t].append(s)

    def show(self):
        print("لیست مجاورت:")
        for i, neighbors in enumerate(self.adj):
            print(f"{i}: {neighbors}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for ne in self.adj[start]:
            if ne not in visited:
                self.dfs(ne, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            v = queue.popleft()
            if v not in visited:
                print(v, end=" ")
                visited.add(v)
                queue.extend(self.adj[v])