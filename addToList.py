def add_items_to_list(data, items=[]):
  items.extend(data)
  return items

my_list = [1, 2, 3]
result1 = add_items_to_list(my_list)  
print(result1) 

result2 = add_items_to_list([4, 5]) 
print(result2) 
