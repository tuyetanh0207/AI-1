
import math
from read_file import read_file, pulp


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

def min_Node_In_Neibor(heu_matrix, matrix, cur):
    dinhke = DinhKe(cur[0],cur[1])
    min = heu_matrix[cur[0]][cur[1]]
    pos = cur
    for i in range(len(dinhke)):
        if ((matrix[dinhke[i][0]][dinhke[i][1]] == 'X')  or  (matrix[dinhke[i][0]][dinhke[i][1]] == 'x')):
            pass
        else:
            if (heu_matrix[dinhke[i][0]][dinhke[i][1]] < min) :
                if (heu_matrix[dinhke[i][0]][dinhke[i][1]] >= 0):
                    min = heu_matrix[dinhke[i][0]][dinhke[i][1]]
                    pos = dinhke[i]
    return pos

def greedBestFirstSearch(matrix, beg, end):

    route = [] #Mảng đường đi
    open_Queue = [] #queue duyệt và so sánh heuristic các đỉnh 
    close_Queue = [] #queue đỉnh đã duyệt
    
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

    while True:
        

# Trường hợp kết thúc        
        #Nếu tạo độ hiện tại bằng tọa độ đích thì kết thúc
        if(cur == end):
            return [route,cost]
            break
        
        cost += 1
        dinhke_end = DinhKe(end[0],end[1])
# Trường hợp kết thúc        
        #Nếu tọa độ đích bị bịt kín thì kết thúc
        if(((matrix[dinhke_end[0][0]][dinhke_end[0][1]] =='x') and (matrix[dinhke_end[1][0]][dinhke_end[1][1]] =='x') and (matrix[dinhke_end[2][0]][dinhke_end[2][1]] == 'x') and (matrix[dinhke_end[3][0]][dinhke_end[3][1]] == 'x')) or(
        (matrix[dinhke_end[0][0]][dinhke_end[0][1]] =='x') and (matrix[dinhke_end[1][0]][dinhke_end[1][1]] =='x') and (matrix[dinhke_end[2][0]][dinhke_end[2][1]] =='x') and (matrix[dinhke_end[3][0]][dinhke_end[3][1]] == 'x'))):
            print ('Khong co duong di den diem dich (diem exit bi bi kin)')
            return [route,cost]




        #Trả về 4 tọa độ kề với tọa độ hiện tại
        dinhke = DinhKe(cur[0],cur[1])

       
        

        count = start
        #Đi qua các tọa kề của tọa độ hiên tại (đang xét, đã mở)
        for i in range(len(dinhke)):
            #Nếu tọa độ xét là biên/ đã xét rồi thì  thêm tọa độ kề đó vào Queue đóng: đã xét rồi
            #Ngược lại thêm tọa độ kề đó vào Queue đóng: đã xét rồi => Nếu có giá trị heuristic nhỏ nhất => Thêm vào route đường đi
            if ((matrix[dinhke[i][0]][dinhke[i][1]] == 'X') or (matrix[dinhke[i][0]][dinhke[i][1]] == 'x')):
                close_Queue.append(dinhke[i])
            elif (check_Close_Node (close_Queue, dinhke[i]) == False):
                close_Queue.append(dinhke[i])
                if ((dinhke[i] == min_Node_In_Neibor(heu_matrix, matrix, cur)) and (count == 0)):
                    route.append(dinhke[i])
                    count += 1
            else:
                pass

            
        
        #Tìm giá trị heuristic nhỏ nhất trong các đỉnh kề thỏa điều kiện di chuyển => set tọa độ cur = tọa độ mang giá trị đó
        next = min_Node_In_Neibor(heu_matrix, matrix, cur)
        cur = next

# Trường hợp kết thúc
        #Nếu giá trị heuristic của các tọa độ kề luôn âm thì kết thúc
        if(heu_matrix[cur[0]][cur[1]] < 0):
            print('Khong co duong di toi diem dich (diem bat dau bi bit kin)')
            return [[],0]





# 
# Code của thầy + test

import os
import matplotlib.pyplot as plt




with open('maze_map.txt', 'w') as outfile:
  outfile.write('2\n')
  outfile.write('3 6 -3\n')
  outfile.write('5 14 -1\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
  outfile.write('x   x   xx xx        x\n')
  outfile.write('x     x     xxxxxxxxxx\n')
  outfile.write('x x   +xx  xxxx xxx xx\n')
  outfile.write('  x   x x xx   xxxx  x\n')
  outfile.write('x          xx +xx  x x\n')
  outfile.write('xxxxxxx x      xx  x x\n')
  outfile.write('xxxxxxxxx  x x  xx   x\n')
  outfile.write('x          x x Sx x  x\n')
  outfile.write('xxxxx x  x x x     x x\n')
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


str='maze_map.txt'
file=read_file(str)
matrix=file[1]
bonus_points=file[0]
start=pulp(matrix)[0]
end=pulp(matrix)[1]
print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')

print ("matrix",matrix)


#Test

route, cost = greedBestFirstSearch(matrix,start,end)
print(route, cost)

visualize_maze(matrix,bonus_points,start,end,route)




        
    
