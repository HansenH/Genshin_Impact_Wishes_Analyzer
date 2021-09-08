CREATE DATABASE IF NOT EXISTS genshine_impact_wishes;
USE genshine_impact_wishes;
CREATE TABLE IF NOT EXISTS `character_wishes` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `item_type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `rank_type` int unsigned NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`),
    INDEX (`item_type`), INDEX (`rank_type`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Genshine Impact Character Wishes';
CREATE TABLE IF NOT EXISTS `weapon_wishes` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `item_type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `rank_type` int unsigned NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`),
    INDEX (`item_type`), INDEX (`rank_type`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Genshine Impact Weapon Wishes';
CREATE TABLE IF NOT EXISTS `standard_wishes` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `item_type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `rank_type` int unsigned NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`),
    INDEX (`item_type`), INDEX (`rank_type`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Genshine Impact Standard Wishes';
CREATE TABLE IF NOT EXISTS `novice_wishes` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `item_type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `rank_type` int unsigned NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`),
    INDEX (`item_type`), INDEX (`rank_type`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Genshine Impact Novice Wishes';
