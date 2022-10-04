from collections import deque

col, row = map(int,(input().split(' ')))
borad = []
cnt = 0
dx = []
for _ in range(col) :
    borad.append(list(map(int, input().split(' '))))

def bfs(x, y):
    if x == row :
        bfs(0,y+1)
    if y == col :
        return 0;
    while 
