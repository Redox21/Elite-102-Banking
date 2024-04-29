import mysql.connector
import rand_account as rd

# This menu function starts the banking program. It allows users to interact and choose between several options.
# It also features recursion for user error inputs.

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
            break

        elif bank_options == 2:
            print("\nYou have selected to Modify Account.\n")
            # account_modification()
            break

        elif bank_options == 3:
            print("\nYou have selected to Close Account.\n")
            # account_closure()
            break

        elif bank_options == 4:
            print("\nYou have selected to Open Transactions.\n")
            # account_transactions()
            break

        else: 
            print("\nInvalid Input. Try Again.\n")
            break


# This creation function allows users to add create new bank accounts.
# Users will be asked for a username, account pin, and account type. ==> Possible feature: ask user how much they want initally deposited.

def account_creation():

    # Database Connection

    connection = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
    cursor = connection.cursor()

    # Prompt user for account details

    username_selection = input("Enter a Username: ")

    account_pin_selection = input("Enter an account pin. Don't forget it: ")

    initial_deposit = float(input("How much money (USD) would you like to deposit: "))

    account_type = input("What account type (business, personal): ")

    # Generate random account number

    account_number = rd.ph_no

    # Updating Database with correct information regarding new users account

    empolyes_information = (1, username_selection, account_number, account_pin_selection, initial_deposit, account_type)

    query = "INSERT INTO empolyes (id, useraccount, accountnumber, accountpin, netbalance, accounttype) VALUES (%s, %s, %s, %s, %s, %s)"

    # try:
        # Execute the query with data

    cursor.execute(query, empolyes_information)

        # Commit the transaction

    connection.commit()
    print("\n",cursor.rowcount,"Account created successfully.\n")

    # except mysql.connector.Error as err:
    #     print("Error:", err)

    # finally:
    #     # Close cursor and connection

    cursor.close()
    connection.close()


# This function will allow users to edit information regarding accounts, including accounttype, useraccount (PIN required)
# def account_modification():

def account_modification():
    # SELECT statement ==> Be able to return specfic database information
    # Then from fields, UPDATE records for users account




# This fucntion will allow users to close their bank accounts. (PIN, accountnumber, and useraccount required)

def account_closure():

    username_selection = input("Enter a Username: ")

    account_pin_selection = input("Enter an account pin. Don't forget it: ")

    # Check if Account exsists in DB. Accces Account Number from DB and check general information. 

    account_number = rd.ph_no 

    while True:
        account_confirmation = input("Are you sure you want to CLOSE your Bank Account? This Cannot be undone, all funds will be lost. (YES, NO): ")

        if account_confirmation == "YES":

            connection = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
            cursor = connection.cursor()

            query = "DELETE FROM empolyes WHERE useraccount = %s"

            # account_deletion = ""

            # query.execute(query, )

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


