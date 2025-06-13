ans[]
visited=[0]*len(adj)
q=[]
start=0
if(visited[start]==0):
    visited[start]=1
    q.append(start)
    while(len(q)>0):
        popElement=q.pop(0)
        for i in adj[popElement]:
            if(visited[i]==0):
                visited[i]=1
                q.append(i)
        ans.append(popElement)]
        
return ans