from read_file import read_file, pulp
import matplotlib.pyplot as plt
import copy
from drawmap import visualize_maze as vm



str='map01.txt'
file=read_file(str)
matrix=file[1]


def Normal_BFS(matrix):
    # This function find the route from start to end of matrix
    # return route, cost
    # algorithm uses the visited array to mark each point whether visited or not
    
    cols=len(matrix[0])
    rows = len (matrix)
    #print("matrix", matrix[1][0])
    visited = copy.deepcopy(matrix)
    parent = [[None for i in range(cols)] for j in range(rows)]
    route=[]
    cost=0
    n_loop=0
    queue=[]
    start=pulp(matrix)[0]
    end=pulp(matrix)[1]
    route.append(start)
    visited[start[0]][start[1]]=1
    queue.append(start)
    #print("visited", visited)
    while queue!=[]:
        s=queue.pop(0)
        if s==end:
            cost+=1
            break
        adj_vertex=[(s[0], s[1] + 1),(s[0], s[1] -1 ),(s[0]+1, s[1] ),(s[0] -1, s[1] )]
        flag=0
        for i in adj_vertex:
            if visited[i[0]][i[1]]==' ':    
                queue.append(i)
                visited[i[0]][i[1]]='#'
                parent[i[0]][i[1]]=s
                n_loop+=1
                flag=1
        

    if s!=end:
        print('Khong co duong di')
        return 0,None,None,None,None,None
    route=[end]
    vertex=end
    while vertex!=start:
        route.insert(0, parent[vertex[0]][vertex[1]])
        vertex=parent[vertex[0]][vertex[1]]
    cost=len(route)
    return 1, start, end, route, cost, n_loop


bonus=[]
check, start, end, route, cost, n_loop=Normal_BFS(matrix)
Normal_BFS(matrix)
print("cost: ", cost)
print("nloop:", n_loop)
vm(matrix, bonus, start, end, route)
