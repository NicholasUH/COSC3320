class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def is_cyclic_util(self, v, visited, rec_stack, in_cycle):
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True

            for i in self.adj[v]:
                if not visited[i] and self.is_cyclic_util(i, visited, rec_stack, in_cycle):
                    in_cycle[v] = True
                    return True
                elif rec_stack[i]:
                    in_cycle[v] = True
                    return True

        rec_stack[v] = False
        return False

    def count_satisfiable_nodes(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        in_cycle = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.is_cyclic_util(i, visited, rec_stack, in_cycle)

        count = self.V - sum(in_cycle)
        return count


# Example Input
n = int(input())
m = int(input())

g = Graph(n)

for _ in range(m):
    v, w = map(int, input().split())
    g.add_edge(v, w)

print(g.count_satisfiable_nodes())
