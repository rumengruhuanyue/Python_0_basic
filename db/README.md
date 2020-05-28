### crud

1. 安装pymysql库
2. 手动创建test库，字符集设置为utf8
3. 建表示例：

        sql = "CREATE TABLE IF NOT EXISTS `{}` ( \
                            `id` int(11) NOT NULL AUTO_INCREMENT,  \
                            `order_id` varchar(256) NOT NULL,  \
                            `state` varchar(256) NOT NULL, \
                            `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
                            PRIMARY KEY (`id`) \
                            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8".format(self.table_name)
                        
3. MySQL存储引擎
    * MyISAM  不支持事务   
    * InnoDB  支持事务  具备外键支持功能
  
4. mysql中的字符集：
    > utf8mb3 - 阉割过的utf8，只使用1-3个字节表示字符
	
    > utf8mb4 - 正宗的utf8，使用1-4个字节表示字符
	
	* mysql中的utf8是utf8mb3的别名
	
	* 如果有使用4个字节编码一个字符的情况，如：存储一些emoji表情，就得使用utf8mb4
	
	* 一般正规使用utf8mb4。  
	
            mysql> show charset;
	        +----------+---------------------------------+---------------------+--------+
	        | Charset  | Description                     | Default collation   | Maxlen |
	        +----------+---------------------------------+---------------------+--------+
	        | utf8     | UTF-8 Unicode                   | utf8_general_ci     |      3 |
	        | utf8mb4  | UTF-8 Unicode                   | utf8mb4_general_ci  |      4 |                                            