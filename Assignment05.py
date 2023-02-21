# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Matthew Lord,02.16.2023,Added code to complete assignment 5
# Matthew Lord,02.16.2023 @ 8:52PM,Added code to complete Step 1. Appears to
#     work.
# Matthew Lord,02.20.2023 @ 7:32PM,Finally completed Step 5, however I left
#     out a portion of code that would let the user know the task they were
#     searching for does not exist in the list. I could not figure this out
#     for some reason. The results I was getting were erratic, so I opted
#     not to continue with this area of feedback for this file/assignment at
#     this time.
# Matthew Lord,02.20.2023 @ 8:15PM,Realized I was doing the whole
#     assignment improperly, and not using the "key: value" system for task
#     and priority. Began revising code.
# Matthew Lord,02.20.2023 @ 9:43PM,Completed through step 5 with revised
#     code
# Matthew Lord,02.20.2023 @ 10:15PM,Added a file path for use with the
#     Terminal/Command Line as the file could not be found otherwise.
# Matthew Lord,02.20.2023 @ 10:48,Added additional comments and reviewed
#     code prior to submittal. Ready to submit code.
#
# ------------------------------------------------------------------------ #

# -- BEGIN DATA -- #
# declare variables and constants
strFile = "ToDoList.txt"  # name of file
# use the strFile (file path) below for Terminal/Command Line (Mac OS)
# strFile = "/Users/spacetimeshift/Documents/_PythonClass/Assignment05/ToDoList.txt"  # name of file
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstRow = []    # A list of string data from the file
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
counter = 0  # a counter for looping through the list of dictionary objects
strExit = ""  # a string for exiting the program

# -- END DATA -- #


# -- BEGIN PROCESSING -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
if (strFile):  # see if the file exists to be read from
    objFile = open(strFile, "r")  # if the file exists, open it to be read
    for row in objFile:  # loop through each row of the file
        strData = row  # assign the text file row to a string
        lstRow = strData.split(",")  # create a temporary list from the string
        # use the temporary list to create a dictionary object
        dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
        lstTable.append(dicRow)  # add the dictionary row to a list/table
    # close the file for now
    objFile.close()
else:
    # if the file does not exist, create the file
    objFile = open(strFile, "w")
    # close the file
    objFile.close()

# -- END PROCESSING -- #


# -- BEGIN INPUT/OUTPUT -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5] - ")
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # print a header for the display table
        print("TASK | PRIORITY")
        # loop through the dictionary objects in the list/table
        for item in lstTable:
            dicRow = item  # assign the list entries to a dictionary object
            print(dicRow["task"] + " | " + dicRow["priority"])  # print the file data as a table
        continue  # continue to the while/menu loop

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # prompt user for a task to add to the list/table
        userTask = input("Enter a task: ")
        # prompt user for the priority associated with the previously entered task
        userPriority = input("Enter the priority (HIGH, MIDDLE, LOW) for " + userTask + ": ")
        # create a list/table entry using a dictionary object
        dicRow = {"task": userTask, "priority": userPriority}
        # add the newly created row to the list/table
        lstTable.append(dicRow)
        continue  # continue to the while/menu loop

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # set counter to check when looping through the full list/table
        counter = 1
        # gather input from user as to which item they would like removed
        taskToDelete = input("What task would you like to remove?: ")
        # loop through each row in the list
        for item in lstTable:
            # get the row of text and assign it to a variable
            dicRow = item
            # check if user entry is NOT found in the table
            if dicRow["task"] != taskToDelete:
                # if the entry is NOT found and we have reached the end of our list/table
                if counter >= len(lstTable):
                    # inform the user that the task they entered is not in the list/table
                    print("\nThe item '", taskToDelete, "' has not been found.")
            # check if user entry is found in the table
            elif dicRow["task"] == taskToDelete:
                # remove the item from the list/table
                lstTable.remove(item)
                # inform the user that the item has been removed
                print("\nThe item '", taskToDelete, "' has been removed from the list.")
                break  # continue to the while loop when task is found and deleted from list/table
            counter += 1  # increase counter for each item in the list/table
        continue  # continue to the while/menu loop

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # open the file to save the data to
        objFile = open(strFile, "w")
        # format the lstTable row by row
        for row in lstTable:
            dicRow = row  # assign the row to a dictionary
            # save the data, formatted as CSV
            objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
        objFile.close()  # close the file
        # let the user know that the data has been saved
        print("The data has been saved!")
        continue  # continue to the while/menu loop

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # verify the user would like to exit the program
        strExit = input("Would you like to exit the program? (Y or N): ")
        # check value of user input
        if strExit.lower() == "y":
            # inform user they have exited the program
            print("You have exited the program.")
            break  # and Exit the program
        else:
            continue  # continue to the while/menu loop

# -- END INPUT/OUTPUT -- #

