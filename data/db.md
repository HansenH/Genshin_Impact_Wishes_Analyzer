# Database Integration for Genshine Impact Wish Analyzer

## Data Structure

Here we take character wishes as an example.
All tables follow the same structure.
There will be total 4 tables,
`character_wishes`, `weapon_wishes`, `standard_wishes`, and `novice_wishes`,
all in one db.

Although all 4 tables shares the same 4 fields currently,
we cannot assume all structures stays the same in the future.
Therefore, we use separate tables for different wish types.

```sql
CREATE TABLE `character_wishes` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `item_type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `rank_type` int unsigned NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`), UNIQUE (`name`),
    INDEX (`item_type`), INDEX (`rank_type`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Genshine Impact Character Wishes'
```

## Script Usage

```bash
mysql -h host -u username -p < ./create_tables.sql
```
