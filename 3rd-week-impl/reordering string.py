str_to_sort = input()
number_list = []
alphabet_list = []

for word in str_to_sort:
  if word.isdigit():
    number_list.append(int(word))
  else:
    alphabet_list.append(word)
alphabet_list.sort()

print("".join(alphabet_list) + str(sum(number_list)))