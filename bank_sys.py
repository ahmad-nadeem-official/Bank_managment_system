import datetime

x = datetime.datetime.now()

history = []
list1 = []
dep_amount = 0.0

def starter():
    while True:
        init = "**********choose the option number**********\n"
        op1 = "1. transaction history\n2. withdraw\n3. deposit\n4. transfer\n5. quit"
        print(init + op1)
        
        st = int(input("enter your desired service (use digits): "))  # Convert input to int
        if st == 1:
            transaction_history()
        elif st == 2:
            withdraw()
        elif st == 3:
            deposit()
        elif st == 4:
            transfer()
        elif st == 5:
            logfunc()
        else:
            print("Invalid option. Please try again.")

def login():
    pin = input("enter pin: ")
    name = input("your name: ")
    if (name, pin) not in list1:
        print("user not found")
    else:
        print("successfully logged in")
        starter()

def signup():
    newname = input("set a user name: ")
    newpin = input("set a pin: ")
    list1.append((newname, newpin))
    print(f"sign up successful at {x}")
    starter()

def deposit():
    global dep_amount  # Use global to modify the global variable
    amount = float(input("enter your amount: "))
    dep_amount += amount
    print(f'you have {dep_amount} in your account')
    da = (f'{amount} deposited at {x}')
    history.append(da)

def withdraw():
    global dep_amount  # Use global to modify the global variable
    withd = float(input("how much do you want to withdraw: "))
    if withd > dep_amount:
        print("Insufficient balance")
    else:
        dep_amount -= withd
        print(f'your remaining balance is {dep_amount}')
        wa = (f'{withd} withdrawn at {x}')
        history.append(wa)

def transfer():
    global dep_amount  # Use global to modify the global variable
    pin = input("enter pin: ")
    name = input("your name: ")
    if (name, pin) not in list1:
        print("try again")
    else:
        acc = input("enter account name: ")
        money = float(input("set an amount to be sent: "))
        confirmation = int(input("sent or cancel (enter answer in 1/2): "))
        if confirmation == 1:
            if money > dep_amount:
                print("Insufficient balance")
            else:
                dep_amount -= money
                print(f'the amount of {money} has been sent to {acc} at {x}')
                print(f'your remaining balance is {dep_amount}')  
                ta = (f'{money} sent to {acc} at {x}')
                history.append(ta)
        else:
            print("Transaction cancelled")

def transaction_history():
    for i in history:
        print(i)  

def logfunc():
    start1 = int(input("login or sign up 1/2: "))
    if start1 == 1:
        login()
    elif start1 == 2:
        signup()
    else:
        print("Invalid option selected")           

if __name__ == "__main__":
    print("LOGIN******SIGNUP")
    logfunc()


# The main issue in my code was the input from the user is always a string, but i am comparing it to integers in my starter function. i need to convert the input to an integer before making the comparisons. Additionally, there are some other issues in my code, such as the deposit and withdraw functions not updating dep_amount properly and the incorrect handling of withdraw and transfer.        
