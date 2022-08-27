CREATE TABLE `University` (
  `UniversityID` int PRIMARY KEY AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL
);

CREATE TABLE `Examinee` (
  `Name` varchar(50) NOT NULL,
  `ExamineeID` int PRIMARY KEY AUTO_INCREMENT,
  `MobileNumber` char(10) UNIQUE NOT NULL,
  `EmailID` varchar(70) UNIQUE NOT NULL,
  `Audio` varchar(30) COMMENT 'device name',
  `Video` varchar(30) COMMENT 'device name',
  `Theme` ENUM ('dark', 'light') DEFAULT "light",
  `UniversityID` int NOT NULL
);

CREATE TABLE `Examiner` (
  `Name` varchar(50) NOT NULL,
  `ExaminerID` int PRIMARY KEY AUTO_INCREMENT,
  `MobileNumber` char(10) UNIQUE NOT NULL,
  `EmailID` varchar(70) UNIQUE NOT NULL,
  `Audio` varchar(30) COMMENT 'device name',
  `Video` varchar(30) COMMENT 'device name',
  `Theme` ENUM ('dark', 'light') DEFAULT "light",
  `UniversityID` int NOT NULL
);

CREATE TABLE `Proctor` (
  `Name` varchar(50),
  `ProctorID` int PRIMARY KEY AUTO_INCREMENT,
  `MobileNumber` char(10) UNIQUE NOT NULL,
  `EmailID` varchar(70) UNIQUE NOT NULL,
  `Audio` varchar(30) COMMENT 'device name',
  `Video` varchar(30) COMMENT 'device name',
  `Theme` ENUM ('dark', 'light') DEFAULT "light"
);

CREATE TABLE `Test` (
  `TestID` int PRIMARY KEY AUTO_INCREMENT,
  `ScheduledTime` datetime NOT NULL,
  `TimeDuration` int NOT NULL COMMENT 'in seconds',
  `TotalQuestions` int DEFAULT 0,
  `MaximumMarks` int DEFAULT 0,
  `UniversityID` int NOT NULL
);

CREATE TABLE `Question` (
  `ExaminerID` int NOT NULL,
  `QuestionID` int,
  `TestID` int,
  `MarksAllocated` int NOT NULL,
  `QuestionText` varchar(500) NOT NULL,
  PRIMARY KEY (`QuestionID`, `TestID`)
);

CREATE TABLE `Examination` (
  `ExamineeID` int,
  `TestID` int,
  `ProctorID` int NOT NULL,
  `LinktoAudio` varchar(100) UNIQUE NOT NULL,
  `LinktoVideo` varchar(100) UNIQUE NOT NULL,
  PRIMARY KEY (`ExamineeID`, `TestID`)
);

CREATE TABLE `CorrectAnswer` (
  `QuestionID` int,
  `TestID` int,
  `Answer` varchar(500),
  PRIMARY KEY (`QuestionID`, `TestID`, `Answer`)
);

CREATE TABLE `QuestionImage` (
  `QuestionID` int NOT NULL,
  `TestID` int NOT NULL,
  `Link` varchar(100) PRIMARY KEY
);

ALTER TABLE `Examinee` ADD FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`);

ALTER TABLE `Examiner` ADD FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`);

ALTER TABLE `Test` ADD FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`);

ALTER TABLE `Question` ADD FOREIGN KEY (`ExaminerID`) REFERENCES `Examiner` (`ExaminerID`);

ALTER TABLE `Question` ADD FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`);

ALTER TABLE `Examination` ADD FOREIGN KEY (`ExamineeID`) REFERENCES `Examinee` (`ExamineeID`);

ALTER TABLE `Examination` ADD FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`);

ALTER TABLE `Examination` ADD FOREIGN KEY (`ProctorID`) REFERENCES `Proctor` (`ProctorID`);

ALTER TABLE `CorrectAnswer` ADD FOREIGN KEY (`QuestionID`) REFERENCES `Question` (`QuestionID`);

ALTER TABLE `CorrectAnswer` ADD FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`);

ALTER TABLE `QuestionImage` ADD FOREIGN KEY (`QuestionID`) REFERENCES `Question` (`QuestionID`);

ALTER TABLE `QuestionImage` ADD FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`);
