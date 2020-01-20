#Command Line Banking Application

#Important libraries for this code
import re

#Array for housing user information
account = []
account = {
    "tes@tester.com": {"password": "2020", "AccountBalance": 1000.0}
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
                    return createAccount()
                else:
                    account[email] = {"password": password, "AccountBalance": AccountBalance}
                    print("Account successfully created.")
            else:
                print("Invalid password format.")
        else:
                print("Invalid password format.")
    else:
        print("This email address already exists")
        return createAccount()


#checkBalance function
def checkBalance(email):
    userBalance = account[email]["AccountBalance"]
    print("Your current account balance is: ₦"+str(userBalance))

    
#Deposit function
#Return balance
def deposit(email):
    userAmount = float(input("Please enter the amount to deposit:"))
    account[email]["AccountBalance"] = account[email]["AccountBalance"] + userAmount
    newBalance = account[email]["AccountBalance"]
    print ("₦"+str(userAmount)+" has been deposited to your account\nYour new account balance is ₦"+str(newBalance))



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
        

#Deposit function
#Return transferMsg
def transfer (email):
    recipient = input("Please enter the recipient's account email")
    transferAmount = float(input("Please enter the amount you wish to transfer"))
    userBalance = float(account[email]["AccountBalance"])
    if (userBalance < 1000):
        print("Insufficient amount. Your account balance is"+str(userBalance))
    elif( userBalance < transfer_amount):
        print("Insufficient amount. Your account balance is"+str(userBalance))
    else:
        account[email]["AccountBalance"] = userBalance - transferAmount
        newBalance = account[email]["AccountBalance"]
        #add to recipients account
        account[recipient]["AccountBalance"] = account[recipient]["AccountBalance"] + transferAmount
        recipientBalance = account[recipient]["AccountBalance"]
        print("₦"+str(transferAmount)+"has been successfully transferred to "+recipient+" \n Your current balance is ₦"+str(newBalance))


#Transaction function
def transaction():
    email = input("Please enter your email to begin")
    # check if user exists or not
    if email not in account :
        print("This account does not exist")
        userSelection = input ("Do you want to create an account: Y/N")
        if userSelection == "Y":
            createAccount()
        else:
            print("Thank you!")
    else:
        password = input("Please enter your password  ")
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
                createAccount()
        else:
            print("Invalid password.")

print ("Welcome!\nKindly enter the number to the corresponding function you want to perform:")
userInput = input("Press 1 to Create Account\nPress 2 to Begin a Transaction\n:")
if int(userInput) == 1:
    createAccount()
elif int(userInput) == 2:
    transaction()
else:
    print ("Invalid input")
    quit()
        
    

    

