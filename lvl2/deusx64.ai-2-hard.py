

MAZE_X = 0x1c
MAZE_Y = 0xc

START_X = 0
START_Y = 0
GOAL_X  = MAZE_X - 1 
GOAL_Y  = MAZE_Y - 1

dst_x   = GOAL_X
dst_y   = GOAL_Y
cur_x   = START_X
cur_y   = START_Y

print (dst_x, dst_y, cur_x, cur_y)

maze = []
for i in range (0, MAZE_Y):
    maze.append ([' '] * (MAZE_X))

maze[START_Y][START_X] = 'o'
maze[GOAL_Y][GOAL_X] = '#'

footprint = []
for i in range (0, MAZE_Y):
    footprint.append ([' '] * (MAZE_X))

def check_point(x, y):
    if  y < 0 or \
        y == MAZE_Y or \
        x < 0 or \
        x == MAZE_X or \
        maze[y][x] == 'X' or footprint[y][x] == 'S':
        
        return False
    return True

def find_path (x, y, path):
    #if dst_x == x and dst_y == y:
    #    return True, path
    print (f'x:{x}, y:{y}, path:{path}') 
    if maze[y][x] == '#':
        print (f'target found at x:{x}, y:{y},\tpath:{path}')
        return True, path
    
    footprint[y][x] = 'S'
    #right shift
    if check_point(x + 1, y):
        r, t_path = find_path (x + 1, y, path+'R')
        if r:
            return r, t_path
    #down shift
    if check_point(x, y + 1):
        r, t_path = find_path (x, y + 1, path+'D')
        if r:
            return r, t_path
    #left shift
    if check_point(x - 1, y):
        r, t_path = find_path (x - 1, y, path+'L')
        if r:
            return r, t_path
       
    #up shift
    if check_point(x, y - 1):
        r, t_path = find_path (x, y - 1, path+'U')
        if r:
            return r, t_path
        
    
    return False, path


#реверс из ассемблера
def get_random_number(i):
    #print (f'init vector: {hex(i)}\tmul {hex( (i * 0x41c64e6d) & 0xffffffff)}')
    r = (i * 0x41c64e6d) & 0xffffffff
    #print (f'\tres {hex(r + 0x3039)}')
    return r + 0x3039
   

iv = 1677336406
#1677312334
#iv = 1677334334 
#1677224124
print ('input :', hex(iv))
get_random_number(iv)

#создание лабиринта
#реверс из ассемблера
#без проверки на проходимость лабиринта
for i in range (0,MAZE_X):
    iv = get_random_number(iv)
    for j in range(0, MAZE_Y):
        iv = get_random_number(iv)
        if (iv & 0x51) == 0x51:
            maze[j][i] = 'X'
                
for l in maze:
    print(l)
r, path = find_path(cur_x, cur_y, '')
print ( f'Result {r}, path: {path}')
