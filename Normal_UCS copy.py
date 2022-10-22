from read_file import read_file, pulp
import matplotlib.pyplot as plt
from GBFS import visualize_maze as vm



str='Normal_BFS.txt'
file=read_file(str)
matrix=file[1]


def Normal_UCS(matrix):
    # This function find the route from start to end of matrix
    # return route, cost
    # algorithm uses the visited array to mark each point whether visited or not
    # the same as BFS because the cost of actions is equal
    cols=len(matrix[0])
    rows = len (matrix)
    print(cols, rows)
    #print("matrix", matrix[1][0])
    visited = [[0 for i in range(cols)] for j in range(rows)]
    route=[]
    cost=0
    queue=[]
    start=pulp(matrix)[0]
    end=pulp(matrix)[1]
    print("start",start, end)
    print("start i", start[0])
    route.append(start)
    visited[start[0]][start[1]]=1
    queue.append(start)
    while queue!=[]:
        s=queue.pop(0)
        print(s, end=" ")
        adj_vertex=[(s[0], s[1] + 1),(s[0], s[1] -1 ),(s[0]+1, s[1] ),(s[0] -1, s[1] )]
        print("adj vertex:", adj_vertex)
        for i in adj_vertex:
            if i==end:
                route.append(end)
                queue=[]
                break
            if visited[i[0]][i[1]]==0 and matrix[i[0]][i[1]]==' ':    
                queue.append(i)
                visited[i[0]][i[1]]=1
                route.append(i)
    return start, end, route


bonus=[]
start, end, route=Normal_UCS(matrix)
print (matrix[0][1] is 'x')
vm(matrix, bonus, start, end, route)
