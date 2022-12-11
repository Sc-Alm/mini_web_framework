-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: booking
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Car`
--

DROP TABLE IF EXISTS `Car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Car` (
  `CarId` int unsigned NOT NULL,
  `ModelId` mediumint unsigned NOT NULL,
  `ColorId` smallint unsigned NOT NULL,
  `Milage` mediumint unsigned NOT NULL,
  `RegistrationNumber` varchar(6) NOT NULL,
  PRIMARY KEY (`CarId`),
  KEY `fk_Car_CarModel1` (`ModelId`),
  KEY `fk_Car_Color1` (`ColorId`),
  CONSTRAINT `fk_Car_CarModel1` FOREIGN KEY (`ModelId`) REFERENCES `CarModel` (`CarModelId`),
  CONSTRAINT `fk_Car_Color1` FOREIGN KEY (`ColorId`) REFERENCES `Color` (`ColorId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Car`
--

LOCK TABLES `Car` WRITE;
/*!40000 ALTER TABLE `Car` DISABLE KEYS */;
INSERT INTO `Car` VALUES (1,1,1,4324,'GDS245'),(2,1,2,74322,'HRE263'),(3,4,4,2544,'HGS845'),(4,3,5,7355,'PAL146'),(5,6,6,7353,'RAI842'),(6,4,2,5363,'WFD930'),(7,6,5,37678,'FDE152'),(8,5,4,3577,'JSD472'),(9,2,6,2312,'JUR622'),(10,1,2,3633,'IRl892');
/*!40000 ALTER TABLE `Car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarModel`
--

DROP TABLE IF EXISTS `CarModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarModel` (
  `CarModelId` mediumint unsigned NOT NULL AUTO_INCREMENT,
  `CarType` enum('Convertible','SUV','Mini','Regular') NOT NULL,
  `ModelName` varchar(255) NOT NULL,
  PRIMARY KEY (`CarModelId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarModel`
--

LOCK TABLES `CarModel` WRITE;
/*!40000 ALTER TABLE `CarModel` DISABLE KEYS */;
INSERT INTO `CarModel` VALUES (1,'Mini','Ford Fiesta'),(2,'Regular','Volvo V40 Automatic'),(3,'Regular','Volvo S40 Eco'),(4,'SUV','Volvo XC60'),(5,'SUV','Ford Transit'),(6,'Convertible','Volvo C70');
/*!40000 ALTER TABLE `CarModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarRentalStation`
--

DROP TABLE IF EXISTS `CarRentalStation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarRentalStation` (
  `CarRentalStationId` int unsigned NOT NULL,
  `CarId` int unsigned NOT NULL,
  KEY `fk_CarRentalStation_Car1` (`CarId`),
  KEY `fk_CarRentalStation_RentalStation1` (`CarRentalStationId`),
  CONSTRAINT `fk_CarRentalStation_Car1` FOREIGN KEY (`CarId`) REFERENCES `Car` (`CarId`),
  CONSTRAINT `fk_CarRentalStation_RentalStation1` FOREIGN KEY (`CarRentalStationId`) REFERENCES `RentalStation` (`RentalStationId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarRentalStation`
--

LOCK TABLES `CarRentalStation` WRITE;
/*!40000 ALTER TABLE `CarRentalStation` DISABLE KEYS */;
INSERT INTO `CarRentalStation` VALUES (1,1),(2,2),(3,1),(4,1),(3,5),(3,6),(1,7),(1,8),(1,9),(3,10);
/*!40000 ALTER TABLE `CarRentalStation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Color`
--

DROP TABLE IF EXISTS `Color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Color` (
  `ColorId` smallint unsigned NOT NULL AUTO_INCREMENT,
  `ColorName` varchar(45) NOT NULL,
  PRIMARY KEY (`ColorId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Color`
--

LOCK TABLES `Color` WRITE;
/*!40000 ALTER TABLE `Color` DISABLE KEYS */;
INSERT INTO `Color` VALUES (1,'Red'),(2,'Blue'),(3,'Green'),(4,'White'),(5,'Purple'),(6,'Yellow');
/*!40000 ALTER TABLE `Color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `CustomerId` int unsigned NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  PRIMARY KEY (`CustomerId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Adam','Johansson'),(2,'Bengt','Bengtsson'),(3,'Maria','Salvander'),(4,'Jörgen','Terven'),(5,'Pakko','Alijärvi'),(6,'Eva','Dahlgren');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomerPhone`
--

DROP TABLE IF EXISTS `CustomerPhone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CustomerPhone` (
  `CustomerId` int unsigned NOT NULL,
  `PhoneId` int unsigned NOT NULL,
  KEY `fk_CustomerPhone_Customer` (`CustomerId`),
  KEY `fk_CustomerPhone_Phone1` (`PhoneId`),
  CONSTRAINT `fk_CustomerPhone_Customer` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`),
  CONSTRAINT `fk_CustomerPhone_Phone1` FOREIGN KEY (`PhoneId`) REFERENCES `Phone` (`PhoneId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomerPhone`
--

LOCK TABLES `CustomerPhone` WRITE;
/*!40000 ALTER TABLE `CustomerPhone` DISABLE KEYS */;
INSERT INTO `CustomerPhone` VALUES (1,1),(1,3),(2,2),(3,4),(4,5),(5,6),(5,8),(6,7);
/*!40000 ALTER TABLE `CustomerPhone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomerRental`
--

DROP TABLE IF EXISTS `CustomerRental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CustomerRental` (
  `CustomerId` int unsigned NOT NULL,
  `RentalStationId` int unsigned NOT NULL,
  `CarId` int unsigned NOT NULL,
  `RentFrom` date NOT NULL,
  `RentTo` date NOT NULL,
  KEY `RentStart` (`RentFrom`),
  KEY `RentEnd` (`RentTo`),
  KEY `fk_CustomerRental_RentalStation1` (`RentalStationId`),
  KEY `fk_CustomerRental_Car1` (`CarId`),
  KEY `fk_CustomerRental_Customer1` (`CustomerId`),
  CONSTRAINT `fk_CustomerRental_Car1` FOREIGN KEY (`CarId`) REFERENCES `Car` (`CarId`),
  CONSTRAINT `fk_CustomerRental_Customer1` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`),
  CONSTRAINT `fk_CustomerRental_RentalStation1` FOREIGN KEY (`RentalStationId`) REFERENCES `RentalStation` (`RentalStationId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomerRental`
--

LOCK TABLES `CustomerRental` WRITE;
/*!40000 ALTER TABLE `CustomerRental` DISABLE KEYS */;
INSERT INTO `CustomerRental` VALUES (1,1,4,'2013-03-10','2013-03-17'),(2,3,5,'2013-03-16','2013-03-17'),(3,2,2,'2012-11-10','2012-11-24'),(1,1,3,'2011-04-14','2011-04-14'),(5,4,7,'2013-03-07','2013-03-16'),(6,1,9,'2013-04-05','2013-05-05'),(2,3,4,'2013-03-18','2013-03-19'),(4,1,6,'2013-02-20','2013-03-12');
/*!40000 ALTER TABLE `CustomerRental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Phone`
--

DROP TABLE IF EXISTS `Phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Phone` (
  `PhoneId` int unsigned NOT NULL,
  `PhoneType` enum('CELL','WORK','HOME') NOT NULL,
  `Number` bigint unsigned NOT NULL,
  PRIMARY KEY (`PhoneId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Phone`
--

LOCK TABLES `Phone` WRITE;
/*!40000 ALTER TABLE `Phone` DISABLE KEYS */;
INSERT INTO `Phone` VALUES (1,'CELL',4243234234),(2,'CELL',4564562322),(3,'HOME',2342466734),(4,'HOME',6465465466),(5,'HOME',2436674564),(6,'HOME',6365374574),(7,'HOME',1434645646),(8,'WORK',2346364566),(9,'WORK',5345345436),(10,'WORK',4565463235),(11,'WORK',2343253356),(12,'CELL',3454366747),(13,'CELL',2342325252),(14,'CELL',2345253453);
/*!40000 ALTER TABLE `Phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RentalStation`
--

DROP TABLE IF EXISTS `RentalStation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RentalStation` (
  `RentalStationId` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`RentalStationId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RentalStation`
--

LOCK TABLES `RentalStation` WRITE;
/*!40000 ALTER TABLE `RentalStation` DISABLE KEYS */;
INSERT INTO `RentalStation` VALUES (1,'Stockholm'),(2,'Göteborg'),(3,'Malmö'),(4,'Sundsvall');
/*!40000 ALTER TABLE `RentalStation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-11 19:17:00
