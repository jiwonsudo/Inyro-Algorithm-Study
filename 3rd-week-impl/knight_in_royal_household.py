alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
possable_moves = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
res = 0

input_list = input()
cur_x = input_list[0]
cur_y = int(input_list[1])

for word in alphabets:
  if cur_x == word:
    cur_x = alphabets.index(word) + 1
    break

for move in possable_moves:
  tem_x = cur_x + move[0]
  tem_y = cur_y + move[1]
  if (tem_x >= 1 and tem_x <= 8) and (tem_y >= 1 and tem_y <= 8):
    res += 1

print(res)