# from collections import ChainMap
# from collections import deque

# #queston 1
# def sort_array(arr):
#     return sorted(arr)
# input_list=[3,1,4,1,5,9,2,6,5]
# sorted_array=sort_array(input_list)
# print(f"the sorted array is: {sorted_array}")




# #question 2
# def double_number(input_tuple):
#     double_tuple=tuple(number*2 for number in input_tuple)
#     return double_tuple
# input_tuple=(1,2,3,4)
# doubled_number=double_number(input_tuple)
# print(f" the doubled numbers in an array are: {doubled_number}")


# #question 3
# grades={
#     "john":85,
#     "Mary":92,
#     "Alex":89
# }
# print(grades["Mary"])

# #question 4
# def find_intersection(set1,set2):
#     return set1.intersection(set2)
# set1={1,2,3,4}
# set2={3,4,5,6}
# intersection=find_intersection(set1,set2)
# print('the intersection of the above sets is: ',intersection)



# #question 5
# frozen_set1=frozenset([1,2,3])
# frozen_set2=frozenset([3,4,5])
# frozen_set=frozen_set1|frozen_set2

# frozen_set=frozenset(frozen_set)
# print('the frozen set of the above sets is: ',frozen_set)

# #question 6

# dict1={
#     "name":"john",
#     "age":25
#     }
# dict2={
#     "City":"New York",
#     "country":"USA"
# }
# dictionary=ChainMap(dict1,dict2)
# print(dictionary)

# #question 7
# dq=deque([1,3,5])
# dq.append(7)
# dq.appendleft(0)
# dq.pop()
# dq.popleft()
# print(dq)
# from collections import deque
# dq=deque([10,30,11,55,20])
# dq.append(13)
# dq.appendleft(7)
# dq.popleft()
#while loop

# i=1
# while i<=10:
#     print i
#first number
# def check():
#     if num==0:
#         print('the number',num,'is zero')
#     elif num>0:
#         print('the number',num,'is positive')
   
#     else:print('the number ',num,'is negative')
# num=int(input('enter a number'))
# check()
#question 6
# from collections import Counter
# def count(word):
#     characters=[]
#     for char in word:
#         characters.append(char)
#     _characters=Counter(characters)
#     print(_characters)
# words=input('enter a word here: ')
# count(words)

# x=lambda s: s[::-1]
# print(x('faith'))


# words=input('enter your word here: ')
# x=lambda s: s[::-1]
# word=len(words)
# if word %2==0:
#     print(words[::2])
# else:
#     print('none')
# reversed_string= lambda words: words[::-1] 

# print(x(words))
    

#function reversed
# reserved_string=input('enter a word here: ')
# def reserved(n):
#     words=[]
#     for word in n:
#         words.append(word)
#         if len(words)%2==0:
#             print(words/n)
#         else:
#             print('none')

# print(reserved(reserved_string))

# write a lambda function  that accept a parameter which is a string verify if it has even number of characters if it has then your will have to divide that string into two equal strings the return the reverse of those small strings as one string
"""
Function check(n)
characters=in
we have vowels array containing vowels
an empty array where we will append the vowels found in the word a user entered
for char in characters:
    for 
"""
#outputting the number of vowels in a string

# def Check(n):
#     vowels=['a','e','i','o','u']
#     vowel=[]
#     character=[]
#     for char in n:
        
#         for vow in vowels:
#             character.append(vow)
#             if vow == char:
#                 vowel.append(vow)
#     print(len(vowel))
# characters=input('enter a word: ')
# Check(characters)                

"Python".strip("Pon")
