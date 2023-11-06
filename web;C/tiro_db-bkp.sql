-- MariaDB dump 10.19-11.1.2-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: tiro_db
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB-1:11.1.2+maria~ubu2204

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ammo`
--

DROP TABLE IF EXISTS `ammo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ammo` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `a_weapon` int(11) DEFAULT NULL,
  `a_vi` int(11) DEFAULT NULL,
  `a_ratio` int(11) DEFAULT NULL,
  `a_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ammo`
--

LOCK TABLES `ammo` WRITE;
/*!40000 ALTER TABLE `ammo` DISABLE KEYS */;
INSERT INTO `ammo` VALUES
(1,1,65,7,'65.m/s'),
(2,6,68,12,'68.m/s'),
(3,1,126,7,'126.m/s'),
(4,1,170,7,'170.m/s'),
(5,6,204,12,'204.m/s'),
(6,1,208,7,'208.m/s'),
(7,6,120,12,'120.m/s');
/*!40000 ALTER TABLE `ammo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bandos`
--

DROP TABLE IF EXISTS `bandos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bandos` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bandos`
--

LOCK TABLES `bandos` WRITE;
/*!40000 ALTER TABLE `bandos` DISABLE KEYS */;
INSERT INTO `bandos` VALUES
(1,'Rusia'),
(2,'Ucrania'),
(3,'Rebeldes'),
(4,'USA'),
(5,'Wagner');
/*!40000 ALTER TABLE `bandos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codigos`
--

DROP TABLE IF EXISTS `codigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `codigos` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_tipo` varchar(5) DEFAULT NULL,
  `c_descrip` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codigos`
--

LOCK TABLES `codigos` WRITE;
/*!40000 ALTER TABLE `codigos` DISABLE KEYS */;
/*!40000 ALTER TABLE `codigos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disparo`
--

DROP TABLE IF EXISTS `disparo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disparo` (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `d_lato` float DEFAULT NULL,
  `d_lono` float DEFAULT NULL,
  `d_latd` float DEFAULT NULL,
  `d_lond` float DEFAULT NULL,
  `d_time` timestamp NULL DEFAULT current_timestamp(),
  `m_id` int(11) DEFAULT NULL,
  `b_id` int(11) DEFAULT NULL,
  `w_id` int(11) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `d_dist` int(11) DEFAULT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disparo`
--

LOCK TABLES `disparo` WRITE;
/*!40000 ALTER TABLE `disparo` DISABLE KEYS */;
INSERT INTO `disparo` VALUES
(3,-34.7565,-58.5078,-34.7579,-58.5118,'2023-11-05 20:43:19',4,2,1,1,391),
(4,-34.7565,-58.5078,-34.7587,-58.5117,'2023-11-05 23:21:09',4,2,1,1,427),
(5,-34.7565,-58.5078,-34.7595,-58.5125,'2023-11-05 23:31:20',4,2,1,2,542),
(6,-34.7565,-58.5078,-34.7605,-58.5137,'2023-11-05 23:32:39',4,2,1,2,691),
(7,-34.7603,-58.5032,-34.7526,-58.4972,'2023-11-06 20:03:28',4,1,6,5,1014),
(8,-34.7603,-58.5032,-34.7542,-58.5066,'2023-11-06 20:05:37',4,1,6,5,741),
(9,-34.7603,-58.5032,-34.7559,-58.5063,'2023-11-06 20:13:22',4,1,6,7,560);
/*!40000 ALTER TABLE `disparo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventlog`
--

DROP TABLE IF EXISTS `eventlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventlog` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_eid` int(11) DEFAULT NULL,
  `l_mid` int(11) DEFAULT NULL,
  `l_codeid` int(11) DEFAULT NULL,
  `l_note` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`l_id`),
  KEY `l_eid` (`l_eid`),
  KEY `l_mid` (`l_mid`),
  KEY `l_codeid` (`l_codeid`),
  CONSTRAINT `eventlog_ibfk_1` FOREIGN KEY (`l_eid`) REFERENCES `eventos` (`e_id`),
  CONSTRAINT `eventlog_ibfk_2` FOREIGN KEY (`l_mid`) REFERENCES `mapas` (`m_id`),
  CONSTRAINT `eventlog_ibfk_3` FOREIGN KEY (`l_codeid`) REFERENCES `codigos` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventlog`
--

LOCK TABLES `eventlog` WRITE;
/*!40000 ALTER TABLE `eventlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `eventlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventos`
--

DROP TABLE IF EXISTS `eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventos` (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_nom` varchar(40) DEFAULT NULL,
  `e_time` timestamp NULL DEFAULT current_timestamp(),
  `e_fecha` date DEFAULT NULL,
  `e_bandos` int(11) DEFAULT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventos`
--

LOCK TABLES `eventos` WRITE;
/*!40000 ALTER TABLE `eventos` DISABLE KEYS */;
INSERT INTO `eventos` VALUES
(2,'Partida Testeo','2023-10-28 15:31:23','2023-10-29',2);
/*!40000 ALTER TABLE `eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_maps`
--

DROP TABLE IF EXISTS `events_maps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events_maps` (
  `elemento_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_id` int(11) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL,
  PRIMARY KEY (`elemento_id`),
  KEY `m_id` (`m_id`),
  CONSTRAINT `events_maps_ibfk_1` FOREIGN KEY (`m_id`) REFERENCES `mapas` (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_maps`
--

LOCK TABLES `events_maps` WRITE;
/*!40000 ALTER TABLE `events_maps` DISABLE KEYS */;
/*!40000 ALTER TABLE `events_maps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mapas`
--

DROP TABLE IF EXISTS `mapas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mapas` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_nom` varchar(40) DEFAULT NULL,
  `m_time` timestamp NULL DEFAULT current_timestamp(),
  `m_eid` int(11) DEFAULT NULL,
  `m_lat` float DEFAULT NULL,
  `m_lon` float DEFAULT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mapas`
--

LOCK TABLES `mapas` WRITE;
/*!40000 ALTER TABLE `mapas` DISABLE KEYS */;
INSERT INTO `mapas` VALUES
(4,'Tablero General','2023-10-28 20:52:26',2,-34.757,-58.5114),
(5,'Test1','2023-11-02 21:05:45',NULL,-34.757,-58.5114);
/*!40000 ALTER TABLE `mapas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetos`
--

DROP TABLE IF EXISTS `objetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objetos` (
  `o_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_id` int(11) DEFAULT NULL,
  `o_lat` float DEFAULT NULL,
  `o_lng` float DEFAULT NULL,
  `b_id` int(11) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`o_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetos`
--

LOCK TABLES `objetos` WRITE;
/*!40000 ALTER TABLE `objetos` DISABLE KEYS */;
INSERT INTO `objetos` VALUES
(1,2,-34.7568,-58.506,2,4),
(2,1,-34.7636,-58.5095,1,4),
(3,3,-34.7559,-58.5064,2,4),
(4,1,-34.7554,-58.5064,2,4),
(5,4,-34.7603,-58.5134,1,4),
(6,1,-34.7603,-58.5137,1,4);
/*!40000 ALTER TABLE `objetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ses`
--

DROP TABLE IF EXISTS `ses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ses` (
  `ses_session` varchar(40) DEFAULT NULL,
  `ses_users_nom` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ses`
--

LOCK TABLES `ses` WRITE;
/*!40000 ALTER TABLE `ses` DISABLE KEYS */;
INSERT INTO `ses` VALUES
('711694b8-11ed-47ce-bc4d-5871540ff0a6','Kender');
/*!40000 ALTER TABLE `ses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos`
--

DROP TABLE IF EXISTS `tipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipos` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_name` varchar(20) DEFAULT NULL,
  `t_grosor` int(11) DEFAULT NULL,
  `t_size` int(11) DEFAULT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos`
--

LOCK TABLES `tipos` WRITE;
/*!40000 ALTER TABLE `tipos` DISABLE KEYS */;
INSERT INTO `tipos` VALUES
(1,'HQ',5,5),
(2,'Deposito S',5,5),
(3,'Comms S',3,5),
(4,'Comms L',5,5),
(5,'Deposito L',5,10);
/*!40000 ALTER TABLE `tipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `users_id` int(11) NOT NULL AUTO_INCREMENT,
  `users_nom` varchar(20) DEFAULT NULL,
  `users_cat` varchar(1) DEFAULT NULL,
  `users_pwd` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`users_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'admin','S','root_4CD4'),
(3,'kender','A','Astudillo');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapon`
--

DROP TABLE IF EXISTS `weapon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weapon` (
  `w_id` int(11) NOT NULL AUTO_INCREMENT,
  `w_portable` tinyint(1) DEFAULT NULL,
  `w_footprint` int(11) DEFAULT NULL,
  `w_type` int(11) DEFAULT NULL,
  `w_name` varchar(20) DEFAULT NULL,
  `w_calibre` int(11) DEFAULT NULL,
  PRIMARY KEY (`w_id`),
  KEY `w_type` (`w_type`),
  CONSTRAINT `weapon_ibfk_1` FOREIGN KEY (`w_type`) REFERENCES `weapon_types` (`wt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapon`
--

LOCK TABLES `weapon` WRITE;
/*!40000 ALTER TABLE `weapon` DISABLE KEYS */;
INSERT INTO `weapon` VALUES
(1,1,1,1,'M19',60),
(2,1,1,1,'M2',60),
(3,1,1,1,'M224',60),
(4,1,1,1,'M252',81),
(5,1,4,1,'2S12 Sani',120),
(6,1,2,1,'2B14 Podnos',82),
(7,1,1,1,'2B24',82);
/*!40000 ALTER TABLE `weapon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapon_ammo`
--

DROP TABLE IF EXISTS `weapon_ammo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weapon_ammo` (
  `weapon_ammo_id` int(11) NOT NULL AUTO_INCREMENT,
  `weapon_id` int(11) DEFAULT NULL,
  `ammo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`weapon_ammo_id`),
  KEY `weapon_id` (`weapon_id`),
  KEY `ammo_id` (`ammo_id`),
  CONSTRAINT `weapon_ammo_ibfk_1` FOREIGN KEY (`weapon_id`) REFERENCES `weapon` (`w_id`),
  CONSTRAINT `weapon_ammo_ibfk_2` FOREIGN KEY (`ammo_id`) REFERENCES `ammo` (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapon_ammo`
--

LOCK TABLES `weapon_ammo` WRITE;
/*!40000 ALTER TABLE `weapon_ammo` DISABLE KEYS */;
INSERT INTO `weapon_ammo` VALUES
(1,1,1),
(2,1,2),
(3,1,3),
(4,1,4),
(5,1,5),
(8,2,1),
(9,2,2),
(10,2,3),
(11,2,4),
(12,2,5),
(16,3,1),
(17,3,2),
(18,3,3),
(19,3,4),
(20,3,5);
/*!40000 ALTER TABLE `weapon_ammo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapon_types`
--

DROP TABLE IF EXISTS `weapon_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weapon_types` (
  `wt_id` int(11) NOT NULL AUTO_INCREMENT,
  `wt_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`wt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapon_types`
--

LOCK TABLES `weapon_types` WRITE;
/*!40000 ALTER TABLE `weapon_types` DISABLE KEYS */;
INSERT INTO `weapon_types` VALUES
(1,'MORTERO'),
(2,'LANZADERA'),
(3,'OBUS'),
(4,'SILO');
/*!40000 ALTER TABLE `weapon_types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-06 21:31:08
