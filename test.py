

# name = "Vishal I\"m surname"

# description = ''' This is me I'm from India
# more writen text
# '''

# print(name)

# print(description)


name = "vishal surnamek"
n = len(name)
# print(n)
# length of string = 6 -> so last characrter will be at index 5
# print(name[2])
# print(name[5])

# print(name[n-2])

# print(name[-2])

# print(name[ : 4])

# print(name[-5 : -2]) 



# start = -5, end = -2 -> -2 - 1 = -3

name = "vishal surname"
# STEPPING
# print(name[0 : 6 : 1])


# print(name)
first_name = "mishal"
last_name = "surname"

full_name = first_name + ' ' + last_name
# print(full_name)


# name[0]  = 'm' --> will throw an error: as string are immutable

# print(name)


# print('mis' in first_name)

# print(first_name.upper())
# print(first_name.capitalize())



# print even numbers from 1 to 100

i = 1

# while i <= 100:
#     if(i % 2 == 0):
#         print(i)
#     i = i+1




# age = 45
# name = 'Anything'

# print("name is: ", name, "and age is: ", age)

# print(f'name is: {name} and age is: {age}')


# i = 2
# while i <= 10:
#     j = 100
#     # print(i)
#     i = i+1
    

# for i in range(1, 5):
#     print(i)

# age = 32
# if True:
#     age = 34
#     print(age)

# print(name)


# x = 300
# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)


li = [35, 76, 345, 23, 2, 4]

# li[0] = li[0] * 2
# li[1] = li[1] * 2
# li[2] = li[2] * 2
# li[3] = li[3] * 2
# li[4] = li[4] * 2

# i = 0
# while i < 5:
#     li[i] = li[i] * 2
#     i = i+1

# a = 5
# a = a + 10
# for v in range(0, 5):
#     li[v] = li[v] * 2
# print(li)


items = [ 1, 2, 4, 'laptop', 'charger', [ 'pen', 'paper', 'lunch' ] ]

# print(items[5][0 : 2])

# items.append(4.5)
# returned = items.pop()
# print(returned)
# items.reverse()

# items.insert(4,'phone')

# li.sort(reverse=True)

# items.remove('laptop')
# print(items)

items.remove(items[4])
# print(items)

# print(li)


# 1. to count positive and negative numbers in a list
li = [4, 5, 6, -2, 0,  -34, 56, 24, -43]

# for loop part & counters management:
# positive_counter = 0
# negative_counter = 0
# n = len(li)

# for i in range(0, n):
#     if li[i] > 0:
#         positive_counter += 1
#     elif li[i] < 0:
#         negative_counter += 1
#     else:
#         pass

# print("+ve count: ", positive_counter)
# print("-ve count: ", negative_counter)


# +ve elements count: 5
# -ve elements count: 3



# 2. Get a count of unique values from a list
# li = [1, 2, 4, 5, 4, 5, 32, 56, 32, 75, 123, 5]
# # unique no: 1, 2, 56, 75, 123
# ans_li = list(set(li))
# print(ans_li)
# print(len(ans_li))

# SETS
st = {1, 2, 1} # -> {1, 2}


st2 = { 4, 5, 6, 1, 2}
# print(st2.union(st))
# print(st.intersection(st2))
# st.add('pan')
# st.update(['pencil', 'park'])
# print(st)

# st.remove('park')
# print(st)




# 3. Maximum and minimum element’s position in a list
li = [45, 23, 2, 44, 3, 6, 76]

n = len(li)

maxIndex = 0
minIndex = 0

for i in range(0, n):
    if li[i] < li[minIndex]:
        minIndex = i
    
    if li[i] > li[maxIndex]:
        maxIndex = i


print("min: ", minIndex + 1)
print("max: ", maxIndex + 1)


# TUPLE

# tup = (3, 53, 52, 21, 22)
# print(tup[3])
# tup[0] = 5   --> It will throw an ERROR🚀. Because tuples are immutable.

# print(tup)
# len(tup)

# tup2 = (1,2,3)
# tup3 = tup2 + tup 
# print(tup3)

# print(len(tup2*5)) 
"""--> n- size of tuple and 
k is constant you are multiplying TUPLE with 
then size of new tuple will be: n*k """

# LIST_NAME.FUNCTION_NAME()
# FUNCTION_NAME(TUPLE_NAME)

# print(min(tup))
# print(max(tup))

# TRUE => 1, FALSE -> 0
# 0 => FALSE, NON_ZERO ->  (-inf, 0) U (0, inf)  => TRUE


# sorted_tup = sorted(tup)
# print(sorted_tup)

# ANY 

# age = 21
# gender =  'male'
# country = 'India'

# base_condition_for_job = ( age > 18, gender == 'male', country != "Pakistan" )
# # round 1
# if all(base_condition_for_job):
#     print("shortlisted")
# else:
#     print('sorry better luck next time.')


# technical round
# techincal = True
# if all(base_condition_for_job) and techincal:
#     print('selected')
# else:
#     print('not selected')


# ALL -> and operator 


# FUNCTIONS:
# SYNTAX: def FUNCTION_NAME(PARAMETERS SEPERATED BY COMMA(,)):
            #block of function

# FUNCTION DECLARATION
def greeting():
    pass

# FUNCTION DEFINITION
def greeting(name):
    # BLOCK OF FUNCTION
    print("Hello ", name)

# FUNCTION CALLING
# greeting('A')


def twice(num):
    return num*2

num2 = twice(5)
# print(num2)

# twice2 = lambda num : num * 2 

# print(twice2(4))


li = [1, 2, 3, 4, 5, 6, 9, 27]  # --> 4356

# (num%2 == 0) --> even check
# num%3 == 0 ---> three's multiple check

# def fncheck(num):
#     return num%3 == 0

# threes_li = list(filter( lambda num : num%3==0 , li))  # --> filter fn will return you iterable filter object

# print(threes_li)

# MAP FUNCTION --> accept(fn, iterable) --> return a new iterable map object

# li_divided =  tuple(map(lambda a : a // 2 , li))
# print(li_divided)

# REDUCE FUNCTION --> accept(fn, iterable, start) ---> single value reduced into one

li = [1, 2, 3, 4, 5, 6, 9, 27]  # --> 4356

def reduce(fn, it, start):
    n = len(it)
    reduced = start
    for i in range(0, n):
        reduced = fn(it[i], reduced)
    return reduced


def arg(x, y):
    return x + y

# ans = reduce(arg, li, 0)
# print(ans)

prod = reduce(lambda num1, num2: num1*num2 , li, 1)
print(prod)

# sum of all elements:
# s = 0
# for el in li:
#     s = s + el


prod = 1
for el in li:
    prod = prod * el

print(prod)

# print(sum(li))