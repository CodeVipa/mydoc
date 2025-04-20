
default_user_pin = 12345
initial_balance = 100000
default_ussd = "*123#"
input_message = "Please enter your pin: "
pin_error_message = "Invalid pin length, please re-enter your pin"
ussd_error_message = "Invalid USSD, please re-enter the code"

print("""
+---------------------------------------+
| Welcome to the Bank simulation system |
+---------------------------------------+
""")


def message_user_format(message):
    return f"""

 {message} 

    """


def validate_pin(user_pin):
    if len(str(user_pin)) != 5:
        print(message_user_format(pin_error_message))
        return False
    return True


def user_pin_input(input_message):
    while True:
        try:
            user_pin = int(input(input_message))  
            if validate_pin(user_pin):  
                return user_pin
        except ValueError:
            print(message_user_format("Invalid input. Please enter a numeric PIN."))


def validate_ussd(ussd):
    if len(ussd) != 5:
        print(message_user_format(ussd_error_message))
        return False
    elif ussd != default_ussd:
        print(message_user_format("Invalid USSD, please re-enter the code"))
        return False
    return True


def ussd_input(input_message="Please enter USSD code: "):
    while True:
        ussd = input(input_message) 
        if validate_ussd(ussd):  
            return ussd


def check_balance(balance):
    if balance > 0:
        print(message_user_format(f"Your current balance is {balance}"))
    else:
        print(message_user_format("Your current balance is 0"))

def withdraw_money(balance):
    if balance > 0:
        check_balance(balance)
        print(message_user_format("How much would you like to withdraw?"))
        while True:
            try:
                withdraw_money_input = int(input("Enter amount: "))
                if withdraw_money_input <= 0:
                    print(message_user_format("Please enter a positive amount."))
                elif withdraw_money_input <= balance:
                    balance -= withdraw_money_input
                    print(message_user_format(f"Dear user, your transaction was completed successfully. Your new balance is {balance}"))
                    break
                else:
                    print(message_user_format("Your account balance is insufficient. Please recharge your account."))
            except ValueError:
                print(message_user_format("Invalid input. Please enter a numeric amount."))
    else:
        print(message_user_format("Insufficient funds."))
    return balance

def deposit_money(balance, message):
    print(message_user_format(f"{message} How much would you like to deposit?"))
    while True:
        try:
            deposit_amount_input = int(input("Enter amount: "))
            if deposit_amount_input <= 0:
                print(message_user_format("Please enter a positive amount."))
            else:
                balance += deposit_amount_input
                print(message_user_format(f"Dear user, your transaction was completed successfully. Your new balance is {balance}"))
                break
        except ValueError:
            print(message_user_format("Invalid input. Please enter a numeric amount."))
    return balance

def display_choices():
    print(message_user_format("""
    1. Withdraw money
    2. Deposit money
    3. Check remaining balance
    4. Exit
    """))
    while True:
        try:
            choice_input = int(input("Enter your choice: "))
            if choice_input not in [1, 2, 3, 4]:
                print(message_user_format("Invalid choice, please enter a number between 1 and 4."))
            else:
                return choice_input
        except ValueError:
            print(message_user_format("Invalid input. Please enter a numeric choice."))

def exit_system():
    print(message_user_format("Thank you for using the MoMo simulation service. Goodbye!"))
    quit()

def main():
    global initial_balance
    
    
    user_pin = user_pin_input(input_message)
    ussd = ussd_input()

    while True:
    
        choice = display_choices()
        
        if choice == 1:
            initial_balance = withdraw_money(initial_balance)
        elif choice == 2:
            initial_balance = deposit_money(initial_balance, "Welcome to the depositing Bank simulation service")
        elif choice == 3:
            check_balance(initial_balance)
        elif choice == 4:
            exit_system()

main()
