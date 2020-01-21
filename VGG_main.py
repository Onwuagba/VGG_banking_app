#Command Line Banking Application

#Important libraries for this code
import re

#Array for housing user information
account = []
account = {
    "tes@tester.com": {"password": "ADMINtest2020#", "AccountBalance": 1000.0}
}

#Initialise account balance
AccountBalance = 0.0

#Create Account function
def createAccount ():
    #global accountNumber
    email = input ("Kindly enter your email address:\n")
    if email not in account :
        password = input ("Kindly enter your password:\n")
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password): #Must contain Uppercase, lowercase, Number, a special character and must not be less than 8
            Newpassword = password
            confirm_password = input ("Kindly re-enter your password:\n")
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', confirm_password): 
                #check if the two passwords match
                if confirm_password != Newpassword:
                    print("Passwords do not match!")
                    userInput = input("Want to try again? Y/N\n:").lower()
                    if userInput == "y":
                        createAccount()
                    else:
                        print("Thank you!")
                else:
                    account[email] = {"password": password, "AccountBalance": AccountBalance}
                    print("Account successfully created.")
                    userInput = input("Want to perform a transaction? Y/N\n:").lower()
                    if userInput == "y":
                        transaction()
                    else:
                        print("Thank you!")
            else:
                print("Invalid password format.")
                userInput = input("Want to try again? Y/N\n:").lower()
                if userInput == "y":
                    createAccount()
                else:
                    print("Thank you!")
        else:
                print("Invalid password format.")
                userInput = input("Want to try again? Y/N\n:").lower()
                if userInput == "y":
                    createAccount()
                else:
                    print("Thank you!")
    else:
        print("This email address already exists")
        userInput = input("Want to create an account? Y/N\n:").lower()
        if userInput == "y":
            return createAccount()
        else:
            print("Thank you!")


#checkBalance function
def checkBalance(email):
    userBalance = account[email]["AccountBalance"]
    print("Your current account balance is: ₦"+str(userBalance))
    userInput = input("Want to carryout another transaction? Y/N\n:").lower()
    if userInput == "y":
        return transaction()
    else:
        print("Thank you!")

    
#Deposit function
#Return balance
def deposit(email):
    userAmount = float(input("Please enter the amount to deposit:"))
    account[email]["AccountBalance"] = account[email]["AccountBalance"] + userAmount
    newBalance = account[email]["AccountBalance"]
    print ("₦"+str(userAmount)+" has been deposited to your account\nYour new account balance is ₦"+str(newBalance))
    userInput = input("Want to carryout another transaction? Y/N\n:").lower()
    if userInput == "y":
        return transaction()
    else:
        print("Thank you!")


#Deposit function
def withdraw (email):
    """Withdraw funds"""
    withdrawal_amount = input("Please enter an amount to withdraw")
    userBalance = account[email]["AccountBalance"]
    #check is amount in user account is enough
    if (userBalance < 1000):
        print("Insufficient amount. Your account balance is"+str(userBalance))
    else:
        #deduct money
        account[email]["AccountBalance"] = userBalance - withdrawal_amount
        newBalance = account[email]["AccountBalance"]
        print("₦"+str(withdrawal_amount)+"has been withdrawn from your account\nYour new balance is ₦"+str(newBalance))
        userInput = input("Want to carryout another transaction? Y/N\n:").lower()
        if userInput == "y":
            return transaction()
        else:
            print("Thank you!")

#Deposit function
#Return transferMsg
def transfer (email):
    recipient = input("Please enter the recipient's account email\n:")
    if email == recipient:
        print("Beneficiary email cannot be same as yours")
        userInput = input("Want to carryout another transaction? Y/N\n:").lower()
        if userInput == "y":
            return transaction()
        else:
            print("Thank you!")
    elif recipient not in account:
        print("Beneficiary does not exists")
        userInput = input("Want to carryout another transaction? Y/N\n:").lower()
        if userInput == "y":
            return transaction()
        else:
            print("Thank you!")
    else:
        transferAmount = float(input("Please enter the amount you wish to transfer\n:"))
        userBalance = float(account[email]["AccountBalance"])
        if (userBalance < 1000):
            print("Insufficient amount. Your account balance is"+str(userBalance))
        elif( userBalance < transferAmount):
            print("Insufficient amount. Your account balance is"+str(userBalance))
        else:
            account[email]["AccountBalance"] = userBalance - transferAmount
            newBalance = account[email]["AccountBalance"]
            #add to recipients account
            account[recipient]["AccountBalance"] = account[recipient]["AccountBalance"] + transferAmount
            recipientBalance = account[recipient]["AccountBalance"]
            print("₦"+str(transferAmount)+" has been successfully transferred to "+recipient+" \n Your current balance is ₦"+str(newBalance))
            userInput = input("Want to carryout another transaction? Y/N\n:").lower()
            if userInput == "y":
                return transaction()
            else:
                print("Thank you!")

#Transaction function
def transaction():
    email = input("Please enter your email to begin\n:")
    # check if user exists or not
    if email not in account :
        print("This account does not exist")
        userSelection = input ("Do you want to create an account: Y/N\n:").lower()
        if userSelection == "y":
            createAccount()
        else:
            print("Thank you!")
    else:
        password = input("Please enter your password\n:")
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            # confirm password matches the saved password
            if password == account[email]["password"]:
                userInput = input("Press 1 to Check Balance\nPress 2 to Deposit\nPress 3 to Withdraw\nPress 4 to Transfer\n:")
                if int(userInput) == 1:
                    checkBalance(email)

                elif int(userInput) == 2:
                    deposit(email)

                elif int(userInput) == 3:
                    withdraw(email)

                elif int(userInput) == 4:
                    transfer(email)

                else:
                    print("Invalid input. Please try again later.")

            else:
                print("Incorrect Password. Please try again")
                userSelection = input ("Do you want to create an account: Y/N").lower()
                if userSelection == "y":
                    createAccount()
                else:
                    print("Thank you!")
        else:
            print("Invalid password.")
            userSelection = input ("Do you want to create an account: Y/N").lower()
            if userSelection == "y":
                createAccount()
            else:
                print("Thank you!")

print ("Welcome!\nKindly enter the number to the corresponding function you want to perform:")
userInput = input("Press 1 to Create Account\nPress 2 to Begin a Transaction\n:")
if int(userInput) == 1:
    createAccount()
elif int(userInput) == 2:
    transaction()
else:
    print ("Invalid input. Please try again later.")
    
        
    

    

