import sys

def check_surrounding(list_to_search: list, row: int, col: int) -> bool:
  max_row, max_col = len(list_to_search), len(list_to_search[0])
  if list_to_search[row][col] == 0: # 현재 칸이 미방문 칸인 경우
    list_to_search[row][col] = 1 # 현재 칸 방문 처리
    if row + 1 < max_row: check_surrounding(list_to_search, row + 1, col)
    if row - 1 >= 0: check_surrounding(list_to_search, row - 1, col)
    if col + 1 < max_col: check_surrounding(list_to_search, row, col + 1)
    if col - 1 >= 0: check_surrounding(list_to_search, row, col - 1)
    return True
  return False

num_of_row, num_of_col = map(int, sys.stdin.readline().split())
locations: list = [list(map(int, sys.stdin.readline().strip())) for _ in range(num_of_row)]
counter: int = 0

for row in range(num_of_row):
  for col in range(num_of_col):
    if check_surrounding(locations, row, col): counter += 1
print(counter)