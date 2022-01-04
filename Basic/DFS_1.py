def DFS(graph, start, visited):
  visited[start] = True
  print(start, end=' ')
  
  for i in graph[start]:
    if not visited[i]:
      DFS(graph, i, visited)


graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

DFS(graph, 1, visited)
