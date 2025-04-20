def ticket_price(age):
    Child_price=5000
    Adult_price=10000
    Senior_price=7000
    discounted=0.5
    
    if(age<12):
        ticketed_price=Child_price
        print(ticketed_price)
    elif(age==12 & age<=60):
        ticketed_price=Adult_price

        if hasStudent_id:
            ticketed_price-=Adult_price*discounted
            print(ticketed_price)
    else:
        ticketed_price=Senior_price
        if hasStudent_id:
            ticketed_price-=Senior_price*discounted

age=int(input('enter your age please'))
hasStudent_id=input('do you have student id??(yes/no)')
if hasStudent_id == 'yes':
    hasStudent_response=hasStudent_id.lower()
final_ticketPrice=ticket_price(age)
print(final_ticketPrice)