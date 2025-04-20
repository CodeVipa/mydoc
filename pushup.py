def Ticket(age, student_id):
    Child = 5000
    Adult = 10000
    Senior = 7000
    student_discount = 0.2
    
    if age < 12:
        ticket = Child
    elif 12 <= age <= 60:
        ticket = Adult
        if student_id:
            ticket -= student_discount * ticket 
    else:
        ticket = Senior
        if student_id:
            ticket -= student_discount * ticket  
    return ticket

age = int(input('Enter your age: '))

studentId_answer = input('Do you have a student ID? (yes/no): ')
student_id = studentId_answer.lower() == 'yes'

final_price = Ticket(age, student_id)
print(f'The final ticket price is: RWF {final_price:.2f}')


