f = open("lifeguards.in", "r")
amount = int(f.readline())
raw_data = f.read()
def calculate_difference(raw_data):
  first_list = []
  second_list = []
  master_list = []
  for pair in raw_data.splitlines():
    first_digit = int(pair.split()[0])
    second_digit = int(pair.split()[1])
    first_list.append(first_digit)
    second_list.append(second_digit)
    master_list.append(first_list)
    master_list.append(second_list)
  return master_list
master_list = calculate_difference(raw_data)
first_list = master_list[1]
second_list = master_list[2]
solutions = []
first_perm = first_list.copy()
second_perm = second_list.copy()
for i in range(len(master_list[0])):
  first_list = first_perm.copy()
  second_list = second_perm.copy()
  first_list.pop(i)
  second_list.pop(i)
  max_2 = None
  max_2_index = None
  for z in range(len(first_list)):
    if max_2 == None:
      max_2 = first_list[z]
      max_2_index = z
    if first_list[z] > max_2:
      max_2 = first_list[z]
      max_2_index = z
  min_1 = None
  min_1_index = None
  for a in range(len(second_list)):
    if min_1 == None:
      min_1 = second_list[a]
      min_1_index = a
    if second_list[a] < min_1:
      min_1 = second_list[a]
      min_1_index = a
  if second_list[max_2_index] > first_list[min_1_index]:
    solution = max_2 - min_1
  else:
    solution = (first_list[max_2_index] - second_list[max_2_index]) - (second_list[min_1_index] - first_list[min_1_index])
  solutions.append(solution)
max_solution = None
for x in range(len(solutions)):
  if max_solution == None:
    max_solution = solutions[x]
  if solutions[x] > max_solution:
    max_solution = solutions[x]
try:
  s = open("lifeguards.out", "x")
  s.close()
except:
  print(max_solution)
s = open("lifeguards.out", "w")
s.write(str(max_solution))
s.close()
    
  
