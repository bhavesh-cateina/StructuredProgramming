bank_list = ['SBI' , 'BOI', 'HDFC']

bank_list[0]  =  ['s1','s2','s3']
bank_list[1]  =  ['b1','b2','b3']
bank_list[2]  =  ['h1','h2','h3']

sbi = bank_list[0]

boi = bank_list[1]

hdfc = bank_list[2]


balance = 0
lt = 0
id  = 0


def deposit(amount):
  global balance
  global lt
  if(amount > 0):
      balance = balance + amount
      lt = amount

def withdraw(amount):
  global balance
  global lt
  if(balance >= amount):
      balance = balance - amount
      lt = -amount

def statement():
    print("|Statment|")
    print("----------------------------------")
    print("Balance =",balance)
    print("Last Transaction =",lt)
    print("----------------------------------")

    print("Welcome to InterBank Transfer\n")

print("Help-")
print("Mention your bank name")
print("Type S for SBI Bank")
print("Type B for BOI Bank")
print("Type H for HDFC Bank")
print("Type q to Quit\n")

action = input("action> ").lower()
while(action != "q"):
    if(action == "s"):
        print("Welcome to SBI Bank")
        print("Enter account details")
        print("Type q to Quit\n")
        acc = input("account>").lower()
        while(acc != "q"):
            if(acc in sbi):
                print("Type d to Deposit")
                print("Type w to Withdraw")
                print("Type s to print the Statement")
                print("Type q to Quit\n")
                transaction_type = input("Transaction Type> ").lower()
                while(transaction_type != "q"):
                    if(transaction_type == "s"):
                        statement();
                    elif(transaction_type == "d"):
                        print("Please Enter the value to be Deposited")
                        amount = int(input("deposit> "))
                        deposit(amount);
                    elif(transaction_type == "w"):
                        print("Please Enter the value to be Withdrawn")
                        amount = int(input("withdraw> "))
                        withdraw(amount)
                    elif(transaction_type == "h"):
                        print("Help-")
                    elif(transaction_type != "d" or transaction_type != "w" or transaction_type != "s"):
                        print("Not a transaction type")
                    transaction_type = input("Transaction Type> ").lower();
            elif(acc not in sbi):
                print("acc not in SBI")
            acc = input("account> ").lower();


    if(action == "b"):
        print("Welcome to BankofIndia")
        print("Enter account details")
        acc = input("account> ").lower()
        while(acc != "q"):
            if(acc in boi):
                print("Type d to Deposit")
                print("Type w to Withdraw")
                print("Type s to print the Statement")
                print("Type q to Quit\n")
                transaction_type = input("Transaction Type> ").lower()
                while(transaction_type != "q"):
                    if(transaction_type == "s"):
                        statement();
                    elif(transaction_type == "d"):
                        print("Please Enter the value to be Deposited")
                        amount = int(input("deposit> "))
                        deposit(amount)
                    elif(transaction_type == "w"):
                        print("Please Enter the value to be Withdrawn")
                        amount = int(input("withdraw> "))
                        withdraw(amount)
                    elif(transaction_type == "h"):
                        print("Help-")
                    elif(transaction_type != "d" or transaction_type != "w" or transaction_type != "s"):
                        print("Not a transaction type")
                    transaction_type = input("Transaction Type> ").lower();
            elif(acc not in boi):
                print("acc not in bank of india")
            acc = input("account> ").lower();

    if(action == "h"):
        print("Welcome to HDFC BANK")
        print("Enter account details")
        acc = input("account> ").lower()
        while(acc != "q"):
            if(acc in hdfc):
                print("Type d to Deposit")
                print("Type w to Withdraw")
                print("Type s to print the Statement")
                print("Type q to Quit\n")
                transaction_type = input("Transaction Type> ").lower()
                while(transaction_type != "q"):
                    if(transaction_type == "s"):
                        statement();
                    elif(transaction_type == "d"):
                        print("Please Enter the value to be Deposited")
                        amount = int(input("deposit> "))
                        deposit(amount)
                    elif(transaction_type == "w"):
                        print("Please Enter the value to be Withdrawn")
                        amount = int(input("withdraw> "))
                        withdraw(amount)
                    elif(transaction_type == "h"):
                        print("Help-")
                    elif(transaction_type != "d" or transaction_type != "w" or transaction_type != "s"):
                        print("Not a transaction type")
                    transaction_type = input("Transaction Type> ").lower();
            elif(acc not in hdfc):
                print("acc not in hdfc bank")
            acc = input("account> ").lower();
    else:
        print("Please Enter A Correct Command")
        action = input("action> ").lower();
print("Thank you for using PiggyBank...");