import mysql.connector
import functions as fun


 # Database Connection

connection = mysql.connector.connect(user = "root", database = "empolyes", password = "0148Uapm@*Ss")

cursor = connection.cursor()
 
# Queries for testQuery all rows 

# query = ("SELECT * FROM accounts")
# query = "INSERT into empolyes (id, useraccount, accountnumber, accountpin, netbalance, acounttype)"

# # Exectuting the queries

# print("\n")
# for item in cursor:

#     print(item)

def main():
    # Call the menu function
    fun.menu()

if __name__ == "__main__":
    main()

# Commiting the connection, then closing it.

cursor.close()

connection.close()

# id, useraccount, accountnumber, accountpin, netbalance, acounttype

# userAccountInput = input("Enter a valid username: ")

# def checkAccount():
#     if userAccountInput == empolyes