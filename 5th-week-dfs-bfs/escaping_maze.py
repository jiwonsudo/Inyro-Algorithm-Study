from collections import deque
import sys

def solve_maze(list_of_maze: list):
  queue = deque()
  queue.append((0, 0)) # 초기 위치 (0, 0)
  while queue:
    row, col = queue.popleft()
    for i in range(4): # 4방향 위치 확인
      cur_row = row + moves_of_row[i]
      cur_col = col + moves_of_col[i]
      if 0 > cur_row or cur_row >= num_of_row or 0 > cur_col or cur_col >= num_of_col: continue
      if list_of_maze[cur_row][cur_col] == 0: continue
      # 해당 노드 첫 방문 시
      if list_of_maze[cur_row][cur_col] == 1:
        list_of_maze[cur_row][cur_col] = list_of_maze[row][col] + 1
        queue.append((cur_row, cur_col))
  return list_of_maze[num_of_row - 1][num_of_col - 1]

num_of_row, num_of_col = map(int, sys.stdin.readline().split())
locations = [list(map(int, sys.stdin.readline().strip())) for _ in range(num_of_row)]

# 이동 방향 (상, 하, 좌, 우)
moves_of_row: list[int] = [0, 0, -1, 1]
moves_of_col: list[int] = [1, -1, 0, 0]

print(solve_maze(locations))