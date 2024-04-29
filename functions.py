import mysql.connector
import random
import unittest
import colorama

# Colorama library listener
colorama.init()

# This menu function starts the banking program. It allows users to interact and choose between several options.
# It also features recursion for user error inputs.


def menu():
    print("\n**************************************\n")
    print(colorama.Fore.YELLOW + "Welcome to C2C Banking Management" + colorama.Fore.RESET)
    print("\n***************************************\n")

    while True:
        bank_options = int(input("What would you like to do: \n" + colorama.Fore.MAGENTA + "Create Account, Modify Account, Close Account, Open Transactions: " + colorama.Fore.GREEN + "Type 1, 2, 3, or 4: " + colorama.Fore.RESET))

        if bank_options == 1:
            print("\nYou have selected to Create Account.\n")
            account_creation()
            bank_options == 0
            break

        elif bank_options == 2:
            print("\nYou have selected to Modify Account.\n")
            account_modification()
            bank_options == 0
            break

        elif bank_options == 3:
            print("\nYou have selected to Close Account.\n")
            # NOT WORKING
            # account_closure()
            bank_options == 0
            break

        elif bank_options == 4:
            print("\nYou have selected to Open Transactions.\n")
            # NOT IMPLEMENTED
            # account_transactions(accountnumber)
            bank_options == 0
            break

        else: 
            print("\nInvalid Input. Try Again.\n")
            break



# This function should be able to check within accounts and determine/find any allotments of accounts matching a particular accountnumber
# It should always run before creating an account as accounts cannot have the same id
# CODE SEGMENT UNFORTUNETLY DIDN'T WORK OUT. FURTHER DEBUGGING REQUIRED.

# def check_account_exists(account_number):
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
#         cursor = connection.cursor()

#         # Execute the query
#         sql_query = "SELECT * FROM account WHERE accountnumber = %s"
#         cursor.execute(sql_query, (account_number,))
        
#         # Fetch the result
#         result = cursor.fetchone()
        
#         # Check if the account exists within accounts
#         if result:
#             print("Account exists.")
#         else:
#             ADDITIONAL CODE SEGMENT
#             print("Account does not exist.")

#     except mysql.connector.Error as err:
#         print("Error:", err)

#     finally:
#         # Close cursor and connection
#         cursor.close()
#         connection.close()



# This creation function allows users to add create new bank accounts.
# Users will be asked for a username, account pin, and account type. ==> Possible feature: ask user how much they want initally deposited.

def account_creation():
    

    # Database Connection
    connection = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
    cursor = connection.cursor()

    try:
        # Prompt user for account details
        username_selection = input(colorama.Fore.CYAN + "Enter a Username: " + colorama.Fore.RESET)
        account_pin_selection = input(colorama.Fore.CYAN + "Enter an account pin. Don't forget it: " + colorama.Fore.RESET)
        initial_deposit = float(input(colorama.Fore.CYAN + "How much money (USD) would you like to deposit: " + colorama.Fore.RESET ))
        account_type = input(colorama.Fore.CYAN + "What account type (business, personal): " + colorama.Fore.RESET)

        print("\n***************************************")

        # Generate random account number
        account_number = random.randint(100000, 999999)
        # print(account_number)

        # Updating Database with correct information regarding new users account
        data = (username_selection, account_number, account_pin_selection, initial_deposit, account_type)
        # DELETE ME gid = ','.join(empolyes_information)

        sqlFormula = "INSERT INTO accounts (useraccount, accountnumber, accountpin, netbalance, accounttype) VALUES (%s, %s, %s, %s, %s)"

        # Execute the query with data
        cursor.execute(sqlFormula, data)

        # Commit the transaction
        connection.commit()

        print("\n", cursor.rowcount, "Account created successfully.")

        print("\n***************************************\n" + colorama.Fore.MAGENTA + "RETURNING TO C2C BANKING MENU." + colorama.Fore.RESET)



        # This code segment should be able to display the recently added information for the new account
        # IMCOMPLETE CODE SEGEMENT
        # query = "SELECT acountnumber FROM accounts"
        # cursor.execute(query)
        # myresult = cursor.fetchone()
        # for item in myresult:
        #     print(item)

    # Rollback the transaction in case of an error
    except mysql.connector.Error as err:
        print("Error:", err)

        connection.rollback()

    # Final process as connection is closed.
    finally:

        # Close cursor and connection
        cursor.close()
        connection.close()

    menu()





# This function will allow users to edit information regarding accounts, including accounttype, useraccount (PIN required)
# https://www.youtube.com/watch?v=W321PFPLcHk&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&index=6 ==> EXAMPLE

def account_modification():

    mydb = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
    mycursor = mydb.cursor()

    options = input(colorama.Fore.CYAN + "Would you like to update useraccount and accounttype: yes/no: " + colorama.Fore.RESET)
    
    if options == "yes":
        new_useraccount = input(colorama.Fore.CYAN + "Enter new useraccount: " + colorama.Fore.RESET)
        new_accounttype = input(colorama.Fore.CYAN + "ENter new accounttype (business/personal): " + colorama.Fore.RESET)
        data = (new_useraccount, new_accounttype)
        print(colorama.Fore.RED + "\nFUNCTIONALLITY NOT WORKING AS INTENDED." + colorama.Fore.RESET)
        quit

    sql_formula = ("UPDATE useraccount, accounttype SET useraccount = %s, accounttype = %s WHERE accountnumber = %s")
    mycursor.execute(sql_formula, data)
    mydb.commit()
    mycursor.close()
    mydb.close()

    # Check account and ensure modification occurs in right row, and returns all modified components otherwise don't commit changes.
    # INCOMPLETE CODE SEGEMENT: 
    # for row in myresult:
    #     print(row)

   # if check_account_exists(account_number) 






# This fucntion will allow users to close their bank accounts. (PIN, accountnumber, and useraccount required)
def account_closure():

    username_selection = input("Enter a Username: ")
    account_pin_selection = input("Enter an account pin. Don't forget it: ")

    # Check if Account exsists in DB. Accces Account Number from DB and check general information. 
    # check_account_exists(account_number)

    # Ensure password can access account before next conditional to DELETE account from SCHEMA
    # NOTE: MORE STEPS ARE REQUIRED TO ENSURE A PROPER WORKING ACCOUNT CLOSURE FUNCTION

    while True:
        account_confirmation = input("Are you sure you want to CLOSE your Bank Account? This Cannot be undone, all funds will be lost. (YES, NO): ")

        if account_confirmation == "YES":

            mydb = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
            mycursor = mydb.cursor()
            query = "DELETE FROM empolyes WHERE address useraccount = %s"

            # INCOMPLETE CODE SEGMENT
            # # account_deletion = 
            # query.execute(query, account_deletion)
            # mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
            break
        
        # ERROR VALIDATION to ensure proper and secure account information
        elif account_confirmation == "NO":
            print("Account remains unclosed.")
            break

        else:
            print("Invalid Input.")





# This function will allow users to access funds, deposits, withdrawls.
# def account_transactions(accountnumber):

# MAIN FEATURES:
"""
-USER must be loggined in via ensuring they have credentials to access an account (useraccount, accountnumber, and user PIN)
to ensure safety for customers
-BY prompting USER for this information, SAFETY features will need to be implented or reused from earlier code to double check
and validate USER information before procceding.

-AFTER USER VALIDATION, PROMPT USER to SEVERAL options including transactional operations including (CHECKING OVERALL BALANCE,
ALLOW DEPOSITS TO OTHER ACCOUNTS, and WITHDRAWL MONEY)

-AFTER ENSURE AND CONFIRM USER ACTIONS with safety prompts before commiting changes to accounts
-FINALLY RETURN to MAIN MENU

-WAYS OF ORGANIZING OVERALL STRUCTURE INCLUDE MAKING CLASSES OR SUBFUNCTIONS into a main account transaction function.
-this will allow development to be easier, and potentially easier for USER as well.

"""

# account_number = input("Enter account number: ")


# connection = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
#    cursor = connection.cursor()
#  cursor.execute("SELECT netbalance FROM accounts WHERE account_number = %s", (account_number))

# NOTE TO SELF: WHAT IF withdrawls exceed balance amount?
# ==> WOULD I ALLOW A NEGATIVE BALANCE or CREATE CONDITIONS TO PREVENT IT FROM OCCURING?

# ADDITIONALLY, would withdrawling money go anywhere? OR is usd money just subtracting from an account netbalance without a trace of it?