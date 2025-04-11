import csv
import random
import datetime
import time
def createAccount():
    name = input("\nPlease enter your name:   ")
    inidep = int(input("Please enter your initial deposit: "))
    accNum = random.randint(1000000000,9999999999)
    while(True):
        password = input("Enter your password:  ")
        checkPass = input("Please reenter your password:    ")
        if(password==checkPass):
            break
        else:
            print("Password don't match")
            print("Try again")
    mobileNo = int(input("Please enter your mobile number:  "))
    while(True):
        if(len(str(mobileNo))==10):
            break
        else:
            time.sleep(1)
            print("Not a valid 10 digit number")
            time.sleep(1)
            mobileNo = int(input("Please enter a 10 digit mobile number:  "))

    try:
        with open("accounts.csv","a+",newline='') as accounts:        
            accounts.seek(0)
            data = csv.reader(accounts)
            next(data)
            account_data = [row[1]for row in data]
            accounts.seek(0)
            data = csv.reader(accounts)
            next(data)
            mobile_data = [row[4]for row in data]
            accNums = list(map(int,account_data))
            mobiles = list(map(int,mobile_data))
            while(accNum in accNums):
                accNum = random.randint(1000000000,9999999999)
            while(True):
                if(mobileNo not in mobiles):
                    break
                else:
                    print("Mobile number already exists")
                    time.sleep(1)
                    mobileNo = int(input("Please enter your mobile number:  "))
            writer = csv.writer(accounts)
            writer.writerow([name,accNum,password,inidep,mobileNo])
    except FileNotFoundError:
        print("File not found")
    print("\nAccount created successfully")
    print(f"\nThank you {name} for opening an account with us. Please note your account number {accNum} for further use\n")
    print("Redirecting to the main page\n")
    time.sleep(2)
    
def login():
    Login = False
    accFound = False
    while(accFound == False):
        accNum = int(input("\nPlease enter your account number:   "))
        try:
            with open("accounts.csv","r") as accounts:
                data = csv.reader(accounts)
                row = next(data,None)
                while(row is not None):
                    try:
                        row[1] = int(row[1])
                    except ValueError:
                        pass
                    if(row[1] == accNum):
                        accFound = True
                        break
                    row = next(data,None)
                if(row == None):
                    time.sleep(1)
                    print("\nInvalid account number")
                    print("Try again\n")
                    time.sleep(1)
        except FileNotFoundError:
            print("File not found")
    password = input("Please enter your pasword:    ")
    try:
        with open("accounts.csv","r") as accounts:
            data = csv.reader(accounts)
            for row in data:
                if row:
                    try:
                        row[1] = int(row[1])
                    except ValueError:
                        pass
                    if(row[1] == accNum):
                        if(row[2]==password):
                            time.sleep(2)
                            print("\nLogin Successful")
                            Login = True
                            break
                        else:
                            time.sleep(1)
                            print("\nWrong Credentials")
                            time.sleep(1)
                            login()
    except FileNotFoundError:
        print("File not found")
    if(Login == True):
        while(True):
            transactionDone = False
            print("\n1. Check balance")
            print("2. Make A Deposit")
            print("3. Make A Withdrawl\n")
            operation = (input("Please enter a number to perform any action: "))
            if (operation == '1'):
                transactionDone = True
                time.sleep(1.5)
                try:
                    with open("accounts.csv","r") as accounts:
                        data = csv.reader(accounts)
                        for row in data:
                            if row:
                                try:
                                    row[1] = int(row[1])
                                except ValueError:
                                    pass
                                if(row[1]==accNum):
                                    print("\nYour current balance is: ",row[3])
                                    time.sleep(2)
                except FileNotFoundError:
                    print("File not found")
            elif(operation == '2'):
                time.sleep(1.5)
                transactionDone = True
                while True:
                    try:
                        deposit = int(input("\nPlease enter a deposit amount: "))
                        depType = input("Please enter the type of deposit(Cash/Cheque): ")
                        break
                    except ValueError:
                        print("Please enter a valid amount")
                try:
                    with open("accounts.csv","r")as accounts:
                        data = csv.reader(accounts)
                        rows = list(data)
                        for row in rows:
                            if row:
                                try:
                                    row[1] = int(row[1])
                                except ValueError:
                                    pass
                                if(row[1] == accNum):
                                    try:
                                        row[3] = int(row[3])
                                    except ValueError:
                                        pass
                                    while(True):
                                        if(deposit>0):
                                            if(depType=='Cash'):
                                                row[3] += deposit
                                                break
                                            elif(depType=='Cheque'):
                                                print("Your cheque is subject to clearance from the bank")
                                                row[3] += deposit
                                                break
                                        else:
                                            time.sleep(1)
                                            print("\nCan't enter negative value\n")
                                            time.sleep(1)
                                            deposit = int(input("Please enter a deposit amount: "))
                
                except FileNotFoundError:
                    print("File not found")
                time.sleep(2)
                x = datetime.datetime.now()
                try:
                    with open("accounts.csv","w",newline='') as account:
                        writer = csv.writer(account)
                        writer.writerows(rows)
                except FileNotFoundError:
                    print("File not found")
                try:
                    with open("transaction.csv","a+",newline='') as transaction:
                        for row in rows:
                            if row:
                                try:
                                    row[1] = int(row[1])
                                except ValueError:
                                    pass
                                if(row[1] == accNum):
                                    writer = csv.writer(transaction)
                                    writer.writerow([row[1],"Deposit",deposit,x.strftime("%d-%m-%Y")])
                                else:
                                    continue
                except FileNotFoundError:
                    print("File not found")
            elif(operation=='3'):
                time.sleep(1.5)
                transactionDone = True
                while True:
                    try:
                        withdrawl = int(input("Please enter a withdrawl amount: "))
                        break
                    except ValueError:
                        print("Please enter a valid amount")
                try:
                    with open("accounts.csv","r")as accounts:
                        data = csv.reader(accounts)
                        rows = list(data)
                        for row in rows:
                            if row:
                                try:
                                    row[1] = int(row[1])
                                except ValueError:
                                    pass
                                if(row[1] == accNum):
                                    try:
                                        row[3] = int(row[3])
                                    except ValueError:
                                        pass
                                    while(True):
                                        if(withdrawl<0):
                                            time.sleep(1)
                                            print("\nCan't enter negative value\n")
                                            time.sleep(1)
                                            withdrawl = int(input("Please enter a withdrawl amount: "))
                                        else:
                                            if(row[3]>=withdrawl):
                                                row[3] -= withdrawl
                                                break
                                            else:
                                                time.sleep(1)
                                                print("\nInsufficient funds\n")
                                                time.sleep(1)
                                                withdrawl = int(input("Please enter a withdrawl amount: "))
                except FileNotFoundError:
                    print("File not found")
                time.sleep(2)
                x = datetime.datetime.now()
                try:
                    with open("accounts.csv","w",newline='') as account:
                        writer = csv.writer(account)
                        writer.writerows(rows)
                except FileNotFoundError:
                    print("File not found")
                try:
                    with open("transaction.csv","a+",newline='') as transaction:
                        for row in rows:
                            if row:
                                try:
                                    row[1] = int(row[1])
                                except ValueError:
                                    pass
                                if(row[1] == accNum):
                                    writer = csv.writer(transaction)
                                    writer.writerow([row[1],"Withdrwal",withdrawl,x.strftime("%d-%m-%Y")])
                                else:
                                    continue
                except FileNotFoundError:
                    print("File not found")
                time.sleep(1)
                print("\nPlease collect the cash and ensure the amount before leaving.")
                time.sleep(1)
            else:
                time.sleep(1.5)
                print("\nInvalid Input\n")
                time.sleep(1)
            if(transactionDone == True):
                another = False
                while(True):
                    more = input("\nDo you want to make another transaction?(Y/n) ")
                    if(more.lower() == 'n'):
                        time.sleep(0.5)
                        print("\nLogging Out\n")
                        time.sleep(2)
                        break
                    elif(more.lower()=='y'):
                        transactionDone = False
                        another = True
                        break
                    else:
                        time.sleep(1)
                        print("\nPlease enter a valid input\n")
                        time.sleep(1)
            else:
                continue
            if(another == False):
                break
            else:
                continue

print("Welcome to the banking system\n")
while(True):
    print("We provide the following services:")
    print("\t1. Create an account")
    print("\t2. Login")
    print("\t3. Exit")
    operation = (input("Please enter a number to perform any action:   "))
    if(operation == '1'):
        time.sleep(2)
        createAccount()
    elif(operation == '2'):
        time.sleep(1.5)
        login()
    elif(operation == '3'):
        time.sleep(1)
        print("\nThank you for using Yash Banking System")
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print("Incorrect input try again")
        time.sleep(1)