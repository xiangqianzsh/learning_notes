
# saiku mysql SQLAlchemy学习


# redis
- Redis快速入门 - Redis教程
http://www.yiibai.com/redis/redis_strings.html 
- Redis的三种启动方式
http://www.tuicool.com/articles/aQbQ3u
- Redis 命令参考
http://doc.redisfans.com/
- redis 多数据库
http://www.ttlsa.com/redis/redis-database/

# mysqlDB
 - python下的MySQLdb使用
http://blog.csdn.net/vincent_czz/article/details/7697039/

# SQLAlchemy
- SQLAlchemy 简单笔记
http://www.jianshu.com/p/e6bba189fcbd

# mysql学习
create database db_cube character set utf8;

- Command Line Shell For SQLite
https://www.sqlite.org/cli.html

- SQLAlchemy基本操作和常用技巧
http://blog.csdn.net/dszgf5717/article/details/45918279

- MySQL for Mac 安装和基本操作
http://blog.sina.com.cn/s/blog_9ea3a4b70101ihl3.html

- MySQL创建用户与授权方法
http://www.jb51.net/article/31850.htm
- mysql 数据类型
http://www.cnblogs.com/zbseoag/archive/2013/03/19/2970004.html

# mysql优化
可以试试优化下数据库和代码：
1. 给每个字段加索引  
2. 不要用select * ... 
3. 如果用的django的model访问数据库，不要使用外键的join查询，特别慢。
这几点都是我踩过的深坑...差点被坑死那种

还有，数据量不是超大的时候，能一次查出来的尽量不要一个个查，数据库有对语句的检查，会耗时；
如果数据量太大，则要反过来，不要一次全查出来（数据库支持并发查询数有限，这样会长时间占用一个查询数），分多次查出来后再拼接。

这个不知道对不对，但我确实这样处理后解决了我的问题

- 高并发异步uwsgi+web.py+gevent
http://blog.csdn.net/linuxheik/article/details/52043414
我们知道gevent通过monkey patch替换掉了标准库中阻塞的模块，但是有的时候可能我们会“无意识”地引入阻塞模块，例如MySQL-Python，pylibmc。这两个模块是通过C扩展程序实现的，都需要进行socket通信，由于调用的底层C的socket接口，所以超出了gevent的管控范围，这样就在使用这两个模块跟mysql或者memcached进行通信时，就退化为了阻塞调用。



# Saiku学习
- Mondrian Documentation
http://mondrian.pentaho.com/documentation/schema.php

# 下载jdk包
# 在MAC上查找和设置$JAVA_HOME
http://guibin.iteye.com/blog/1999238

sh start-saiku.sh
现在可以启动
tomcat；然后再浏览器中输入：http://localhost:8080,可以看到Saiku的登录页面，输入admin和admin作为密码登
录Saiku。恭喜，Saiku已经部署成功了。

saiku的日志在tomcat/log里面
tail catalina.out
当你发现配置好了但界面上显示不出来的时候，就去看日志

- 数据仓库-多维分析展示平台Saiku
http://www.tuicool.com/articles/J3yq2mz 
- 如何把saiku部署到tomcat上
http://zhidao.baidu.com/link?url=r431pRJGZaL1rzHwGpAT9wGGlwd7rHlpO_ZM4IZRtZmztHC8MBCnaOcSj5m1CS55plOlPGjmZulNsgxQ3do5nOKBd9V66qnzlT3XwyTPhuW

- saiku源码整合（无maven情况下）
http://blog.csdn.net/gsying1474/article/details/39018251


# python flask

- How to prevent errno 32 broken pipe?
http://stackoverflow.com/questions/11866792/how-to-prevent-errno-32-broken-pipe