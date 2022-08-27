'''
PROCTORING SOFTWARE
Course: Data and Applications

Group: Welcome_to_IIIT
AUTHORS
    1. Rohan C (2020101130)
    2. Radheshyam T (2020115009)
    3. Priyanshul G (2021121002)
'''

import pymysql.cursors
import random


#region Functions

# Create a new university
def createUniversity():
    try:
        UniName = input("Enter University's Name: ")
        InsertQuery = "INSERT INTO `University`(`Name`) VALUES(%s)"
        cursor.execute(InsertQuery, (UniName))    
        connection.commit()
        RetrieveQuery = "SELECT MAX(`UniversityID`) AS res FROM `University`"
        cursor.execute(RetrieveQuery)
        newID = cursor.fetchall()[0]['res']
        print(UniName, "has been successfully added and has been allotted ID:", newID)

    except Exception as e:
        print("Unable to create university")
        print(e)

# Create a new user account
def createAccount():
    try:
        print("1. Examinee")
        print("2. Examiner")
        print("3. Proctor")
        accountType = input("Enter Account Type: ")
                
        if accountType not in ["1", "2", "3"]:
            print("Invalid Account Type")
            return

        name = input("Enter Name: ")
        mobileNumber = input("Enter Mobile Number: ")
        
        if len(mobileNumber) != 10:
            print("Invalid Mobile Number")
            return    
            
        emailID = input("Enter Email ID: ")     

        if accountType == "1":
            uid = input("Enter University ID: ")
            sqlquery = "INSERT INTO `Examinee` (`Name`,`MobileNumber`, `EmailID`,`UniversityID`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sqlquery, (name, mobileNumber, emailID, uid))

        elif accountType == "2":
            uid = input("Enter University ID: ")
            sqlquery = "INSERT INTO `Examiner` (`Name`,`MobileNumber`, `EmailID`,`UniversityID`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sqlquery, (name, mobileNumber, emailID, uid))
        
        else:
            sqlquery = "INSERT INTO `Proctor` (`Name`,`MobileNumber`, `EmailID`) VALUES (%s,%s,%s)"
            cursor.execute(sqlquery, (name, mobileNumber, emailID))
        
        connection.commit()
        print("Account created successfully")

    except Exception as e:
        print("Unable to create account")
        print(e)

# Schedule a test
def scheduleTest():
    try:
        universityID = input("Enter University ID: ")
        time = input("Enter Scheduled Time (YYYY-MM-DD HH:MM:SS): ")
        duration = input("Enter Duration (seconds): ")
        sql = "INSERT INTO `Test` (`UniversityID`, `ScheduledTime`, `TimeDuration`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (universityID, time, duration))
        connection.commit()
        print("Test Scheduled Successfully")

    except Exception as e:
        print("Unable to schedule test")
        print(e)

# Create a question
def createQuestion():
    try:
        examinerid = input("Enter Examiner ID: ")
        questionid = input("Enter Question Number: ")
        testid = input("Enter Test ID: ")
        marks = input("Enter Marks Allocated: ")
        questiontext = input("Enter Question Text (500 char): ")
        
        sqlquery = "INSERT INTO `Question` (`ExaminerID`, `QuestionID`, `TestID`, `MarksAllocated`, `QuestionText`) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sqlquery, (examinerid, questionid, testid, marks, questiontext))
        
        variable = input("Add question images? (Yes/No): ")
        while variable == "Yes":
            img = input("Enter Image Link: ")
            sqlquery = "INSERT INTO `QuestionImage` (`QuestionID`, `TestID`, `Link`) VALUES (%s,%s,%s)" 
            cursor.execute(sqlquery, (questionid, testid, img))
            variable = input("Add more images? (Yes/No): ")

        variable = "Yes"
        while variable == "Yes":
            ans = input("Enter Correct Answer (500 char): ")
            sqlquery = "INSERT INTO `CorrectAnswer` (`QuestionID`, `TestID`, `Answer`) VALUES (%s,%s,%s)"
            cursor.execute(sqlquery, (questionid, testid, ans))
            variable = input("Add more correct answers? (Yes/No): ")
        
        sqlquery = "UPDATE `Test` SET TotalQuestions = TotalQuestions + 1 WHERE TestID = %s"
        cursor.execute(sqlquery, (testid))
        sqlquery = "UPDATE `Test` SET MaximumMarks = MaximumMarks + %s WHERE TestID = %s"
        cursor.execute(sqlquery, (marks,testid))

        connection.commit()

    except Exception as e:
        print("Unable to create question")
        print(e)
    
# Add new answer for a question
def updateAnswerKey():
    try:
        questionID = input("Enter Question ID: ")
        testID = input("Enter Test ID: ")
        answer = input("Enter New Answer: ")

        sql = "INSERT INTO `CorrectAnswer` VALUES(%s,%s,%s)"
        cursor.execute(sql, (questionID, testID, answer))
        connection.commit()
        print("Answer key updated successfully")

    except Exception as e:
        print("Unable to update answer key")
        print(e)

# Modify user settings (audio/video/theme)
def modifyUserSettings():
    try:
        print("1. Examinee")
        print("2. Examiner")
        print("3. Proctor")
        userAccountType = input("Enter User Account Type: ")

        if userAccountType == "1":
            account = "Examinee"
        elif userAccountType == "2":
            account = "Examiner"
        elif userAccountType == "3":
            account = "Proctor"
        else:
            print("Invalid User Account Type")
            return
        
        userID = input("Enter User ID: ")

        print("1. Change Theme")
        print("2. Change Audio Source")
        print("3. Change Video Source")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            value = input("Enter Theme (dark/light): ")
            update = "Theme"
        elif choice == 2:
            value = input("Enter Audio Source: ")
            update = "Audio"
        elif choice == 3:
            value = input("Enter Video Source: ")
            update = "Video"
        else:
            print("Invalid Choice")
            return

        sql = f"UPDATE {account} SET {update} = %s WHERE {account}ID = %s"
        cursor.execute(sql, (value, userID))
        connection.commit()
        print("User settings modified successfully")

    except Exception as e:
        print("Unable to modify user settings")
        print(e)

# Modify a test's scheduled time and duration
def modifyTestTime():
    try:
        TID = input("Enter TestID of the test to modify: ")
        ST = input("Enter new scheduled time (in the format YYYY-MM-DD HH:MM:SS): ")
        TD = input("Enter new time duration for the test (in seconds): ")
            
        query = "UPDATE `Test` SET `ScheduledTime` = %s, `TimeDuration` = %s WHERE `TestID` = %s"
        cursor.execute(query, (ST,TD,TID))
        connection.commit()
        print("Test timing updated successfully.")

    except Exception as e:
        print("Unable to modify test timing")
        print(e)

# Take a test
def takeTest():
    try:
        ExamineeID = input("Enter Examinee ID: ")
        TestID = input("Enter Test ID: ")
        retrieveProctor = "SELECT `ProctorID` FROM `Proctor`"
        cursor.execute(retrieveProctor)
        ProctorIDs = [dict["ProctorID"] for dict in cursor.fetchall()]
        PID = random.choice(ProctorIDs)

        LinkAud = f"Audio{TestID}_{ExamineeID}.mp3"
        LinkVid = f"Video{TestID}_{ExamineeID}.mp4"

        insertQuery = "INSERT INTO `Examination` VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(insertQuery, (ExamineeID, TestID, PID, LinkAud, LinkVid))        
        connection.commit()

        print("Taking test under proctor with Proctor ID: ", PID)

    except Exception as e:
        print("Unable to enroll for the test")
        print(e)

# Show all scheduled tests for a university
def showTests():
    try:
        universityID = input("Enter University ID: ")
        sql = "SELECT * FROM `Test` WHERE UniversityID = %s"
        cursor.execute(sql, (universityID))
        result = cursor.fetchall()

        print("TestID\tScheduledTime\t\tTimeDuration\tTotalQuestions\tMaximumMarks")
        for row in result:
            print(f'{row["TestID"]}\t{row["ScheduledTime"]}\t{row["TimeDuration"]}\t\t{row["TotalQuestions"]}\t\t{row["MaximumMarks"]}')

    except Exception as e:
        print("Unable to fetch tests")
        print(e)

# Find a particular question by a part of the question text
def findQuestion():
    try:
        keyWord = "%"+input("Enter the keyword (or phrase) to be present in the questions: ")+"%"
        query = "SELECT `TestID`, `QuestionID`, `QuestionText` FROM Question WHERE `QuestionText` LIKE %s"
        cursor.execute(query,(keyWord))
        output = cursor.fetchall()

        print("TestID\tQuestionID\tQuestionText")
        for entry in output:
            print(f'{entry["TestID"]}\t{entry["QuestionID"]}\t\t{entry["QuestionText"]}')

    except Exception as e:
        print("Error")
        print(e)

# Find all examinees who have taken a particular test and belong to a particular university
def findExamineeGT():
    try:
        uid = input("Enter University ID: ")
        testid = input("Enter Test ID: ")
        sqlquery = "SELECT ExamineeID, Name FROM `Examinee` WHERE ExamineeID IN (SELECT ExamineeID FROM `Examination` WHERE TestID = %s) and UniversityID = %s"
        cursor.execute(sqlquery, (testid, uid))
        result = cursor.fetchall()
        
        print("ExamineeID\tName")
        for row in result:
            print(f'{row["ExamineeID"]}\t\t{row["Name"]}')

    except Exception as e:
        print("Unable to retrieve information")
        print(e)

# Name of all examinees monitored by a proctor.
def findProcExaminee():
    try:
        proctorID = input("Enter Proctor ID: ")
        sql = "SELECT Name, ExamineeID FROM `Examinee` WHERE ExamineeID IN (SELECT ExamineeID FROM `Examination` WHERE ProctorID = %s)"
        cursor.execute(sql, (proctorID))
        result = cursor.fetchall()
        print("ExamineeID\tName")
        for row in result:
            print(f'{row["ExamineeID"]}\t\t{row["Name"]}')

    except Exception as e:
        print("Unable to fetch examinees")
        print(e)

# List details of question which have marks allocated more than the average marks per question in that test.
def questionMarks():
    try:
        testid = input("Enter Test ID: ")
        sqlquery = "SELECT AVG(MarksAllocated) FROM Question WHERE TestID = %s"
        cursor.execute(sqlquery, (testid))
        avg = cursor.fetchone()['AVG(MarksAllocated)']
        sqlquery = "SELECT * FROM `Question` WHERE TestID = %s AND MarksAllocated > %s"
        cursor.execute(sqlquery, (testid, avg))
        result = cursor.fetchall()
        
        print("TestID\tQuestionID\tMarksAllocated")
        for entry in result:
            print(f'{entry["TestID"]}\t{entry["QuestionID"]}\t\t{entry["MarksAllocated"]}')

    except:
        print("Unable to retrieve information")

# Find the most valuable test of a university (by the maximum marks allocated to the test)
def findMostValuableTest():
    try:
        universityID = input("Enter University ID: ")
        sqlquery = "SELECT TestID, MaximumMarks FROM `Test` WHERE UniversityID = %s ORDER BY MaximumMarks DESC LIMIT 1"
        cursor.execute(sqlquery, (universityID))
        result = cursor.fetchone()
        print("TestID\tMaximumMarks")
        if result:
            print(f'{result["TestID"]}\t{result["MaximumMarks"]}')

    except Exception as e:
        print("Unable to retrieve information")
        print(e)

#endregion


def main():
    print("Welcome to the Proctoring Software!")
    while True:
        print("\n\n1. Create University")
        print("2. Create New User")
        print("3. Schedule Test")
        print("4. Create Question")
        print("5. Update Answer Key")
        print("6. Modify User Settings")
        print("7. Modify Test Time")
        print("8. Take Test")
        print("9. Show Scheduled Tests")
        print("10. Find Question")
        print("11. Find Examinees who have taken a test")
        print("12. Find Examinees monitored by a proctor")
        print("13. Find Questions which are valuable for that test")
        print("14. Show the most valuable tests for a particular university")
        print("15. EXIT\n")
        choice = int(input("Enter your choice: "))

        #region Menu Choices
        if choice == 15:
            print("Thank you for using the Proctoring Software!")
            return
        elif choice == 1:
            createUniversity()
        elif choice == 2:
            createAccount()
        elif choice == 3:
            scheduleTest()
        elif choice == 4:
            createQuestion()
        elif choice == 5:
            updateAnswerKey()
        elif choice == 6:
            modifyUserSettings()
        elif choice == 7:
            modifyTestTime()
        elif choice == 8:
            takeTest()
        elif choice == 9:
            showTests()
        elif choice == 10:
            findQuestion()
        elif choice == 11:
            findExamineeGT()
        elif choice == 12:
            findProcExaminee()
        elif choice == 13:
            questionMarks()
        elif choice == 14:
            findMostValuableTest()
        else:
            print("Invalid choice\n")
        #endregion



if __name__ == "__main__":
    
    connection = pymysql.connect(
        host='localhost',
        user='user',
        password='Password@123',
        database='ProjectFinal', 
        cursorclass=pymysql.cursors.DictCursor
    )

    if not connection.open:
        print("Connection failed!")
        exit()

    with connection.cursor() as cursor:
        main()


# END OF CODE
