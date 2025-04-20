from itertools import permutations
import random

#Question 1
def all_unique(numbers):
    return len(numbers) == len(set(numbers))

print(all_unique([1, 2, 3, 4])) 
print(all_unique([1, 2, 2, 4]))  
#Question 2
def generate_strings():
    chars = 'aeioI'
    return [''.join(p) for p in permutations(chars)]


print(f"some of the generated stings include: {generate_strings()}")
#Question 3
def count_notes(amount):
    notes = [500, 200, 100, 50, 20, 10]
    result = {}
    for note in notes:
        result[note] = amount // note
        amount %= note
    return result

print(f"The number of notes are: {count_notes(1260)}")
#Question 4
def count_divisors(num, even=True):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0 and (i % 2 == 0 if even else i % 2 != 0):
            count += 1
    return count


print( f"the total number of even numbers are:{count_divisors(10, even=True)}")  
print(f"the total number of odd numbers are: {count_divisors(10, even=False)}")  

#Question 5
def divisible_num():
    for num in range(1500,2701):
        if num%7 == 0 and num%5 == 0:
           return num
        else:
            print("that number is not in range")
       
print(divisible_num())
# Question 6


def guess_number():
    target = random.randint(1, 9)
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess == target:
            print(f"Well guessed! the number you guessed is: {target}")
            break
        else:
            print("Try again.")
print( guess_number())

#Question 7:

def stone_piles(n):
   return [n + 2 * i for i in range(n)]

print(f"the number of the stone piles if n is 2 : {stone_piles(2)}")
print(f"the number of the stone piles if n is 10: {stone_piles(10)}") 
print(f"the number of the stone piles if n is 3: {stone_piles(3)}")  
print(f"the number of the stone piles if n is 17: {stone_piles(17)}") 