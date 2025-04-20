# #Exercises 1

def Product():
    numbers='your numbers should be between 0 and 1000'
    print(numbers)
    num1=int(input('enter the first number here: '))
    num2=int(input('Enter the second number here: '))
    num3=num1*num2
    if(num3<=1000):
        print( num3)
    else:
        num4=num1+num2
        print('the product of those numbers is greater than 1000 but their sum is: ',num4)
Product()
#exercises 2
print('we are outputting the sum of previous and current number in range of 10')
previous_number=0
for current_number in range(10):
    if current_number==0:
        previous_number=current_number
    else:
        previous_number=current_number-1
        sumOfNumbers=previous_number+current_number
        print('current number:',current_number, 'previous number:',previous_number, 'sum:',sumOfNumbers)
#exercises 3
print('printing the characters at index of even in the words you provide')
characters=input('enter words of your choice here: ')
indexes=[]

for char in characters:
    indexes.append(char)
for i in range(len(indexes)):
    if i%2 ==0:
        current=indexes[i]
    else:
        continue 
    print(current)
#exercise 4
def charRemove(word,n):
    return word[n: ]
words=input('Enter a word here: ')
print(charRemove(words,2))

#exercise 5
def check():
    num1=[12,13,6,10,3,12,5,12]
    
    if (num1[0] == num1[-1]):
           print('true')
    else:
            print('false')


check()
#exercises 6
list=[10,20,30,45,89,101]
arr=[]
for i in list:
    if i%5 == 0:
        arr.append(i)
print(arr)

