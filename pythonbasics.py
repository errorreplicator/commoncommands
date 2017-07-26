# a = 0
# while a <= 100:
#     print(a)
#     a += 1
#
# for x in range(1,11):
#     print(x)
#
#
# a = 20
# b = 20
#
# if a > b:
#     print('a={} is greater than b={}'.format(a,b))
# elif a == b:
#     print('a = {} is equal b={}'.format(a,b))
# else:
#     print('a = {} is smaller than b = {}'.format(a,b))

##FizzBuzz
# for x in range(1,101):
#     if x%3 == 0 and x%5 == 0:
#         print('FizzBuzz')
#     elif x%3 == 0:
#         print('Fizz')
#     elif x%5 == 0:
#         print('Buzz')
#     else:
#         print(x)

##Fibonacci
# a, b = 0, 1
# for i in range(1,11):
#     print(a)
#     a,b = b,a+b

# def fibo(no):
#     a, b = 0, 1
#     for x in range(1 , no+1):
#         if x == no:
#             print(a)
#         a, b = b , a+b
#
# fibo(7)

##DATA TYPES
#Tuples are fixed size in nature whereas lists are dynamic.
#LIST
#MUTABLE (can be changed )
#slower than tuple

# my_list = [2,4,6,8,10]
# for x in my_list:
#     print(x)

#TUPLE
#IMMUTABLE
#Faster than list
#Cant add/remove element from tuple
#It makes your code safer if you “write-protect” data that does not need to be changed.

# my_tuple = (1,2,3,4,5,6,7)
# for x in my_tuple:
#     print(x)

#dictionary
#dictionary is hash table
# my_dict = {'A':1,'B':2,'C':3}
# for key,val in my_dict.items():
#     print(key,val)

#SET
# my_set = {1,2,3,1,2,4,5,6,7,7,7,8,9,10}
# for x in my_set:
#     print(x)

## LIST COMPREHENSIONS
my_list = [1,2,3,4,5]
list_sqr = [x*x for x in my_list]
print(list_sqr)
list_sqr_nat = [x*x for x in range(1,3)]
print(list_sqr_nat)

#ITERATORS YILD

#Basis of CLASSES