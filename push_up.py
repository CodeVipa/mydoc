# User_data=int(input('enter a number: '))
# def piles(n):
#     data=[]
#     for i in range (n):
#         data.append(n)
#         n+=2
#         print(data)
# piles(User_data)
# calculator

def add(x,y):
    return(x + y)

def substract(x,y):
    return(x - y)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    if y!=0:
        return(x / y)
    else:
        print('error! cant divide a number by 0')
print('select the following number')
print('1.Add')
print('2.Substract')
print('3.Multiply')
print('4.Divide')
 
while True:
    choice=input('enter ur choice(1,2,3,4): ')
    if choice in ['1','2','3','4']:
        num1=float(input('your first number: '))
        num2=float(input('your second number: '))
        if choice == '1':
            print(num1, '+' , num2,'=', add(num1,num2))
        
        elif choice == '2':
            print(num1,'-',num2,'=', substract(num1,num2))
       
        elif choice == '3':
            print(num1,'*',num2,'=', multiply(num1,num2))
       
        elif choice == '4':
            print(num1,'/',num2,'=', divide(num1,num2))
        
        else:
            print('invalid input')