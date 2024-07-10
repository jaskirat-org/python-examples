def selection_sort(data):
  for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:  
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data


def merge_sort(data):
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])  
  right = merge_sort(data[mid:]) 
  return left + right  

data = [5, 2, 8, 1, 3]
sorted_data = merge_sort(data)
print(sorted_data) 
