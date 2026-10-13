# An array is a data structure used to store multiple values in a sequence.

num = [10, 20, 30, 40, 50, 60]
"""
Index:     0    1    2    3    4
           ↓    ↓    ↓    ↓    ↓
         ┌────┬────┬────┬────┬────┐
Value:   │ 10 │ 20 │ 30 │ 40 │ 50 │
         └────┴────┴────┴────┴────┘
"""
# The index tells us the position of an element.
print(num)

# Indexing: Python uses zero-based indexing.
# That means the first element is at index 0.

arr = [10, 20, 30, 40, 50]

print(arr[0])  # 10
print(arr[1])  # 20
print(arr[2])  # 30
print(arr[3])  # 40