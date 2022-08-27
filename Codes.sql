INSERT INTO University(Name) VALUES("Symbiosis");
INSERT INTO University(Name) VALUES("IITK");
INSERT INTO University(Name) VALUES("Manipal");
INSERT INTO University(Name) VALUES("IIITH");

INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Priyanshul","9267910962","priyanshul.govil@gmail.com",1);
INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Rohan","9898989898","rohan@gmail.com",4);
INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Radheshyam","9482103711","radheshyam@gmail.com",4);
INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Hari","9899705327","hari@gmail.com",4);
INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Shreyas","8860752347","shreyas@gmail.com",3);
INSERT INTO Examinee(Name, MobileNumber, EmailID, UniversityID) VALUES("Pallav","9673401298","pallavk@gmail.com",4);

INSERT INTO Examiner(Name, MobileNumber, EmailID, UniversityID) VALUES("Shantanov","9347198832","shantanov@iiit.ac.in",4);
INSERT INTO Examiner(Name, MobileNumber, EmailID, UniversityID) VALUES("Kamal","8845769023","kamal@iiit.ac.in",4);
INSERT INTO Examiner(Name, MobileNumber, EmailID, UniversityID) VALUES("Kannan","9976590023","kannan@iiit.ac.in",4);

INSERT INTO Proctor(Name, MobileNumber, EmailID) VALUES("Ramesh","8799458710","rameshrocks@yahoo.in");
INSERT INTO Proctor(Name, MobileNumber, EmailID) VALUES("Suresh","6362668906","suresh.op@hotmail.com");
INSERT INTO Proctor(Name, MobileNumber, EmailID) VALUES("Mohini","8854789955","mohini@gmail.com");

INSERT INTO Test(UniversityID, ScheduledTime, TimeDuration) VALUES(4,"2021-10-27 12:00:00",3600);
INSERT INTO Test(UniversityID, ScheduledTime, TimeDuration) VALUES(2,"2021-10-29 10:00:00",4800);
INSERT INTO Test(UniversityID, ScheduledTime, TimeDuration) VALUES(4,"2021-11-02 14:30:00",1800);
INSERT INTO Test(UniversityID, ScheduledTime, TimeDuration) VALUES(4,"2021-12-15 10:00:00",2500);
INSERT INTO Test(UniversityID, ScheduledTime, TimeDuration) VALUES(4,"2022-01-01 00:00:00",3600);

INSERT INTO Question (ExaminerID, QuestionID, TestID, MarksAllocated, QuestionText) VALUES (%s,%s,%s,%s,%s)

Examiner ID: 2
Question Number: 1
Test ID: 1
Marks: 10
Question: How many marks do you think you'll get in this test?
Correct Answers:
    Dependant on other question's performance.
Image Links
    None

Examiner ID: 1
Question Number: 2
Test ID: 1
Marks: 10
Question: Do you think that question 1 is justified?
Correct Answers:
    1. Yes
Image Links
    None

Examiner ID: 2
Question Number: 3
Test ID: 1
Marks: 5
Question: Congrats on completing the course. Did you (a) Achieve knowledge (b) Had fun (c) Liked the course?
Correct Answers:
    1. (a) Achieve knowledge
    2. (b) Had fun
    3. (c) Liked the course
Image Links
    1. https://imgur.com/gallery/ei9D7KF