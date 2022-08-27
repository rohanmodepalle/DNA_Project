import pymysql.cursors
import random

connection = pymysql.connect(host='localhost', user='user', password="Password@123", database='Project23', cursorclass=pymysql.cursors.DictCursor)

def newUni():
    try:
        UniName = input("Please enter the University's name: ")
        InsertQuery = "INSERT INTO `University`(`Name`) VALUES(%s)"
        cursor.execute(InsertQuery,(UniName))    
        connection.commit()
        RetrieveQuery = "SELECT MAX(`UniversityID`) AS res FROM `University`"
        cursor.execute(RetrieveQuery)
        newID = cursor.fetchall()[0]['res']
        print(UniName,"has been successfully added and has been allotted ID:",newID)

    except Exception as e:
        print("Unable to create entry")
        print(e)


def takeTest():
    try:
        ExamineeID = input("Enter Examinee ID: ")
        TestID = input("Enter Test ID: ")
        retrieveProctor = "SELECT `ProctorID` FROM `Proctor`"
        cursor.execute(retrieveProctor)
        ProctorIDs = [dict["ProctorID"] for dict in cursor.fetchall()]
        PID = random.choice(ProctorIDs)

        ###############################
        # Create Link to audio and video

        LinkAud = ".mp3"
        LinkVid = ".mp4"

        insertQuery = "INSERT INTO `Examination` VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(insertQuery, (ExamineeID,TestID,PID,LinkAud,LinkVid))        
        connection.commit()

        #######################
        # Join to display Proctor details?
        print("Successfully enrolled in exam \n Proctor assigned",PID)

    except Exception as e:
        print("Error")
        print(e)


def findQuestion():
    try:
        keyWord = '"%'+input("Enter the keyword (only 1) to be present in the questions: ").split()[0]+'%"'
        query = "SELECT `TestID`, `QuestionID`, `QuestionText` FROM Question WHERE `QuestionText` LIKE %s"
        cursor.execute(query,(keyWord))
        output = cursor.fetchall()

        print("TestID \t QuestionID \t QuestionText \n")
        for entry in output:
            print(entry["TestID"]+"\t"+entry["QuestionID"]+"\t"+entry["QuestionText"]+"\n")

    except Exception as e:
        print("Error")
        print(e)


def valuableTest():
    try:
        query = "SELECT `UniversityID`, `Name`, `TestID`, `MAX(MaximumMarks)` FROM `Test` INNER JOIN `University` ON `Test.UniversityID` = `University.UniversityID` GROUP BY `UniversityID`"
        cursor.execute(query)
        output = cursor.fetchall()
        for row in output:
            print(row)

    except Exception as e:
        print("Error")
        print(e)
    

def modifyTestTime():
    try:
        TID = input("Enter TestID of the test to modify: ")
        ST = input("Enter new scheduled time (in the format YYYY-MM-DD HH:MM:SS) ")
        TD = input("Enter new time duration for the test (in seconds)")
    
        # ogQuery = "SELECT `ScheduledTime`, `TimeDuration` FROM `Test` WHERE `TestID` = %s"
        # cursor.execute(ogQuery,(TID))
        # output = cursor.fetchall()
        
        query = "UPDATE `Test` SET `ScheduledTime` = %s, `TimeDuration` = %s WHERE `TestID` = %s"
        cursor.execute(query, (ST,TD,TID))
        connection.commit()

    except Exception as e:
        print("Error")
        print(e)


with connection:
    with connection.cursor() as cursor:
        # newUni()
        takeTest()
