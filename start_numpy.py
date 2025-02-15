import numpy as np

# n1 = np.array([12,2,5,6])

# print(type(n1))

# zeros_arr = np.zeros([3,3,3])

# [
#     [[], [], []], [[], [], []], [[], [], []]
# ]

# print(zeros_arr)

# scalar_mat = np.eye(4)
# print(scalar_mat)

# arr = np.full([3,3], '56')
# print(arr)

# arr = np.linspace(0, 11, 10)
# print(arr)

# nd_arr_with_range = np.arange(10, 21, 2)
# print(nd_arr_with_range)

# random_values = np.random.rand(3,2, 3)

# print(random_values)

# rand_n_values = np.random.randn(2,3)
# print(rand_n_values)

# rand_int_value = np.random.randint(1, 10, 10)
# print(rand_int_value)

# array = np.random.rand(5, 2) 
# print(array)


# Q5: Find all the combination in the list satisfying some
#     condition.
# a = [3,66, 32, 63, 72, 22 , 435]
# condition = num % 3 == 0

# n1 = np.random.rand()
# print(n1)

li = [2,3,5]
li2 = [ 
    [1,2,3], [4,5,65], [32, 43, 4]
]   # => shape ==> 3 X 3, 3 by 3

li3 = [
    [[1,2], [3,4], [5,3]], 
    [[1,2], [3,4], [5,3]], 
    [[1,2], [3,4], [5,3]]
]


# print(li3)
# shape => 3 X 3 X 2

# n1 = np.random.rand(3,3, 2)
# shape -> 3 X 3 X 2. at rool level how many elements in each list -> 2
# print(n1[0][0])
# n1[0][0] = 5
# print(n1)

# n2 = np.random.randn(5)
# print(n2)

n3 = np.random.randint(50, size=100) # => [0, 50) -> int-> 0, 1, 2
print(n3)