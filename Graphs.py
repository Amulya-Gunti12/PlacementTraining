#BFS Graph
def BFS(graph,start):
    visited=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in visited:
            print(n,end=" ")
            visited.add(n)
            q.extend(graph[n])
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
print("BFS Graph")
BFS(graph,'A')
print()

#DFS Graph
def DFS(graph,n,visited=set()):
    if n not in visited:
        print(n,end=" ")
        visited.add(n)
        for i in graph[n]:
            DFS(graph,i,visited)
            
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
print("DFS Graph")
DFS(graph,'A')
