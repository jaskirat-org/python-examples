# Complex code with bad practices

class DataManager:
  """Data manager class with bad practices (spaghetti code)"""

  def __init__(self):
    self.data = []  # Unclear data structure

  def add_data(self, item):
    """Adds data to the manager (appends without validation)"""
    self.data.append(item)

  def get_data_by_index(self, index):
    """Gets data by index (error-prone if index is out of bounds)"""
    try:
      return self.data[index]
    except IndexError:
      return None  # Silent error handling

  def get_data_by_value(self, value):
    """Gets data by value (inefficient linear search)"""
    for item in self.data:
      if item == value:
        return item
    return None

  def process_data(self):
    """Processes data (unclear logic and potential side effects)"""
    for item in self.data:
      if isinstance(item, str):
        item.upper()  # Modifying data in-place (potential side effects)
      elif isinstance(item, list):
        item.sort()  # Modifying data in-place (potential side effects)

# Usage with bad practices
data_manager = DataManager()
data_manager.add_data(10)
data_manager.add_data("hello")
data_manager.add_data([2, 5, 1])

# Error-prone access (index out of bounds)
print(data_manager.get_data_by_index(10))  # May return None silently

# Inefficient search
print(data_manager.get_data_by_value(2))

# Unclear data processing (modifies data in-place)
data_manager.process_data()

# Potential side effects after processing
print(data_manager.data)  # Data may be modified (uppercase string, sorted list)
