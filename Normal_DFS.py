import copy

def Normal_DFS(maxtrix, start, end):
    temp_maxtrix = copy.deepcopy(maxtrix)
    parent_save = copy.deepcopy(maxtrix)
    stack = [start] ## Tạo ngăn xếp và thêm nút gốc vào
    d = 0
    current=()
    while len(stack) != 0:
        d += 1
        current = stack.pop()
        temp_maxtrix[current[0]][current[1]] = 'v' ## Đánh dấu đã thăm đỉnh này
        
        if current == end:
            break
        ## Xét các vị trí lân cận
        arounds = [(current[0] - 1, current[1]), (current[0], current[1] - 1),
                   (current[0] + 1, current[1]), (current[0], current[1] + 1)]
        ## Nếu không tường và chưa thăm thì thêm vào ngăn xếp, và lưu lại nút tạo nên sự việc này
        for i in arounds:
            if (temp_maxtrix[i[0]][i[1]] != 'v' and maxtrix[i[0]][i[1]] != 'x'):
                parent_save[i[0]][i[1]] = current
                stack.append(i)
   
    ## Nếu không tìm được đường ra
    if current != end:
        with open ("dfs.txt","w+") as f:
            f.write("NO")
        return    
    route = [end]
    point = end
    while point != start:
        route.insert(0, parent_save[point[0]][point[1]])
        point = parent_save[point[0]][point[1]]

    cost = len(route)
    with open ("dfs.txt","w+") as f:
        f.write(str(cost))
    return route



