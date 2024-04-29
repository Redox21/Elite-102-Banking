import mysql.connector
import random
import unittest

# This menu function starts the banking program. It allows users to interact and choose between several options.
# It also features recursion for user error inputs.

# class TestStringMethods(unittest.TEstCase):

#     def 




def menu():
    print("\n")
    print("\n**************************************\n")
    print("Welcome to C2C Banking Management")
    print("\n***************************************\n")

    while True:
        bank_options = int(input("What would you like to do: \nCreate Account, Modify Account, Close Account, Open Transactions: Type 1, 2, 3, or 4: "))

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
            # account_closure()
            bank_options == 0
            break

        elif bank_options == 4:
            print("\nYou have selected to Open Transactions.\n")
            # account_transactions()
            bank_options == 0
            break

        else: 
            print("\nInvalid Input. Try Again.\n")
            break

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
        
#         # Check if the account exists
#         if result:
#             print("Account exists!")
#         else:
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
        username_selection = input("Enter a Username: ")
        account_pin_selection = input("Enter an account pin. Don't forget it: ")
        initial_deposit = float(input("How much money (USD) would you like to deposit: "))
        account_type = input("What account type (business, personal): ")

        print("\n***************************************\n")

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

        print("\n", cursor.rowcount, "Account created successfully.\n")

        print("\n***************************************\n")

        # This code segment should be able to display the recently added information for the new account
        # query = "SELECT acountnumber FROM accounts"
        # cursor.execute(query)
        # myresult = cursor.fetchall()
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
def account_modification():

    mydb = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT accountnumber FROM accounts")
    myresult = mycursor.fetchall()

    # for row in myresult:
    #     print(row)

   # if check_account_exists(account_number) == 


# This fucntion will allow users to close their bank accounts. (PIN, accountnumber, and useraccount required)
def account_closure():

    username_selection = input("Enter a Username: ")
    account_pin_selection = input("Enter an account pin. Don't forget it: ")

    # Check if Account exsists in DB. Accces Account Number from DB and check general information. 
    # account_number = rd.ph_no 

    while True:
        account_confirmation = input("Are you sure you want to CLOSE your Bank Account? This Cannot be undone, all funds will be lost. (YES, NO): ")

        if account_confirmation == "YES":

            mydb = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
            mycursor = mydb.cursor()
            query = "DELETE FROM empolyes WHERE useraccount = %s"

            account_deletion = ""
            query.execute(query, )
            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
            break
        
        elif account_confirmation == "NO":
            print("Account remains unclosed.")
            break

        else:
            print("Invalid Input.")




# This function will allow users to access funds, deposits, withdrawls.
# def account_transactions():

