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
print(arr[4])  # 50
# print(arr[5])  # list index out of range

# If an array has n elements:"First index = 0" & "Last index  = n - 1"

# Accessing the Last Element==> arr[-1]

print(arr[-1])

"""Index:    0    1    2    3    4
            -5   -4   -3   -2   -1
    Value:   10   20   30   40   50
"""

# Changing an Array Element:Arrays are mutable in Python
arr =[10, 20, 30, 40, 50]
arr[1] = 100 # [10, 100, 30, 40, 50]
# changed 20 =>100
print(arr)
arr[-5] = 70 # [70, 100, 30, 40, 50]
# changed 10 => 70
print(arr)

# Finding Array Length

print(len(arr))


# Difference: Index vs Value

arr = [15, 25, 35]

""" index 0 → value 15
    index 1 → value 25
    index 2 → value 35
"""
arr[1] == 25

print(arr[1])

# Basic Array Operations

arr = [11, 21, 31]
#Access
print(arr[1])

# Update
arr[0] = 45
print(arr) #[45, 21, 31]

# length
print(len(arr)) #3
# Add
arr.append(45)
print(arr)  #[45, 21, 31, 45]

# Problem 1
arr = [2, 3, 4, 5, 6, 7]
#First element
print(arr[0])#2
#Last element
print(arr[-1])#7
# Third element
print(arr[2])#4
# Length
print(len(arr))#6

"""
An array is a data structure that stores multiple elements in a sequence and allows access using an index.
What is the first index in Python?: 0
What does arr[3] mean?:Access the element stored at index 3.
What does arr[-1] mean in Python?:It accesses the last element.
"""

arr = [5, 10, 15, 20, 25]
print(arr[2])
print(arr[-1])
arr[3] = 100
print(arr)

print(len(arr))

arr = [10, 20, 30, 40, 50, 60]
length = len(arr)
print(length)
print(arr[length- 1])

#print(arr[len(arr) - 1])

"""
Array has n elements
        ↓
First index = 0
        ↓
Last index = n - 1
"""