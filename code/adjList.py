adjList=[]
for i in range(v):
    adjList.append([])
for n,m in edges:
    adjList[n].append(m)
    adjList[m].append(n)
return adjList