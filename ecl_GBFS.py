import copy
import math

def DinhKe(x,y): #(x = m: dòng, y = n: cột)
    a = []
    if(x-1 >= 0):
        a.append((x-1,y))
    else:
        a.append((x+1,y))
    a.append((x+1,y))
    if(y - 1 >= 0):
        a.append((x,y-1))
    else:
        a.append((x,y+1))
    a.append((x,y+1))
    return a # a=[trên, dưới, trái phải]

def ecl_GBFS(matrix, h_matrix, start, end):

    duyet_Mat = copy.deepcopy(matrix) #Ma trận duyệt toàn bản đồ
    F = copy.deepcopy(matrix) #Ma trận danh sách liên kế, lưu vị trí của điểm trước khi đến nó
    

    duyet_Mat[start[0]][start[1]] = '@'
    prio_Q = [start] #Lập hàng đợi ưu tiên
    cost = 0

    while len(prio_Q) != 0:
        
        cost += 1
        cur = prio_Q.pop(0)
        duyet_Mat[cur[0]][cur[1]] = '@'

        if cur == end:
            break

        dinh_Ke = DinhKe(cur[0], cur[1])

        for i in range(len(dinh_Ke)):
            if (duyet_Mat[dinh_Ke[i][0]][dinh_Ke[i][1]] != 'x') and (duyet_Mat[dinh_Ke[i][0]][dinh_Ke[i][1]] != '@'):
                F[dinh_Ke[i][0]][dinh_Ke[i][1]] = cur
                j = 0
                while j < len(prio_Q):
                    if h_matrix[dinh_Ke[i][0]][dinh_Ke[i][1]] < h_matrix[prio_Q[j][0]][prio_Q[j][1]]:
                        break
                    j += 1
                prio_Q.insert(j, dinh_Ke[i])

    route = [end]
    curPoint = end
    while curPoint != start:
        route.insert(0, F[curPoint[0]][curPoint[1]])
        curPoint = F[curPoint[0]][curPoint[1]]

    print('Chi phi thuc hien ecl_GBFS: ', cost,' vong lap')
    return route



import os
import matplotlib.pyplot as plt


with open('maze_map2.txt', 'w') as outfile:
  outfile.write('0\n')
  outfile.write('xx xxxxxxxxxxxxxxxxxxx\n')
  outfile.write('x  x    x  xx        x\n')
  outfile.write('x  x x      x   x    x\n')
  outfile.write('x    x  x   x   x    x\n')
  outfile.write('x    x  x   x   x    x\n')
  outfile.write('xx x    x   x   x    x\n')
  outfile.write('x       x   x   x    x\n')
  outfile.write('x xxxxxxx   x   x    x\n')
  outfile.write('x  x    x   x   x    x\n')
  outfile.write('xx   x          x  S x\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx')


def visualize_maze(matrix, bonus, start, end, route=None):
    """
    #Args:
    #  1. matrix: The matrix read from the input file,
    #  2. bonus: The array of bonus points,
    #  3. start, end: The starting and ending points,
    #  4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    
"""
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

def read_file(file_name: str = 'maze.txt'):
  f=open(file_name,'r')
  n_bonus_points = int(next(f)[:-1])
  bonus_points = []
  for i in range(n_bonus_points):
    x, y, reward = map(int, next(f)[:-1].split(' '))
    bonus_points.append((x, y, reward))

  text=f.read()
  matrix=[list(i) for i in text.splitlines()]
  f.close()

  return bonus_points, matrix




bonus_points, matrix = read_file('maze_map1.txt')

print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)
                
        else:
            pass

visualize_maze(matrix,bonus_points,start,end)

def euclid_Heuristic_Funct (X,Y): #X,Y: tọa độ 2 điểm trên không gian 2 chiều (bản đồ)
    dist = 0
    for i in range(len(X)):
        dist += pow(Y[i] - X[i],2)
    dist = math.sqrt(dist)
    
    return dist

def heuristic_Matrix (matrix, des): #matrix: ma trận 2 chiều (bản đồ) đọc từ file, des: điểm thoát exit cần tìm
    heu_Matrix = []
    new = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new.append(0)
        heu_Matrix.append(new)
        new=[]
    for i in range(len(heu_Matrix)):
        for j in range (len(heu_Matrix[0])):
            heu_Matrix[i][j] = euclid_Heuristic_Funct((i,j), des)
    return heu_Matrix #Ma trận gồm các giá trị hàm heuristic để ước lượng khoảng cách từ điểm có tọa độ bất kì trên bản đồ đến điểm thoát exit


#Test
h_matrix = heuristic_Matrix(matrix, end)
route = ecl_GBFS(matrix,h_matrix,start,end)

visualize_maze(matrix,bonus_points,start,end,route)