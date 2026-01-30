from collections import deque

R,C = 5,5

m = [
    ['S','.','.','#','.'],
    ['#','#','.','#','.'],
    ['.','.','.','.','.'],
    ['.','#','#','#','E'],
    ['.','.','.','.','.']
]

sr, sc = 0,0
rq,cq = deque(), deque()

move_count = 0
Bnodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False

visited = [[False for _ in range(C)] for _ in range(R)]

dr = [-1,+1,0,0]
dc = [0,0,+1,-1]

parents = [[None for _ in range(C)] for _ in range(R)]

def explore_neighbous(r,c):
    global nodes_in_next_layer
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if rr < 0 or cc < 0 or rr>=R or cc>=C:
            continue
        if visited[rr][cc] or m[rr][cc]=='#':
            continue

        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True

        parents[rr][cc] = (r,c)
        nodes_in_next_layer += 1

def solve():
    global move_count, Bnodes_left_in_layer, nodes_in_next_layer, reached_end

    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    while rq:
        r = rq.popleft()
        c = cq.popleft()

        if m[r][c] == 'E':
            reached_end = True
            break

        explore_neighbous(r,c)
        Bnodes_left_in_layer -= 1

        if Bnodes_left_in_layer == 0:
            Bnodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count, (r,c)
    
    return -1, None

def reconstruct_path(end_r, end_c):
    r,c = end_r, end_c

    while(r,c) != (sr,sc):
        m[r][c] = "▅"
        r,c = parents[r][c]

    m[sr][sc] = 'S'
    m[end_r][end_c] = 'E'


result, end_pos = solve()

if result != -1:
    reconstruct_path(*end_pos)

print("Matrix with the shortest path:")
for row in m:
    print(" ".join(row))
print("\nShortest path length", result)
