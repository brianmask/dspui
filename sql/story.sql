-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dspui
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB-0ubuntu0.18.04.2

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
-- Table structure for table `api_story`
--

DROP TABLE IF EXISTS `api_story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_story` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `position` double NOT NULL,
  `icon` varchar(65) NOT NULL,
  `is_story` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_story`
--

LOCK TABLES `api_story` WRITE;
/*!40000 ALTER TABLE `api_story` DISABLE KEYS */;
INSERT INTO `api_story` VALUES (1,'Client Setup',2,'settings',1),(2,'Connect to the Server',2,'cast_connected',1);
/*!40000 ALTER TABLE `api_story` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_storyboard`
--

DROP TABLE IF EXISTS `api_storyboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_storyboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` double NOT NULL,
  `name` varchar(65) NOT NULL,
  `text` longtext NOT NULL,
  `story_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_storyboard_story_id_bdf59faf_fk_api_story_id` (`story_id`),
  CONSTRAINT `api_storyboard_story_id_bdf59faf_fk_api_story_id` FOREIGN KEY (`story_id`) REFERENCES `api_story` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_storyboard`
--

LOCK TABLES `api_storyboard` WRITE;
/*!40000 ALTER TABLE `api_storyboard` DISABLE KEYS */;
INSERT INTO `api_storyboard` VALUES (1,1,'Installing FFXI','<strong>In this section we will install and update Final Fantasy XI from Retail Discs.</strong>\r\n<br />\r\n<p>Even if you have CD\'s I would download from POL due to the new install client having most updates already installed.</p>\r\n<a href=\"http://www.playonline.com/ff11us/download/media/install_win.html\" target=\"_blank\">\r\nhttp://www.playonline.com/ff11us/download/media/install_win.html\r\n</a>\r\n<ul>\r\n<li>Install POL (use appropriate version for your system)</li>\r\n<li>Install FFXI</li>\r\n<li>Install Rise of the Zilart</li>\r\n<li>Install Chains of Promathia</li>\r\n<li>Install Treasures of Aht Urghan</li>\r\n<li>Install Wings of the Goddess</li>\r\n</ul>\r\n<p>Time to update!</p>\r\n<br />\r\n<strong>The next page will describe how to update the client.</strong>',1),(2,2,'Preparing For Updates','<ul>\r\n<li>Run <strong>PlayOnline.</strong> When it first runs it will prompt you to update, do it.</li>\r\n<li>After the update for POL is done and restarted it will ask you if you\'re a New User or Existing User.</li>\r\n<li><strong>Choose Existing User</strong> using 1234567 as username/pass/account id etc.</li>\r\n</ul>\r\nUnregistered PlayOnline Account made! Time for the next step.',1),(3,3,'Updating Final Fantasy XI','<p>Download the patch file: <a href=\"/static/files/patch.zip\">Here</a></p>\r\n<ul>\r\n<li>Open the file using an archiving program</li>\r\n<li>Extract to a new directory e.g. c:\\patch</li>\r\n<li>Close your archiving program</li>\r\n<li>Navigate to c:\\patch</li>\r\n<li>Single left-click anywhere in the folder and press Ctrl+A</li>\r\n<li>Once you see everything highlighted press Ctrl+C</li>\r\n<li>Navigate to the directory you installed Final Fantasy XI.</li>\r\n<ul>\r\n<li>(For 64-bit systems, the default location is C:\\Program Files (x86)\\PlayOnline\\SquareEnix\\FINAL FANTASY XI\\)</li>\r\n<li>(For 32-bit systems, the default location is C:\\Program Files\\PlayOnline\\SquareEnix\\FINAL FANTASY XI\\)</li>\r\n</ul><br />\r\n<li>Paste those files you copied from C:\\Patch to /FINAL FANTASY XI/ directory.</li>\r\n<li>Single left click any where in the directory and hold Ctrl+V</li>\r\n<li>When prompted to overwrite the files say Yes to All</li>\r\n<li>Close windows explorer.</li><br />\r\n<li>Run PlayOnline. On the left side of the screen click Check Files</li>\r\n<li>On the next screen where it says \"PlayOnlineViewer\" click the two arrows and change it to \"Final Fantasy XI\". The \"version\" should be \"UNKNOWN\", **if it does not work then redo Step 3 and carry on following from there**</li>\r\n<li>Click on the Check Files button.</li>\r\n<li>PlayOnline will then check all the FINAL FANTASY XI files (usually takes about 15-20 minutes) and prompt you on what to do because it found errors.</li>\r\n<li>You should then choose to fix the errors. They are errors after all and need to be fixed.</li>\r\n<li>PlayOnline will then automatically start checking and updating files. This takes around ~20 minutes with new client install, 5-10hrs with the old. Once it starts downloading you can leave it unattentended if you wish to do so (best to do this overnight as PlayOnline servers are sloooooooooooooooooow)</li>\r\n<li>Once you\'re done updating, navigate to /PlayOnlineViewer/.</li>\r\n<li>Right-click the \"data\" folder and click copy</li>\r\n<li>Navigate to /FINAL FANTASY XI/, right click an empty space in the folder and click paste. You should now have the \"data\" folder inside your /FINAL FANTASY XI/ folder.</li>\r\n</ul>',1),(4,1,'Setting up the Launcher','<p><strong>In this section you will configure FFXI to connect to Ranik\'s Realm Private Server</strong></p>\r\n<p>We\'ll focus on using Ashita, as it has a nice feature set and is great for connecting to private servers.</p>\r\n<p>You can also use windower or xiloader directly if you want, but won\'t find instructions here on the details.</p><br />\r\n<a href=\"https://www.ashitaxi.com/\" target=\"_blank\">First, download Ashita here, and continue to the next page</a>',2);
/*!40000 ALTER TABLE `api_storyboard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-02 19:56:48
