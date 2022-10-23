import copy

def Normal_DFS(matrix, start, end):
    temp_maxtrix = copy.deepcopy(matrix)
    parent_save = copy.deepcopy(matrix)
    stack = [start]
    d = 0
    
    while len(stack) != 0:
        d += 1
        current = stack.pop()
        temp_maxtrix[current[0]][current[1]] = 'v'
        
        if current == end:
            break

        arounds = [(current[0] - 1, current[1]), (current[0], current[1] - 1),
                   (current[0] + 1, current[1]), (current[0], current[1] + 1)]

        for i in arounds:
            if (temp_maxtrix[i[0]][i[1]] != 'v' and maxtrix[i[0]][i[1]] != 'x'):
                parent_save[i[0]][i[1]] = current
                stack.append(i)
        
    route = [end]
    point = end
    while point != start:
        route.insert(0, parent_save[point[0]][point[1]])
        point = parent_save[point[0]][point[1]]

    return route, d



