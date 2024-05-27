graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set()

def bfs(graph, root):
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend(list(set(graph[vertex]) - visited))

# Driver Code
print("\nBreadth-First Search:")
bfs(graph, 'A')

print("\nBreadth-First Search starting from node B:")
bfs(graph, 'B')
