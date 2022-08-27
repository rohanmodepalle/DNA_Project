-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: Project23
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CorrectAnswer`
--

DROP TABLE IF EXISTS `CorrectAnswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CorrectAnswer` (
  `QuestionID` int NOT NULL,
  `TestID` int NOT NULL,
  `Answer` varchar(500) NOT NULL,
  PRIMARY KEY (`QuestionID`,`TestID`,`Answer`),
  KEY `TestID` (`TestID`),
  CONSTRAINT `CorrectAnswer_ibfk_1` FOREIGN KEY (`QuestionID`) REFERENCES `Question` (`QuestionID`),
  CONSTRAINT `CorrectAnswer_ibfk_2` FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CorrectAnswer`
--

LOCK TABLES `CorrectAnswer` WRITE;
/*!40000 ALTER TABLE `CorrectAnswer` DISABLE KEYS */;
/*!40000 ALTER TABLE `CorrectAnswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Examination`
--

DROP TABLE IF EXISTS `Examination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Examination` (
  `ExamineeID` int NOT NULL,
  `TestID` int NOT NULL,
  `ProctorID` int NOT NULL,
  `LinktoAudio` varchar(100) NOT NULL,
  `LinktoVideo` varchar(100) NOT NULL,
  PRIMARY KEY (`ExamineeID`,`TestID`),
  UNIQUE KEY `LinktoAudio` (`LinktoAudio`),
  UNIQUE KEY `LinktoVideo` (`LinktoVideo`),
  KEY `TestID` (`TestID`),
  KEY `ProctorID` (`ProctorID`),
  CONSTRAINT `Examination_ibfk_1` FOREIGN KEY (`ExamineeID`) REFERENCES `Examinee` (`ExamineeID`),
  CONSTRAINT `Examination_ibfk_2` FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`),
  CONSTRAINT `Examination_ibfk_3` FOREIGN KEY (`ProctorID`) REFERENCES `Proctor` (`ProctorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Examination`
--

LOCK TABLES `Examination` WRITE;
/*!40000 ALTER TABLE `Examination` DISABLE KEYS */;
/*!40000 ALTER TABLE `Examination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Examinee`
--

DROP TABLE IF EXISTS `Examinee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Examinee` (
  `Name` varchar(50) NOT NULL,
  `ExamineeID` int NOT NULL AUTO_INCREMENT,
  `MobileNumber` char(10) NOT NULL,
  `EmailID` varchar(70) NOT NULL,
  `Audio` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Video` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Theme` enum('dark','light') DEFAULT 'light',
  `UniversityID` int NOT NULL,
  PRIMARY KEY (`ExamineeID`),
  UNIQUE KEY `MobileNumber` (`MobileNumber`),
  UNIQUE KEY `EmailID` (`EmailID`),
  KEY `UniversityID` (`UniversityID`),
  CONSTRAINT `Examinee_ibfk_1` FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Examinee`
--

LOCK TABLES `Examinee` WRITE;
/*!40000 ALTER TABLE `Examinee` DISABLE KEYS */;
INSERT INTO `Examinee` VALUES ('Priyanshul',2,'9267910962','priyanshul.govil@research.iiit.ac.in',NULL,NULL,'light',1),('Rohan',3,'9898989898','rohan@gmail.com',NULL,NULL,'light',4),('Radheshyam',4,'9482103711','radheshyam@gmail.com',NULL,NULL,'light',4),('Hari',5,'9899705327','hari@gmail.com',NULL,NULL,'light',4),('Shreyas',6,'8860752347','shreyas@gmail.com',NULL,NULL,'light',3),('Pallav',7,'9673401298','pallavk@gmail.com',NULL,NULL,'light',4);
/*!40000 ALTER TABLE `Examinee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Examiner`
--

DROP TABLE IF EXISTS `Examiner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Examiner` (
  `Name` varchar(50) NOT NULL,
  `ExaminerID` int NOT NULL AUTO_INCREMENT,
  `MobileNumber` char(10) NOT NULL,
  `EmailID` varchar(70) NOT NULL,
  `Audio` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Video` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Theme` enum('dark','light') DEFAULT 'light',
  `UniversityID` int NOT NULL,
  PRIMARY KEY (`ExaminerID`),
  UNIQUE KEY `MobileNumber` (`MobileNumber`),
  UNIQUE KEY `EmailID` (`EmailID`),
  KEY `UniversityID` (`UniversityID`),
  CONSTRAINT `Examiner_ibfk_1` FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Examiner`
--

LOCK TABLES `Examiner` WRITE;
/*!40000 ALTER TABLE `Examiner` DISABLE KEYS */;
INSERT INTO `Examiner` VALUES ('Shantanov',1,'9347198832','shantanov@iiit.ac.in',NULL,NULL,'light',4),('Kamal',2,'8845769023','kamal@iiit.ac.in',NULL,NULL,'light',4),('Kannan',3,'9976590023','kannan@iiit.ac.in',NULL,NULL,'light',4);
/*!40000 ALTER TABLE `Examiner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proctor`
--

DROP TABLE IF EXISTS `Proctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Proctor` (
  `Name` varchar(50) DEFAULT NULL,
  `ProctorID` int NOT NULL AUTO_INCREMENT,
  `MobileNumber` char(10) NOT NULL,
  `EmailID` varchar(70) NOT NULL,
  `Audio` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Video` varchar(30) DEFAULT NULL COMMENT 'device name',
  `Theme` enum('dark','light') DEFAULT 'light',
  PRIMARY KEY (`ProctorID`),
  UNIQUE KEY `MobileNumber` (`MobileNumber`),
  UNIQUE KEY `EmailID` (`EmailID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proctor`
--

LOCK TABLES `Proctor` WRITE;
/*!40000 ALTER TABLE `Proctor` DISABLE KEYS */;
INSERT INTO `Proctor` VALUES ('Ramesh',1,'8799458710','rameshrocks@yahoo.in',NULL,NULL,'light'),('Suresh',2,'6362668906','suresh.op@hotmail.com',NULL,NULL,'light'),('Mohini',3,'8854789955','mohini@gmail.com',NULL,NULL,'light');
/*!40000 ALTER TABLE `Proctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Question`
--

DROP TABLE IF EXISTS `Question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Question` (
  `ExaminerID` int NOT NULL,
  `QuestionID` int NOT NULL,
  `TestID` int NOT NULL,
  `MarksAllocated` int NOT NULL,
  `QuestionText` varchar(500) NOT NULL,
  PRIMARY KEY (`QuestionID`,`TestID`),
  KEY `ExaminerID` (`ExaminerID`),
  KEY `TestID` (`TestID`),
  CONSTRAINT `Question_ibfk_1` FOREIGN KEY (`ExaminerID`) REFERENCES `Examiner` (`ExaminerID`),
  CONSTRAINT `Question_ibfk_2` FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Question`
--

LOCK TABLES `Question` WRITE;
/*!40000 ALTER TABLE `Question` DISABLE KEYS */;
/*!40000 ALTER TABLE `Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `QuestionImage`
--

DROP TABLE IF EXISTS `QuestionImage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `QuestionImage` (
  `QuestionID` int NOT NULL,
  `TestID` int NOT NULL,
  `Link` varchar(100) NOT NULL,
  PRIMARY KEY (`Link`),
  KEY `QuestionID` (`QuestionID`),
  KEY `TestID` (`TestID`),
  CONSTRAINT `QuestionImage_ibfk_1` FOREIGN KEY (`QuestionID`) REFERENCES `Question` (`QuestionID`),
  CONSTRAINT `QuestionImage_ibfk_2` FOREIGN KEY (`TestID`) REFERENCES `Test` (`TestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `QuestionImage`
--

LOCK TABLES `QuestionImage` WRITE;
/*!40000 ALTER TABLE `QuestionImage` DISABLE KEYS */;
/*!40000 ALTER TABLE `QuestionImage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test`
--

DROP TABLE IF EXISTS `Test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Test` (
  `TestID` int NOT NULL AUTO_INCREMENT,
  `ScheduledTime` datetime NOT NULL,
  `TimeDuration` int NOT NULL COMMENT 'in seconds',
  `TotalQuestions` int DEFAULT '0',
  `MaximumMarks` int DEFAULT '0',
  `UniversityID` int NOT NULL,
  PRIMARY KEY (`TestID`),
  KEY `UniversityID` (`UniversityID`),
  CONSTRAINT `Test_ibfk_1` FOREIGN KEY (`UniversityID`) REFERENCES `University` (`UniversityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test`
--

LOCK TABLES `Test` WRITE;
/*!40000 ALTER TABLE `Test` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `University`
--

DROP TABLE IF EXISTS `University`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `University` (
  `UniversityID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`UniversityID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `University`
--

LOCK TABLES `University` WRITE;
/*!40000 ALTER TABLE `University` DISABLE KEYS */;
INSERT INTO `University` VALUES (1,'Symbiosis'),(2,'IITK'),(3,'Manipal'),(4,'IIITH');
/*!40000 ALTER TABLE `University` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-25 14:45:00
