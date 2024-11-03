class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        self.edges.sort()
        parent = []
        rank = []
        mst = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for edge in self.edges:
            w, u, v = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append(edge)
                self.union(parent, rank, root_u, root_v)

            if len(mst) == self.V - 1:
                break

        print("Edges in the Minimum Spanning Tree:")
        for weight, u, v in mst:
            print(f"{u} -- {v} == {weight}")

g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
