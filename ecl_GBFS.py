
from calendar import c
import math

def swap (a,b):
    temp = a
    a = b
    b = temp

def sort (close_Queue, heu_Matrix):
    for i in range(len(close_Queue)):
        for j in range(i,len(close_Queue),1):
            if



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



def check_Close_Node (close_Queue, node):
    for i in range(len(close_Queue)):
        if (node == close_Queue[i]):
            return True
    return False

'''def check_Baned_Node (ban_Queue, node):
    for i in range(len(ban_Queue)):
        if (node == ban_Queue[i]):
            return True
    return False'''

def min_Node_In_Neibor(heu_matrix, matrix, cur, close_Queue):
    dinhke = DinhKe(cur[0],cur[1])
    min = 0
    pos = []
   
    for i in range(len(dinhke)):
        if(heu_matrix[dinhke[i][0]][dinhke[i][1]] >= 0) and check_Close_Node(close_Queue,dinhke[i]) == False:
            min = heu_matrix[dinhke[i][0]][dinhke[i][1]]
            pos = dinhke[i]
            break
    for i in range(len(dinhke)):
        if ((matrix[dinhke[i][0]][dinhke[i][1]] == 'X')  or  (matrix[dinhke[i][0]][dinhke[i][1]] == 'x') or check_Close_Node(close_Queue,dinhke[i]) == True):
           pass
        else:
            if (heu_matrix[dinhke[i][0]][dinhke[i][1]] < min) :
                if (heu_matrix[dinhke[i][0]][dinhke[i][1]] >= 0):
                    min = heu_matrix[dinhke[i][0]][dinhke[i][1]]
                    pos = dinhke[i]
        
           

    return pos

def greedBestFirstSearch(matrix, beg, end):

    flag_hint = [] #cờ này bật khi bị bí đường => yêu cầu quay lui: 0: chưa duyệt, 3->1 đã duyệt và còn đường, -1 đã duyệt và không còn đường đi/ không thể đi tiếp
    route = [] #Mảng đường đi
    open_Queue = [] #queue duyệt và so sánh heuristic các đỉnh 
    close_Queue = [] #queue đỉnh đã duyệt
    ban_Queue = [] #queue cấm
    

    new = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new.append(0)
        flag_hint.append(new)
        new=[]
    #open_Queue.append(beg): bị thừa
    #close_Queue.append(beg)

    cost = 0 #Chi phí đường đi
    heu_matrix = heuristic_Matrix(matrix,end)
    #heuristic_val = heuristic_Matrix(matrix, end)[beg] #thiết lập giá trị heuristic tại điểm bắt đầu
    

    #Tinh chỉnh lại bản đô
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if ((matrix[i][j]=='X') or  (matrix[i][j]=='x')):
                    heu_matrix[i][j] = -1 


    cur = beg
     #Thêm tọa độ hiện tại vào queue đóng: xác định là đã xét rồi và không bao giờ xét (mở) nữa
    close_Queue.append(cur)
    route.append(cur)
    a = 0
    while True:
        a+=1
        if a == 10000:
            pass
        
        # Trường hợp kết thúc        
        #Nếu tạo độ hiện tại bằng tọa độ đích thì kết thúc
    
        if(cur == end):
            return [route,cost]
            break
        
        cost += 1
        
        
        #Trả về 4 tọa độ kề với tọa độ hiện tại
        dinhke = DinhKe(cur[0],cur[1])

        count = 0
        c_way = 0

     
        sum = 0
        for i in range(len(dinhke)):
                
            if (matrix[dinhke[i][0]][dinhke[i][1]] == 'X') or (matrix[dinhke[i][0]][dinhke[i][1]] == 'x')  or check_Close_Node (close_Queue, dinhke[i]) == True:
               pass
            else:
                sum +=1
        flag_hint[cur[0]][cur[1]] = sum

        if flag_hint[cur[0]][cur[1]] == 0:
            while flag_hint[route[len(route)-1][0]][route[len(route)-1][1]] == 0:
                route.pop()
                cur = route[len(route)-1]

        for i in range(len(dinhke)):
            
            #Nếu tọa độ xét là biên/ đã xét rồi thì  thêm tọa độ kề đó vào Queue đóng: đã xét rồi
            #Ngược lại thêm tọa độ kề đó vào Queue đóng: đã xét rồi => Nếu có giá trị heuristic nhỏ nhất => Thêm vào route đường đi
            if ((matrix[dinhke[i][0]][dinhke[i][1]] == 'X') or (matrix[dinhke[i][0]][dinhke[i][1]] == 'x')):
                #flag_hint[dinhke[i][0]][dinhke[i][1]] -= 1
                pass
            else:
                if (check_Close_Node (close_Queue, dinhke[i]) == False):
                    if ((dinhke[i] == min_Node_In_Neibor(heu_matrix, matrix, cur, close_Queue)) and (count == 0)):
                        close_Queue.append(dinhke[i])
                        route.append(dinhke[i])
                        cur = dinhke[i]
                        count += 1
          
           
            
        '''if c_way >= 3: #Xung quanh hết đường đi => quay lui
            close_Queue.append(cur)
            route.pop()
            cur = route[len(route)-1]
        else:
        #Tìm giá trị heuristic nhỏ nhất trong các đỉnh kề thỏa điều kiện di chuyển => set tọa độ cur = tọa độ mang giá trị đó
            next = min_Node_In_Neibor(heu_matrix, matrix, cur, close_Queue)
            cur = next'''


def min_heu_value_of_route(heu_matrix, route):
    kq = []
    for i in range(len(route)):
        kq.append(route, heu_matrix[route[i][0]][route[i][1]])
    return kq





# 
# Code của thầy + test

import os
import matplotlib.pyplot as plt


with open('maze_map1.txt', 'w') as outfile:
  outfile.write('0\n')
  outfile.write('xx xxxxxxxxxxxxxxxxxxx\n')
  outfile.write('x       xx xx        x\n')
  outfile.write('x                    x\n')
  outfile.write('xx              xxxxxx\n')
  outfile.write('x                    x\n')
  outfile.write('x  x          xxx  xxx\n')
  outfile.write('xxxxx              x x\n')
  outfile.write('xxxxxxxxx    xxxxx   x\n')
  outfile.write('x          xxx S     x\n')
  outfile.write('xxxxx x x          x x\n')
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


#Test

route, cost = greedBestFirstSearch(matrix,start,end)
print(route, cost)

visualize_maze(matrix,bonus_points,start,end,route)


