SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `{table_prefix}board` (
  `idx` int(200) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  `id` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `{table_prefix}flag` (
  `{blind_column}1` varchar(200) NOT NULL,
  `{blind_column}2` varchar(200) NOT NULL,
  `{blind_column}3` varchar(200) NOT NULL,
  `{blind_column}4` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `{table_prefix}flag` (`{blind_column}1`, `{blind_column}2`, `{blind_column}3`, `{blind_column}4`) VALUES
('', '', 'flag{flagflagflagffagflaglfaglfag}', '');

CREATE TABLE `{table_prefix}users` (
  `idx` int(200) NOT NULL,
  `id` varchar(300) NOT NULL,
  `pw` varchar(50) NOT NULL,
  `email` varchar(300) NOT NULL,
  `ip` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `{table_prefix}board`
  ADD PRIMARY KEY (`idx`);
  
ALTER TABLE `{table_prefix}users`
  ADD PRIMARY KEY (`idx`);

ALTER TABLE `{table_prefix}board`
  MODIFY `idx` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `{table_prefix}users`
  MODIFY `idx` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;