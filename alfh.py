import maze_maker
# 2차원 배열을 이용하여 미로의 모양을 정한다
path = [
        [0, 9, 9, 9, 9, 0, 0, 0, 0, 0],
        [0, 9, 9, 9, 9, 0, 9, 9, 9, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
        [9, 0, 9, 0, 9, 0, 9, 9, 9, 9],
        [9, 0, 9, 0, 9, 0, 0, 0, 0, 9],
        [9, 0, 9, 0, 9, 9, 9, 9, 0, 9],
        [9, 0, 9, 0, 9, 9, 9, 9, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 9, 0]
    ]

maze_maker.show()           # 미로 가상화면 보인다

# 버튼이 클릭될 때까지 기다린다

# 2중 반복문을 이용하여 2차원 배열에 있는 정보대로 미로를 그린다
for y in range(8):
    for x in range(10):
        maze_maker.set_cell_type(x, y, path[y][x])
def findway(x,y,way):
    if (x < 0) : return
    if (x > 9) : return
    if (y < 0) : return
    if (y > 7) : return
    if path[y][x] != 0: return
    path[y][x] = 1
    if (x ==9 ) and (y == 7):
        print('find',way)
        return
    
    findway(x-1, y, way + ("(%d,%d)" % (x,y)) )
    findway(x+1, y, way + ("(%d,%d)" % (x,y)) )
    findway(x, y-1, way + ("(%d,%d)" % (x,y)) )
    findway(x, y+1, way + ("(%d,%d)" % (x,y)) )
    

findway(0,0, "")
