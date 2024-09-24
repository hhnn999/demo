-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2021 at 11:49 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlsbai`
--

-- --------------------------------------------------------

--
-- Table structure for table `ban`
--

CREATE TABLE `ban` (
  `idban` bigint(20) NOT NULL,
  `tenban` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `trangthaiban` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `ban`
--

INSERT INTO `ban` (`idban`, `tenban`, `trangthaiban`) VALUES
(1, 'BAN1', '-1'),
(2, 'BAN2', '-1'),
(3, 'BAN3', '-1');

-- --------------------------------------------------------

--
-- Table structure for table `bgsan`
--

CREATE TABLE `bgsan` (
  `id` bigint(20) NOT NULL,
  `idsan` bigint(20) DEFAULT NULL,
  `ngayapdung` date NOT NULL,
  `loaisan` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tugio` time(6) NOT NULL,
  `dengio` time(6) NOT NULL,
  `dongia` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bgsan`
--

INSERT INTO `bgsan` (`id`, `idsan`, `ngayapdung`, `loaisan`, `tugio`, `dengio`, `dongia`) VALUES
(4, NULL, '2020-01-01', 'SAN 5', '17:00:00.000000', '21:00:00.000000', '400000'),
(8, NULL, '2020-01-01', 'SAN 7', '17:00:00.000000', '21:00:00.000000', '600000'),
(11, NULL, '2020-01-01', 'SAN 11', '17:00:00.000000', '21:00:00.000000', '800000');

-- --------------------------------------------------------

--
-- Table structure for table `chitietdvau`
--

CREATE TABLE `chitietdvau` (
  `id` bigint(20) NOT NULL,
  `idhoadon` bigint(20) DEFAULT NULL,
  `idsanpham` bigint(20) DEFAULT NULL,
  `soluong` float DEFAULT NULL,
  `dongia` float DEFAULT NULL,
  `thanhtien` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietdvau`
--

INSERT INTO `chitietdvau` (`id`, `idhoadon`, `idsanpham`, `soluong`, `dongia`, `thanhtien`) VALUES
(1, 1, 1, 2, 3000, 6000),
(2, 2, 2, 3, 4000, 12000);

-- --------------------------------------------------------

--
-- Table structure for table `chitietdvpk`
--

CREATE TABLE `chitietdvpk` (
  `id` bigint(20) NOT NULL,
  `idhoadon` bigint(20) DEFAULT NULL,
  `idphukien` bigint(20) DEFAULT NULL,
  `soluong` float DEFAULT NULL,
  `giomuon` datetime DEFAULT NULL,
  `giotra` datetime DEFAULT NULL,
  `thanhtien` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietdvpk`
--

INSERT INTO `chitietdvpk` (`id`, `idhoadon`, `idphukien`, `soluong`, `giomuon`, `giotra`, `thanhtien`) VALUES
(1, 1, 1, 2, '2021-04-12 17:00:00', '2021-04-12 18:00:00', 70000),
(2, 2, 2, 1, '2021-04-12 17:00:00', '2021-04-12 18:00:00', 5000000);

-- --------------------------------------------------------

--
-- Table structure for table `chitietdvsan`
--

CREATE TABLE `chitietdvsan` (
  `id` bigint(20) NOT NULL,
  `idhoadon` bigint(20) DEFAULT NULL,
  `idsan` bigint(20) DEFAULT NULL,
  `giovao` datetime DEFAULT NULL,
  `giora` datetime DEFAULT NULL,
  `thanhtien` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietdvsan`
--

INSERT INTO `chitietdvsan` (`id`, `idhoadon`, `idsan`, `giovao`, `giora`, `thanhtien`) VALUES
(1, 1, 1, '2021-04-12 17:00:00', '2021-04-12 18:00:00', 400000),
(2, 2, 2, '2021-04-12 18:00:00', '2021-04-12 19:00:00', 500000);

-- --------------------------------------------------------

--
-- Table structure for table `chitietnhap`
--

CREATE TABLE `chitietnhap` (
  `id` bigint(20) NOT NULL,
  `idphieunhap` bigint(20) DEFAULT NULL,
  `idsanpham` bigint(20) DEFAULT NULL,
  `soluong` float DEFAULT NULL,
  `gianhap` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietnhap`
--

INSERT INTO `chitietnhap` (`id`, `idphieunhap`, `idsanpham`, `soluong`, `gianhap`) VALUES
(1, 1, 1, 8, 30000),
(3, 3, 2, 6, 8000),
(2, 2, 2, 4, 35000);

-- --------------------------------------------------------

--
-- Table structure for table `chitietphieukho`
--

CREATE TABLE `chitietphieukho` (
  `id` bigint(20) NOT NULL,
  `IDphieu` bigint(20) NOT NULL,
  `IDsanpham` bigint(20) NOT NULL,
  `Soluong` float NOT NULL,
  `Nguonnhap` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietphieukho`
--

INSERT INTO `chitietphieukho` (`id`, `IDphieu`, `IDsanpham`, `Soluong`, `Nguonnhap`) VALUES
(1, 1, 1, 3, 'nasa'),
(2, 2, 2, 2, 'my');

-- --------------------------------------------------------

--
-- Table structure for table `chitietxuat`
--

CREATE TABLE `chitietxuat` (
  `id` bigint(20) NOT NULL,
  `idphieuxuat` bigint(20) DEFAULT NULL,
  `idsanpham` bigint(20) DEFAULT NULL,
  `soluong` float DEFAULT NULL,
  `dongia` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chitietxuat`
--

INSERT INTO `chitietxuat` (`id`, `idphieuxuat`, `idsanpham`, `soluong`, `dongia`) VALUES
(1, 1, 1, 2, 2000),
(2, 2, 2, 5, 8000);

-- --------------------------------------------------------

--
-- Table structure for table `congnokh`
--

CREATE TABLE `congnokh` (
  `id` bigint(20) NOT NULL,
  `idkhachhang` bigint(20) NOT NULL,
  `idhinhthuc` bigint(20) DEFAULT NULL,
  `tongtienno` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `congnokh`
--

INSERT INTO `congnokh` (`id`, `idkhachhang`, `idhinhthuc`, `tongtienno`) VALUES
(1, 1, 1, 50000),
(2, 2, 2, 50000);

-- --------------------------------------------------------

--
-- Table structure for table `congnoncc`
--

CREATE TABLE `congnoncc` (
  `idnhacungcap` bigint(20) NOT NULL,
  `idhinhthuc` bigint(20) NOT NULL,
  `tongtien` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `congnoncc`
--

INSERT INTO `congnoncc` (`idnhacungcap`, `idhinhthuc`, `tongtien`) VALUES
(1, 1, 80000),
(2, 2, 8000000);

-- --------------------------------------------------------

--
-- Table structure for table `danhsachsan`
--

CREATE TABLE `danhsachsan` (
  `idsan` bigint(20) NOT NULL,
  `loaisan` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `khuvuc` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `trangthaisan` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `danhsachsan`
--

INSERT INTO `danhsachsan` (`idsan`, `loaisan`, `khuvuc`, `trangthaisan`) VALUES
(1, 'san 7', 'Cau Giay', '1'),
(2, 'san 9', 'Tran duy hung', '2'),
(3, 'san 7', 'nam dinh', '0');

-- --------------------------------------------------------

--
-- Table structure for table `datban`
--

CREATE TABLE `datban` (
  `id` bigint(20) NOT NULL,
  `idban` bigint(20) DEFAULT NULL,
  `idkhach` bigint(20) DEFAULT NULL,
  `giovao` datetime DEFAULT NULL,
  `giora` datetime DEFAULT NULL,
  `datcoc` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `datban`
--

INSERT INTO `datban` (`id`, `idban`, `idkhach`, `giovao`, `giora`, `datcoc`) VALUES
(1, 1, 1, '2021-04-12 06:00:00', '2021-04-12 09:00:00', 500000);

-- --------------------------------------------------------

--
-- Table structure for table `datpk`
--

CREATE TABLE `datpk` (
  `id` bigint(20) NOT NULL,
  `idpk` bigint(20) DEFAULT NULL,
  `idkhach` bigint(20) DEFAULT NULL,
  `giovao` datetime DEFAULT NULL,
  `giora` datetime DEFAULT NULL,
  `datcoc` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `datpk`
--

INSERT INTO `datpk` (`id`, `idpk`, `idkhach`, `giovao`, `giora`, `datcoc`) VALUES
(1, 1, 1, '2021-04-12 12:00:00', '2021-04-12 14:00:00', 500),
(2, 2, 2, '2021-04-12 20:00:00', '2021-04-12 21:00:00', 3000);

-- --------------------------------------------------------

--
-- Table structure for table `datsan`
--

CREATE TABLE `datsan` (
  `id` bigint(20) NOT NULL,
  `idsan` bigint(20) DEFAULT NULL,
  `idkhach` bigint(20) DEFAULT NULL,
  `giovao` datetime DEFAULT NULL,
  `giora` datetime DEFAULT NULL,
  `datcoc` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `datsan`
--

INSERT INTO `datsan` (`id`, `idsan`, `idkhach`, `giovao`, `giora`, `datcoc`) VALUES
(1, 1, 1, '2021-04-12 09:00:00', '2021-04-12 10:00:00', 500000),
(2, 2, 2, '2021-04-12 15:00:00', '2021-04-12 16:00:00', 600000);

-- --------------------------------------------------------

--
-- Table structure for table `doituongtt`
--

CREATE TABLE `doituongtt` (
  `id` bigint(20) NOT NULL,
  `iddoituong` bigint(20) NOT NULL,
  `tendoituong` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `doituongtt`
--

INSERT INTO `doituongtt` (`id`, `iddoituong`, `tendoituong`) VALUES
(1, 1, 'tien thu san'),
(2, 2, 'tien nhap hang');

-- --------------------------------------------------------

--
-- Table structure for table `hoadon`
--

CREATE TABLE `hoadon` (
  `id` bigint(20) NOT NULL,
  `code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `idkhachhang` bigint(20) DEFAULT NULL,
  `idnhanvien` bigint(20) DEFAULT NULL,
  `idkhuvuc` bigint(20) DEFAULT NULL,
  `idhinhthuc` bigint(20) DEFAULT NULL,
  `giovao` datetime DEFAULT NULL,
  `giora` datetime DEFAULT NULL,
  `tongtien` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `hoadon`
--

INSERT INTO `hoadon` (`id`, `code`, `idkhachhang`, `idnhanvien`, `idkhuvuc`, `idhinhthuc`, `giovao`, `giora`, `tongtien`) VALUES
(1, 'NT1', 1, 1, 1, 1, '2021-04-12 12:00:00', '2021-04-12 13:00:00', 10000),
(2, 'NT2', 2, 2, 2, 2, '2021-04-12 09:00:00', '2021-04-12 10:00:00', 30000);

-- --------------------------------------------------------

--
-- Table structure for table `htthanhtoan`
--

CREATE TABLE `htthanhtoan` (
  `id` bigint(20) NOT NULL,
  `tenhinhthuc` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `htthanhtoan`
--

INSERT INTO `htthanhtoan` (`id`, `tenhinhthuc`) VALUES
(1, 'Tiền mặt'),
(2, 'Chuyển khoản');

-- --------------------------------------------------------

--
-- Table structure for table `khachhang`
--

CREATE TABLE `khachhang` (
  `id` bigint(20) NOT NULL,
  `tenkh` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `diachi` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sdt` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `khachhang`
--

INSERT INTO `khachhang` (`id`, `tenkh`, `diachi`, `sdt`) VALUES
(1, 'Nguyễn Văn A', '99 Trung Kính', '0359847895'),
(2, 'Trần Thị B', '12 Nguyễn Khánh Toàn', '0864598752'),
(3, 'Phạm Văn C', '10 Cầu Giấy', '0874563214');

-- --------------------------------------------------------

--
-- Table structure for table `khuvuc`
--

CREATE TABLE `khuvuc` (
  `id` bigint(20) NOT NULL,
  `tenkv` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `diachi` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `khuvuc`
--

INSERT INTO `khuvuc` (`id`, `tenkv`, `diachi`) VALUES
(1, 'DV', 'Cầu Giấy'),
(2, 'PK', 'Phạm Văn Đồng');

-- --------------------------------------------------------

--
-- Table structure for table `nhaccap`
--

CREATE TABLE `nhaccap` (
  `id` bigint(20) NOT NULL,
  `tennccap` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nhanvien`
--

CREATE TABLE `nhanvien` (
  `id` bigint(20) NOT NULL,
  `tennv` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ngaysinh` date DEFAULT NULL,
  `diachi` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sdt` char(10) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `nhanvien`
--

INSERT INTO `nhanvien` (`id`, `tennv`, `ngaysinh`, `diachi`, `sdt`) VALUES
(1, 'NGUYEN VAN A', '1999-01-01', 'NH', '0987654321'),
(2, 'NGUYEN VAN B', '2000-09-06', 'TB', '0999999999'),
(3, 'NGUYEN VAN C', '1997-09-11', 'ND', '0988888666');

-- --------------------------------------------------------

--
-- Table structure for table `phieunhap`
--

CREATE TABLE `phieunhap` (
  `idphieunhap` bigint(20) NOT NULL,
  `ngaynhap` datetime DEFAULT NULL,
  `idnhanvien` bigint(20) DEFAULT NULL,
  `ghichu` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `phieunhap`
--

INSERT INTO `phieunhap` (`idphieunhap`, `ngaynhap`, `idnhanvien`, `ghichu`) VALUES
(1, '2021-02-22 00:00:00', 1, 'abcd'),
(2, '2021-06-12 00:00:00', 2, 'grưtg'),
(3, '2021-06-15 00:00:00', 3, 'gbt');

-- --------------------------------------------------------

--
-- Table structure for table `phukien`
--

CREATE TABLE `phukien` (
  `id` bigint(20) NOT NULL,
  `tenphukien` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dongia` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `phukien`
--

INSERT INTO `phukien` (`id`, `tenphukien`, `dongia`) VALUES
(1, 'Găng tay', 70000),
(2, 'Giày bóng', 300000),
(3, 'Áo', 200000);

-- --------------------------------------------------------

--
-- Table structure for table `sanpham`
--

CREATE TABLE `sanpham` (
  `idsanpham` bigint(20) NOT NULL,
  `idloaisanpham` bigint(20) NOT NULL,
  `tensanpham` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `sanpham`
--

INSERT INTO `sanpham` (`idsanpham`, `idloaisanpham`, `tensanpham`) VALUES
(1, 1, 'Bánh mì'),
(2, 0, 'Coca'),
(3, 0, '7up');

-- --------------------------------------------------------

--
-- Table structure for table `tonkhopk`
--

CREATE TABLE `tonkhopk` (
  `id` bigint(20) NOT NULL,
  `idpk` bigint(20) DEFAULT NULL,
  `soluongdauky` float DEFAULT NULL,
  `soluongcuoiky` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tonkhopk`
--

INSERT INTO `tonkhopk` (`id`, `idpk`, `soluongdauky`, `soluongcuoiky`) VALUES
(1, 1, 3, 2),
(2, 2, 8, 3),
(3, 3, 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `tonkhosp`
--

CREATE TABLE `tonkhosp` (
  `id` bigint(20) NOT NULL,
  `idsanpham` bigint(20) DEFAULT NULL,
  `soluongdauky` float DEFAULT NULL,
  `soluongcuoiky` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tonkhosp`
--

INSERT INTO `tonkhosp` (`id`, `idsanpham`, `soluongdauky`, `soluongcuoiky`) VALUES
(1, 1, 4, 3),
(2, 2, 6, 2),
(3, 3, 5, 6);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ban`
--
ALTER TABLE `ban`
  ADD PRIMARY KEY (`idban`);

--
-- Indexes for table `bgsan`
--
ALTER TABLE `bgsan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietdvau`
--
ALTER TABLE `chitietdvau`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietdvpk`
--
ALTER TABLE `chitietdvpk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietdvsan`
--
ALTER TABLE `chitietdvsan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietnhap`
--
ALTER TABLE `chitietnhap`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietphieukho`
--
ALTER TABLE `chitietphieukho`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chitietxuat`
--
ALTER TABLE `chitietxuat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `congnokh`
--
ALTER TABLE `congnokh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `congnoncc`
--
ALTER TABLE `congnoncc`
  ADD PRIMARY KEY (`idnhacungcap`);

--
-- Indexes for table `danhsachsan`
--
ALTER TABLE `danhsachsan`
  ADD PRIMARY KEY (`idsan`);

--
-- Indexes for table `datban`
--
ALTER TABLE `datban`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `datpk`
--
ALTER TABLE `datpk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `datsan`
--
ALTER TABLE `datsan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doituongtt`
--
ALTER TABLE `doituongtt`
  ADD PRIMARY KEY (`iddoituong`);

--
-- Indexes for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `htthanhtoan`
--
ALTER TABLE `htthanhtoan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `khachhang`
--
ALTER TABLE `khachhang`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `khuvuc`
--
ALTER TABLE `khuvuc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nhaccap`
--
ALTER TABLE `nhaccap`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `phieunhap`
--
ALTER TABLE `phieunhap`
  ADD PRIMARY KEY (`idphieunhap`);

--
-- Indexes for table `phukien`
--
ALTER TABLE `phukien`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`idsanpham`);

--
-- Indexes for table `tonkhopk`
--
ALTER TABLE `tonkhopk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tonkhosp`
--
ALTER TABLE `tonkhosp`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
