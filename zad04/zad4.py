def prim(graph):
    n=len(graph)
    visited=[False]*n
    mst=[]
    start_vertex=0
    visited[start_vertex]=True

    while len(mst) < n-1:
        min_weight=float("inf")
        u,v=-1,-1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j]!=0 and graph[i][j] < min_weight:
                        min_weight=graph[i][j]
                        u=i
                        v=j
        
        if u!=-1 and v!=-1:
            mst.append((u,v,min_weight))
            visited[v]=True
    return mst
        

if __name__=="__main__":
    graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
    ]
    mst = prim(graph)
    total_weight = sum(weight for _, _, weight in mst)

    print(f"Minimalne drzewo rozpinające: {mst}")
    for u, v, weight in mst:
        print(f"{u} -- {v} : {weight}")
    print(f"Całkowita waga: {total_weight}")
    