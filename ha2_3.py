
INF = int(1e9 + 7)

def floyd_warshall(dist,length):
    #initialize next whose entries point to the next vertex in the shortest path
    next = [[-1]*length for val in range(length)]

    for i in range(length): 
        for j in range(length):
            if dist[i][j] != INF:
                next[i][j] = j #at first set value of entry to the destination node, meaning shortest path = direct path

    #update dist and next if path through other intermediate nodes is shorter than the original direct path
    for k in range(length):
        for i in range(length):
            for j in range(length): 
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k] #meaning shortest path from i to j is through k
    return next,dist

def construct_path(u,v): #take in source and destination nodes
    path = [u]
    while u != v:
        u = next_pointer[u][v]
        path.append(u) #keep adding the next vertex via next_pointer
    return path

if __name__ == '__main__':
    dist = [[0,3,INF,7],
            [8,0,2,INF],
            [5,INF,0,1],
            [2,INF,INF,0]]
    
    length = len(dist)

    next_pointer,distance = floyd_warshall(dist,length)
    print('Vertices on v1-v3 shortest path is',construct_path(1,3),', total distance is',distance[1][3])
    print('Vertices on v0-v2 shortest path is',construct_path(0,2),', total distance is',distance[0][2])