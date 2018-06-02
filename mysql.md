# mysql

本机登陆mysql：mysql -u root -p 


删除权限：
```mysql
revoke all privileges on test1.* from test1@"%";
use mysql;
delete from user where user="root" and host="%";
flush privileges;
```
```mysql
CREATE TABLE temp(
    id int NOT NULL AUTO_INCREMENT
);
```


- MySQL 的自动补全功能
http://blog.csdn.net/skydreamer01/article/details/6606186

- Ubuntu安装配置Mysql
http://www.cnblogs.com/wuhou/archive/2008/09/28/1301071.html
