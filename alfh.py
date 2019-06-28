import maze_maker
# 2���� �迭�� �̿��Ͽ� �̷��� ����� ���Ѵ�
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

maze_maker.show()           # �̷� ����ȭ�� ���δ�

# ��ư�� Ŭ���� ������ ��ٸ���

# 2�� �ݺ����� �̿��Ͽ� 2���� �迭�� �ִ� ������� �̷θ� �׸���
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
