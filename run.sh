from importlib import import_module
import math
from references import read_file,visualize_maze
from Normal_DFS import Normal_DFS
from Normal_BFS import Normal_BFS
from ecl_GBFS import heuristic_Matrix,ecl_GBFS
from ecl_A_Star import heuristic_Matrix,ecl_A_Star
from man_GBFS import manhattan_Heuristic_Funct, man_GBFS
from man_A_Star import manhattan_Heuristic_Funct, man_A_Star

bonus_points, matrix = read_file('map01.txt')


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)
bonus_points, matrix = read_file('map01.txt')


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)
route=[]
if type == 1:
    route = Normal_DFS(matrix, start, end)
        
if type == 2:
    start, end, route = Normal_BFS(matrix)
    
if type == 3:
    start, end, route=Normal_UCS(matrix)

if type == 4:
    h_matrix = heuristic_Matrix(matrix, end)
    route = ecl_GBFS(matrix, h_matrix, start, end)

if type == 5:
    h_matrix = heuristic_Matrix(matrix, end)
    route = ecl_A_Star(matrix,h_matrix,start,end)

if type == 6:
    h_matrix = heuristic_Matrix(matrix, end)
    route = man_GBFS(matrix,h_matrix,start,end)

if type == 7:
    h_matrix = heuristic_Matrix(matrix, end)
    route = man_A_Star(matrix,h_matrix,start,end)

visualize_maze(matrix, bonus_points, start, end, route)