nodes,edges=7,6
links=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
adjMat=[]
for i in range(nodes):
    temp=[0]*nodes
    adjMat.append(temp)
for n,m in links:
    adjMat[n][m]=1
    adjMat[m][n]=1
print(adjMat)