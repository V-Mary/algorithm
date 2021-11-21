class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, start_vertex, end_vertex, weight):
        self.graph.append([start_vertex, end_vertex, weight])

    def check(self, nodes, i):
        if nodes[i] == i:
            return i
        return self.check(nodes, nodes[i])

    def notice_node(self, nodes, rank, x, y):
        xroot = self.check(nodes, x)
        yroot = self.check(nodes, y)
        if rank[xroot] < rank[yroot]:
            nodes[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            nodes[yroot] = xroot
        else:
            nodes[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        nodes = []
        rank = []
        for node in range(self.V):
            nodes.append(node)
            rank.append(0)
        while e < self.V - 1:
            start_vertex, end_vertex, weight = self.graph[i]
            i = i + 1
            print("start_vertex, end_vertex",start_vertex, end_vertex)

            x = self.check(nodes, start_vertex)
            y = self.check(nodes, end_vertex)
            print("x,y:",x, y)
            if x != y:
                e = e + 1
                result.append([start_vertex, end_vertex, weight])
                self.notice_node(nodes, rank, x, y)

        for start_vertex, end_vertex, weight in result:
            print("Edge:", start_vertex, end_vertex,end=" ")
            print("-", weight)


g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 6)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 13)
g.add_edge(3, 4, 8)
g.kruskal()