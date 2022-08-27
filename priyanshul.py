import pymysql.cursors

connection = pymysql.connect(host='localhost', user='priyanshul', password='priyanshul', database='Project', cursorclass=pymysql.cursors.DictCursor)

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

def showTests():
    try:
        universityID = input("Enter University ID: ")
        sql = "SELECT * FROM `Test` WHERE UniversityID = %s"
        cursor.execute(sql, (universityID))
        result = cursor.fetchall()
        for row in result:
            print(row)

    except Exception as e:
        print("Unable to fetch tests")
        print(e)

def getProctorsMonitoredExaminees():
    try:
        proctorID = input("Enter Proctor ID: ")
        sql = "SELECT Name, ExamineeID FROM `Examinee` WHERE ExamineeID IN (SELECT ExamineeID FROM `Examination` WHERE ProctorID = %s)"
        cursor.execute(sql, (proctorID))
        result = cursor.fetchall()
        for row in result:
            print(row)

    except Exception as e:
        print("Unable to fetch examinees")
        print(e)

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

        sql = "UPDATE %s SET %s = %s WHERE %sID = %s"
        cursor.execute(sql, (account, update, value, account, userID))
        connection.commit()
        print("User settings modified successfully")

    except Exception as e:
        print("Unable to modify user settings")
        print(e)

def updateAnswerKey():
    try:
        questionID = input("Enter Question ID: ")
        testID = input("Enter Test ID: ")
        answer = input("Enter New Answer: ")

        sql = "UPDATE `CorrectAnswer` SET Answer = %s WHERE QuestionID = %s AND TestID = %s"
        cursor.execute(sql, (answer, questionID, testID))
        connection.commit()
        print("Answer key updated successfully")

    except Exception as e:
        print("Unable to update answer key")
        print(e)

with connection:
    with connection.cursor() as cursor:
        showTests()
