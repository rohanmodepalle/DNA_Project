import pymysql.cursors

connection = pymysql.connect(host='localhost', user='rohan', password='rohan',
                             database='Project', cursorclass=pymysql.cursors.DictCursor)


def createAccount():
    try:
        print("1. Examinee")
        print("2. Examiner")
        print("3. Proctor")
        createAccountType = input("Enter Create Account Type: ")
        if createAccountType == "1":
            examineename = input("Enter examinee name")
            mobilenumber = eval(input("Enter examinee mobile number"))
            if mobilenumber / 10 ^ 9 < 10 and mobilenumber / 10 ^ 9 >= 1:
                mobile = "Valid"
            if mobile != "Valid":
                print("mobile number is invalid")
                return
            examineeemail = input("Enter examinee emailid")
            examineeaudio = input("Enter joining audio device")
            examineevideo = input("Enter joining video device")
            examineetheme = input("Enter theme (light/dark)")
            if examineetheme != "light" and examineetheme != "dark":
                print("Invalid theme entered")
                return
            examineeuid = eval(input("Enter examinee`s University ID"))
            sqlquery = "INSERT into `Examinee` (`Name`,`MobileNumber`, `EmailID`, `Audio`, `Video`, `Theme`, `UniversityID`) VALUES (%s,%d,%s,%s,%s,%s,%s)" % (
                examineename, mobilenumber, examineeemail, examineeaudio, examineevideo, examineetheme, examineeuid)
            cursor.execute(sqlquery)
            print("Examinee entered successfully")
        elif createAccountType == "2":
            examinername = input("Enter examiner name")
            mobilenumber = eval(input("Enter examiner mobile number"))
            if mobilenumber / 10 ^ 9 < 10 and mobilenumber / 10 ^ 9 >= 1:
                mobile = "Valid"
            if mobile != "Valid":
                print("mobile number is invalid")
                return
            examineremail = input("Enter examiner emailid")
            examineraudio = input("Enter joining audio device")
            examinervideo = input("Enter joining video device")
            examinertheme = input("Enter theme (light/dark)")
            if examinertheme != "light" and examinertheme != "dark":
                print("Invalid theme entered")
                return
            examineruid = eval(input("Enter examiner`s University ID"))
            sqlquery = "INSERT into `Examiner` (`Name`,`MobileNumber`, `EmailID`, `Audio`, `Video`, `Theme`, `UniversityID`) VALUES (%s,%d,%s,%s,%s,%s,%s)" % (
                examinername, mobilenumber, examineremail, examineraudio, examinervideo, examinertheme, examineruid)
            cursor.execute(sqlquery)
            print("Examiner entered successfully")
        elif createAccountType == "3":
            proctorname = input("Enter proctor name")
            mobilenumber = eval(input("Enter proctor mobile number"))
            if mobilenumber / 10 ^ 9 < 10 and mobilenumber / 10 ^ 9 >= 1:
                mobile = "Valid"
            if mobile != "Valid":
                print("mobile number is invalid")
                return
            proctoremail = input("Enter proctor emailid")
            proctoraudio = input("Enter joining audio device")
            proctorvideo = input("Enter joining video device")
            proctortheme = input("Enter theme (light/dark)")
            if proctortheme != "light" and proctortheme != "dark":
                print("Invalid theme entered")
                return
            sqlquery = "INSERT into `Proctor` (`Name`,`MobileNumber`, `EmailID`, `Audio`, `Video`, `Theme`) VALUES (%s,%d,%s,%s,%s,%s)" % (
                proctorname, mobilenumber, proctoremail, proctoraudio, proctorvideo, proctortheme)
            cursor.execute(sqlquery)
            print("Examiner entered successfully")
        else:
            print("Invalid Create Account Type")
            return
        connection.commit()

    except Exception as e:
        print("Unable to create examinee/examiner")
        print(e)


def examinerQuestion():
    try:
        examinerid = eval(input("Enter ExaminerID"))
        questionid = eval(input("Enter question ID"))
        testid = eval(input("Enter test ID"))
        marks = eval(input("Enter marks allocated"))
        questiontext = input("Enter question text")
        variable = "Yes"
        
        sqlquery = "INSERT into `Question` (`ExaminerID`, `QuestionID`, `TestID`, `MarksAllocated`, `QuestionText`) VALUES (%d,%d,%d,%d,%s)" % (
            examinerid, questionid, testid, marks, questiontext)
        cursor.execute(sqlquery)

        while variable == "Yes":
            ans = input("Enter correct answer")
            img = input("Enter answer image link")
            
            sqlquery = "INSERT into `CorrectAnswer` (`QuestionID`, `TestID`, `Answer`) VALUES (%d,%d,%s)" % (
                questionid, testid, ans)
            cursor.execute(sqlquery)
            sqlquery = "INSERT into `QuestionImage` (`QuestionID`, `TestID`, `Link`) VALUES (%d,%d,%s)" % (
                questionid, testid, img)
            cursor.execute(sqlquery)
            variable = input(
                "Type `Yes` if you want to add more correct answers and images, else type `No`")
        sqlquery = "UPDATE `Test` SET TotalQuestions = TotalQuestions + 1 WHERE QuestionID = questionid and TestID = testid"
        cursor.execute(sqlquery)
        sqlquery = "UPDATE `Test` SET MaximumMarks = MaximumMarks + marks WHERE QuestionID = questionid and TestID = testid"
        cursor.execute(sqlquery)
        connection.commit()

    except Exception as e:
        print("Could not make examiner create question")
        print(e)


def examinerTest():
    try:
        uid = input("Enter university ID")
        testid = input("Enter test ID")
        sqlquery = "SELECT Name, ExamineeID FROM `Examinee` WHERE ExamineeID IN (SELECT ExamineeID FROM `Examination` WHERE TestID = testid) and UniversityID = uid"
        cursor.execute(sqlquery)
        result = cursor.fetchall()
        for row in result:
            print(row)

    except:
        print("Unable to retrieve information")


def questionMarks():
    try:
        uid = input("Enter university ID")
        testid = input("Enter test ID")
        sqlquery = "SELECT TotalQuestions FROM `TEST` WHERE TestID=testid and UniversityID=uid"
        cursor.execute(sqlquery)
        total = cursor.fetchall()
        sqlquery = "SELECT MaximumMarks FROM `TEST` WHERE TestID=testid and UniversityID=uid"
        cursor.execute(sqlquery)
        marks = cursor.fetchall()
        avg = marks[0]/total[0]
        sqlquery = "SELECT * FROM `TEST` WHERE TestID=testid and UniversityID=uid and MaximumMarks>avg"
        cursor.execute(sqlquery)
        result = cursor.fetchall()
        for row in result:
            print(row)

    except:
        print("Unable to retrieve information")


with connection:
    with connection.cursor() as cursor:
        createAccount()
