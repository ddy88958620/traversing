/*
Navicat MySQL Data Transfer

Source Server         : travers
Source Server Version : 50617
Source Host           : 192.168.10.179:3306
Source Database       : traversing_1

Target Server Type    : MYSQL
Target Server Version : 50617
File Encoding         : 65001

Date: 2014-07-11 11:31:31
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `tb_character_info`
-- ----------------------------
DROP TABLE IF EXISTS `tb_character_info`;
CREATE TABLE `tb_character_info` (
  `id` bigint(20) NOT NULL,
  `nickname` varchar(128) DEFAULT '',
  `coin` bigint(20) NOT NULL DEFAULT '0',
  `gold` bigint(20) NOT NULL DEFAULT '0',
  `hero_soul` bigint(20) NOT NULL DEFAULT '0',
  `level` int(11) NOT NULL DEFAULT '1',
  `exp` int(11) NOT NULL DEFAULT '0',
  `junior_stone` int(11) NOT NULL DEFAULT '0',
  `middle_stone` int(11) NOT NULL DEFAULT '0',
  `high_stone` int(11) NOT NULL DEFAULT '0',
  `fine_hero_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `excellent_hero_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `fine_equipment_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `excellent_equipment_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `stamina` blob,
  `pvp_times` int(11),
  `get_stamina_times` int(11) NOT NULL DEFAULT '0',
  `buy_stamina_times` int(11) NOT NULL DEFAULT '0',
  `last_login_time` int(11),
  `vip_level` int(11) NOT NULL DEFAULT '0',
  `create_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;