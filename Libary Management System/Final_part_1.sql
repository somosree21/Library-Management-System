-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2021 at 08:39 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_t`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_details`
--

CREATE TABLE `book_details` (
  `isbn` int(40) NOT NULL,
  `stu_id` int(40) NOT NULL,
  `b_name` varchar(40) NOT NULL,
  `auth` varchar(40) NOT NULL,
  `fine` int(40) NOT NULL,
  `issue_dt` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_details`
--

INSERT INTO `book_details` (`isbn`, `stu_id`, `b_name`, `auth`, `fine`, `issue_dt`, `status`) VALUES
(1006, 5256, 'Objective Math', 'R.S Agarwal', 3324, '2012-03-14', 1),
(1015, 1569, 'GK', 'Smbst', 0, '2021-05-05', 1),
(1024, 5613, 'Python', 'Manna', 0, '2021-05-19', 1),
(1026, 5531, 'Biology', 'R.g kar', 0, '2021-05-19', 1),
(1027, 5531, 'Night Sleep', 'W.K', 0, '2021-05-19', 1),
(1028, 5531, 'Alice in wounderland', 'Soumyadip', 0, '2021-05-19', 1),
(1029, 5566, 'Python', 'Manna', 0, '2021-05-18', 1),
(1030, 0, 'Python', 'Manna', 0, '0000-00-00', 1),
(1031, 0, 'Python', 'Manna', 0, '0000-00-00', 1),
(1032, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1033, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1034, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1035, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1036, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1037, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1038, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1039, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1040, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0),
(1041, 0, 'Objective Math', 'R.S Agarwal', 0, '0000-00-00', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
