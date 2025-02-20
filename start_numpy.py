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

n1 = np.random.rand(3,3, 2) # --> 3 * 3 * 2 = 18
# shape -> 3 X 3 X 2. at rool level how many elements in each list -> 2
# print(n1[0][0])
# n1[0][0] = 5
# print(n1)

# n2 = np.random.randn(5)
# print(n2)

n3 = np.random.randint(50, size=100) # => [0, 50) -> int-> 0, 1, 2
# print(n3)

# print(n1)
 
# eg -> (3 X 3 X 2) = 18 ==reshape==> (4 X 9) = 9

# n_arr = np.array([1,2,3,5,6,7,87,88, 23])
# n_arr2 = np.arange(5, 20)

# print(n_arr.shape)

# print(type(n_arr2))
# print(n_arr2)

# a = n_arr2.reshape(3, 5)
# print(n_arr2)
# print(a)

# n_arr.reshape(3, 3)

# print(n_arr)
# print(n_arr.shape)


# n1 = np.random.rand(3, 2)
# n2 = np.random.rand(2,3)

# tup = (n1, n2)
# # print(tup)
# print(n1)
# print(n2)

# # n3 = np.vstack(tup)
""" number of columns must be equal of both nd_arrays vstack """
# # print(n3)

# n4 = np.hstack(tup)
""" number of rows must be equal of both nd_arrays in hstack """
# print(n4)

n1 = np.arange(1,5)
n2 = np.arange(2, 6)

# print(np.column_stack((n1, n2))) 
""" ===> if n1 & n2 are 2-D arrays then 
 column_stack will work just like hstack funciton."""


#  VSTACK
n1 = np.array([
    [1,2,3], 
    [34,5,64]
    ])
n2 = np.array([
    [1,2,3], 
    [34,5,64],
    [65, 22, 21]
    ])

"""
[
    [1,2,3], 
    [34,5,64],
    [1,2,3], 
    [34,5,64],
    [65, 22, 21]
]

"""
# np.vstack((n1, n2))

# one_d_arr = np.array([1,2,3])
# two_d_arr = np.array([
#     [4,5,22],
#     [23, 63, 24]
# ])

# print(two_d_arr.shape)

# merged_arr = np.vstack((one_d_arr, two_d_arr))
# print(merged_arr)


# a = '4'
# print(type(a))
# a = int(a)

# print(type(a))
nd_arr = np.array(['4.4', '6.7', '8.6', '2.4456'])

# print(nd_arr)
# li = [] 
# for item in nd_arr:
#     li.append(float(item))

# nd_arr_f = np.array(li)

# nd_arr_f = nd_arr.astype(float)
# print(nd_arr_f)


# 6th 
# rand
# randn(shape) --> it generated the values with Gausian distribution --> mean ~ 0 & variance 1
# randint
# mat = np.random.randn(5,6)
# # mat = np.random.rand(5,6) 
# """
# rand:
# Create an array of the given shape and populate it with random samples from a
# uniform distribution over [0, 1).
# """
# mean = sum(sum(mat)) / 30 
# variance = np.var(mat)

# print(mean, " ", variance)

# 9 -> laplace distribution

# numpy.random.laplace(loc=0.0, scale=1.0, size=None)
# lap_dist = np.random.laplace(loc=8.9,scale=1.5, size=35)
# mn = sum(lap_dist)/35
# print(lap_dist)
# print(mn)



# uniformly distributed
uni_data = np.random.uniform(1, 15, 10)
print(uni_data)