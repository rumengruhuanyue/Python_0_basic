### content

---

- python代码操作数据库，进行插入语句执行
-爬虫：爬取某网站信息，分析爬取的信息，找出有用信息
    - mysqlclient库
    - requests库
    - bs4库
    - lxml库

---

### 远程linux主机配置环境（mysql数据库，anaconda隔离），连接工作

        1. 库
        CREATE DATABASE scraping CHARACTER SET utf8 COLLATE utf8_general_ci;
        
        CREATE DATABASE scraping CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
        
        2. 表
        CREATE TABLE `urls` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `url` varchar(1000) NOT NULL,
            `content` varchar(4000) NOT NULL,
            `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

        3. 可视化连接工具连接 SSH连接远程主机 + 数据库账户密码
         
        ### 本地navcat连接远程linux（虚拟机环境）中的mysql 
        
        ********************
        *General Information
        ********************
        服务器类型: MySQL
        连接名: local_virtual_mysql
        主机名或 IP 地址: 127.0.0.1
        端口: 3306
        用户名: root
        保存密码: True
        
        ********************
        *SSH Information
        ********************
        使用 SSH 通道: True
        主机名或 IP 地址: 192.168.232.128
        端口: 22
        用户名: root
        验证方法: 密码
        保存密码: True
        
        ********************
        *Other Information
        ********************
        服务器版本: 5.7.30
        通讯协定: 10
        信息: 127.0.0.1 via TCP/IP

               
1. 需要先安装mysql
2. 用pip安装mysqlclient库，连接Python和MySQL

        conda install mysqlclient = 1.4.6 
        
        ___________________________________________________________
        The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        mysql-connector-c-6.1.11   |       h597af5e_1         1.2 MB
        mysqlclient-1.4.6          |   py38he6710b0_0          85 KB
        ------------------------------------------------------------
                                               Total:         1.3 MB

3. conda install beautifulsoup4

4. 【问题】
    1. mysqlclient 安装 可能 需要 先在虚拟机centos上安装好mysql，而且注意使用anaconda安装，`conda install mysqlclient`
   
            【未安装mysql使用pip安装时】
            
            (py38) [root@localhost ~]# pip install mysqlclient==1.4.6
            Collecting mysqlclient==1.4.6
              Downloading mysqlclient-1.4.6.tar.gz (85 kB)
                 |████████████████████████████████| 85 kB 8.4 kB/s 
                ERROR: Command errored out with exit status 1:
                 command: /root/anaconda3/envs/py38/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-we1f_usy/mysqlclient/setup.py'"'"'; __file__='"'"'/tmp/pip-install-we1f_usy/mysqlclient/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-install-we1f_usy/mysqlclient/pip-egg-info
                     cwd: /tmp/pip-install-we1f_usy/mysqlclient/
                Complete output (12 lines):
                /bin/sh: mysql_config: command not found
                /bin/sh: mariadb_config: command not found
                /bin/sh: mysql_config: command not found
                Traceback (most recent call last):
                  File "<string>", line 1, in <module>
                  File "/tmp/pip-install-we1f_usy/mysqlclient/setup.py", line 16, in <module>
                    metadata, options = get_config()
                  File "/tmp/pip-install-we1f_usy/mysqlclient/setup_posix.py", line 61, in get_config
                    libs = mysql_config("libs")
                  File "/tmp/pip-install-we1f_usy/mysqlclient/setup_posix.py", line 29, in mysql_config
                    raise EnvironmentError("%s not found" % (_mysql_config_path,))
                OSError: mysql_config not found
                ----------------------------------------
            ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
            
       * 这里要注意使用anaconda安装，因为，**使用pip强制只安装`mysqlclient`时会报错**。而使用conda install mysqlclient 安装，会同时安装`mysql-connector-c         6.1.11`
    
    2. **linux系统安装mysql时**，安装上后先修改 `vim /etc/my.cnf` 文件跳过密码验证,然后进入mysql后修改密码。
        1. Open & Edit `vim /etc/my.cnf` (or /etc/mysql/my.cnf ,这个没试), depending on your distro.
        2. Add `skip-grant-tables` under [mysqld]
        3. Restart Mysql: `systemctl restart mysqld`(or `service mysqld restart `)
        4. You should be able to login to mysql now using the below command `mysql -u root -p`，然后直接回车,进入mysql>
        5. Run mysql> `flush privileges;`
        6. Set new password by `ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPassword';`
        7. Go back to /etc/my.cnf and remove/comment skip-grant-tables
        8. Restart Mysql
        9. Now you will be able to login with the new password mysql -u root -p
        10. 【注】这个地方不会显示******密码，就直接输完也不会有任何显示回车，密码准确就进入了。
        
        -[ ] 引用：
            * [CentOS7 yum方式安装MySQL5.7](https://www.cnblogs.com/luohanguo/p/9045391.html)
            * [MySQL Error: : 'Access denied for user 'root'@'localhost'](https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost)
    
    3. linux 安装mysql很慢（一直等着安装结束）
            
    3. python代码执行mysql数据库插入数据时候，字符集问题
        > 【错误】UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-2: character maps to <undefined>
            
        > 【解决】创建连接对象时，加上编码格式 `conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', db='scraping', charset='utf8')`
    
    4. bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
        * bs4需要环境中有lxml，不需要铭文引入，但环境中要有。
            - [【爬虫其实很简单】requests 与 beautiful soup基础入门](https://www.jianshu.com/p/9c266216957b)
- [ ] 引用：
    - [【爬虫其实很简单】requests 与 beautiful soup基础入门](https://www.jianshu.com/p/9c266216957b)
    - [mysql字符集 utf8 和utf8mb4 的区别](https://www.cnblogs.com/lgj8/p/12065888.html)
        * utf8mb4兼容utf8
    - [mysql创建数据库及表时设置字符集](https://blog.csdn.net/ncafei/article/details/70142193)