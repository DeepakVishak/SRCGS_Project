-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 16, 2021 at 12:09 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `send_success_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `sender_receiver_data`
--

CREATE TABLE `sender_receiver_data` (
  `tid` int(11) NOT NULL,
  `roll_no` int(11) NOT NULL,
  `stud_name` varchar(50) NOT NULL,
  `class` varchar(20) NOT NULL,
  `division` varchar(20) NOT NULL,
  `p_name` varchar(50) NOT NULL,
  `p_mailid` varchar(50) NOT NULL,
  `exam_name` varchar(50) NOT NULL,
  `aca_year` varchar(20) NOT NULL,
  `no_sub` int(11) NOT NULL,
  `mark_sub` int(11) NOT NULL,
  `tr_name` varchar(50) NOT NULL,
  `tr_mailid` varchar(50) NOT NULL,
  `total` float NOT NULL,
  `percent` float NOT NULL,
  `date_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sender_receiver_data`
--
ALTER TABLE `sender_receiver_data`
  ADD PRIMARY KEY (`tid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sender_receiver_data`
--
ALTER TABLE `sender_receiver_data`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
