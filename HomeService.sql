-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: HomeService
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

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
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(15) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `created_by_id` (`created_by_id`),
  CONSTRAINT `accounts_customer_created_by_id_3037fb75_fk_accounts_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'9876543210','Kalanki, Kathmandu','2021-04-20 15:27:30.474255',2);
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_servicemen`
--

DROP TABLE IF EXISTS `accounts_servicemen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_servicemen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(15) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `expertise` varchar(200) DEFAULT NULL,
  `is_available` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `created_by_id` (`created_by_id`),
  CONSTRAINT `accounts_servicemen_created_by_id_123e917a_fk_accounts_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_servicemen`
--

LOCK TABLES `accounts_servicemen` WRITE;
/*!40000 ALTER TABLE `accounts_servicemen` DISABLE KEYS */;
INSERT INTO `accounts_servicemen` VALUES (1,'9876543210','Kathmandu','Plumbing',1,'2021-04-20 15:29:00.722278',3),(2,'9876543210','Kathmandu','Painting',1,'2021-04-20 15:30:12.763490',4),(3,'9876543210','Kathmandu','Cleaning',1,'2021-04-20 15:31:08.799572',5);
/*!40000 ALTER TABLE `accounts_servicemen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_customer` tinyint(1) NOT NULL,
  `is_servicemen` tinyint(1) NOT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$216000$pnRJ5rHCvVqw$wUMcYn3SbABLulC9eAvSuhVugdR9tdlLM9sPJG3DdlM=','2021-04-20 15:52:03.673466',1,'theodis',1,1,'2021-04-20 15:12:57.944921',0,0,NULL,NULL,'admin@homeservice.com'),(2,'pbkdf2_sha256$216000$3GPNFJmPKCc1$l+c3If1BAtonule7ybQRLHxLyv2TO/unJMh57OXwHh0=','2021-04-20 15:50:26.098200',0,'customer',0,1,'2021-04-20 15:27:30.080225',1,0,'Diptan','Regmi','customer@email.com'),(3,'pbkdf2_sha256$216000$6EnKXQpIeBxf$4IhNoz/HlkodPOcIndIPVA6xaXPCu39yWwC36nT2G0I=','2021-04-20 15:50:37.796360',0,'servicemen',0,1,'2021-04-20 15:29:00.187699',0,1,'Aditya','Goyal','aditya@servicemen.com'),(4,'pbkdf2_sha256$216000$DxUpIU4gr31a$ZzGXHw8JsMRn6ow1hCriM8DTawAnrLEkKJOJOECfInI=','2021-04-20 15:30:13.194578',0,'servicemen1',0,1,'2021-04-20 15:30:12.306156',0,1,'Sachin','Thapa','sachin@servicemen.com'),(5,'pbkdf2_sha256$216000$VkRyBrJYl8HM$0XU5yse3u9YANVU325s8EKr6h1a63UcauFTabXJyK8g=','2021-04-20 15:31:09.103016',0,'servicemen2',0,1,'2021-04-20 15:31:08.309091',0,1,'Bibek','Ghimire','bibek@servicemen.com');
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_groups`
--

DROP TABLE IF EXISTS `accounts_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_groups`
--

LOCK TABLES `accounts_user_groups` WRITE;
/*!40000 ALTER TABLE `accounts_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_user_permissions`
--

DROP TABLE IF EXISTS `accounts_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_user_permissions`
--

LOCK TABLES `accounts_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add service',6,'add_service'),(22,'Can change service',6,'change_service'),(23,'Can delete service',6,'delete_service'),(24,'Can view service',6,'view_service'),(25,'Can add order',7,'add_order'),(26,'Can change order',7,'change_order'),(27,'Can delete order',7,'delete_order'),(28,'Can view order',7,'view_order'),(29,'Can add payment',8,'add_payment'),(30,'Can change payment',8,'change_payment'),(31,'Can delete payment',8,'delete_payment'),(32,'Can view payment',8,'view_payment'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add service men',10,'add_servicemen'),(38,'Can change service men',10,'change_servicemen'),(39,'Can delete service men',10,'delete_servicemen'),(40,'Can view service men',10,'view_servicemen'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-04-20 15:36:28.618838','1','1',1,'[{\"added\": {}}]',7,1),(2,'2021-04-20 15:37:14.563329','2','2',1,'[{\"added\": {}}]',7,1),(3,'2021-04-20 15:38:01.964685','3','3',1,'[{\"added\": {}}]',7,1),(4,'2021-04-20 15:40:46.270612','1','1',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1),(5,'2021-04-20 15:40:54.052929','2','2',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1),(6,'2021-04-20 15:41:02.367694','3','3',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1),(7,'2021-04-20 15:42:11.139566','1','1',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1),(8,'2021-04-20 15:42:21.047918','2','2',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1),(9,'2021-04-20 15:43:00.904208','3','3',2,'[{\"changed\": {\"fields\": [\"Servicemen\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'accounts','customer'),(10,'accounts','servicemen'),(9,'accounts','user'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'order','order'),(8,'order','payment'),(6,'service','service'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-20 15:07:08.477980'),(2,'contenttypes','0002_remove_content_type_name','2021-04-20 15:07:13.347184'),(3,'auth','0001_initial','2021-04-20 15:07:17.312947'),(4,'auth','0002_alter_permission_name_max_length','2021-04-20 15:07:30.032089'),(5,'auth','0003_alter_user_email_max_length','2021-04-20 15:07:30.276851'),(6,'auth','0004_alter_user_username_opts','2021-04-20 15:07:30.469974'),(7,'auth','0005_alter_user_last_login_null','2021-04-20 15:07:30.720830'),(8,'auth','0006_require_contenttypes_0002','2021-04-20 15:07:30.841398'),(9,'auth','0007_alter_validators_add_error_messages','2021-04-20 15:07:31.004699'),(10,'auth','0008_alter_user_username_max_length','2021-04-20 15:07:31.209300'),(11,'auth','0009_alter_user_last_name_max_length','2021-04-20 15:07:31.372535'),(12,'auth','0010_alter_group_name_max_length','2021-04-20 15:07:31.838385'),(13,'auth','0011_update_proxy_permissions','2021-04-20 15:07:32.089784'),(14,'auth','0012_alter_user_first_name_max_length','2021-04-20 15:07:32.278164'),(15,'accounts','0001_initial','2021-04-20 15:07:39.614479'),(16,'admin','0001_initial','2021-04-20 15:08:01.602339'),(17,'admin','0002_logentry_remove_auto_add','2021-04-20 15:08:08.540739'),(18,'admin','0003_logentry_add_action_flag_choices','2021-04-20 15:08:08.900456'),(19,'service','0001_initial','2021-04-20 15:08:11.252919'),(20,'order','0001_initial','2021-04-20 15:08:13.877221'),(21,'sessions','0001_initial','2021-04-20 15:08:29.825584');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('p7ffpqjvdrxffik5n3g1unsryeexb5v0','.eJxVjEsOwiAUAO_C2hBo-bp03zMQeLwnVQNJaVfGuxuSLnQ7M5k3C_HYSzg6bmHN7Moku_yyFOGJdYj8iPXeOLS6b2viI-Gn7XxpGV-3s_0blNjL2M6QrQfpjbQWHHkrZpumpARSJCI0c5KgtdLe06ScQ0QjDVAWQpiY2ecL4Pk4Fg:1lYsfT:4613-el-2J_LAU93_8RH-HBjddfX7ZpBl_0mJYKb2Uo','2021-05-04 15:52:03.853024');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order`
--

DROP TABLE IF EXISTS `order_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(2000) DEFAULT NULL,
  `date_ordered` datetime(6) NOT NULL,
  `status` varchar(200) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `service_id` int DEFAULT NULL,
  `servicemen_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_order_customer_id_5bbbd957_fk_accounts_customer_id` (`customer_id`),
  KEY `order_order_service_id_06032452_fk_service_service_id` (`service_id`),
  KEY `order_order_servicemen_id_f76f22e9_fk_accounts_servicemen_id` (`servicemen_id`),
  CONSTRAINT `order_order_customer_id_5bbbd957_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `order_order_service_id_06032452_fk_service_service_id` FOREIGN KEY (`service_id`) REFERENCES `service_service` (`id`),
  CONSTRAINT `order_order_servicemen_id_f76f22e9_fk_accounts_servicemen_id` FOREIGN KEY (`servicemen_id`) REFERENCES `accounts_servicemen` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
INSERT INTO `order_order` VALUES (1,'I need to Pain my Living Room','2021-04-20 15:36:28.616885','Working','Kalanki','Kathmandu',1,1,2),(2,'I need to clean my office carpet floor.','2021-04-20 15:37:14.561308','Reviewed','Dillibazar','Kathmandu',1,2,3),(3,'My basin water fore is low. Please fix it.','2021-04-20 15:38:01.962601','Reviewed','Kalanki','Kathmandu',1,3,1);
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_payment`
--

DROP TABLE IF EXISTS `order_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_payment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `amount` double DEFAULT NULL,
  `complete` tinyint(1) DEFAULT NULL,
  `paid_through` varchar(200) DEFAULT NULL,
  `paid_date` datetime(6) DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_payment_order_id_588933b6_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_payment_order_id_588933b6_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_payment`
--

LOCK TABLES `order_payment` WRITE;
/*!40000 ALTER TABLE `order_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_service`
--

DROP TABLE IF EXISTS `service_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_service` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_service`
--

LOCK TABLES `service_service` WRITE;
/*!40000 ALTER TABLE `service_service` DISABLE KEYS */;
INSERT INTO `service_service` VALUES (1,'Painting','painting','All types of house painting job including interior and exterior painting of house. We also give artistic look to your room.','hands-house-paint-brush-home-services-concept-painter-96100507.jpg'),(2,'Cleaning','cleaning','House Cleaning, Kitchen Cleaning, Water Tank Cleaning, Roof Cleaning, Carpet Cleaning and many more household cleaning job.','images.jpeg'),(3,'Plumbing','plumbing','Water Leakage Problem? Don\'t worry we will fix all kind of leakages. We do also take new fittings orders.','Plumbing-Basics.jpg');
/*!40000 ALTER TABLE `service_service` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-20 22:00:12
