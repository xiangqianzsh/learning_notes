

# Linux文件权权限与目录配置

## 1.使用者与群组

在我们Linux系统当中，默认的情况下，所有的系统上的账号与一般身份使用者，还有那个root的相关信息， 都是记录在/etc/passwd这个文件内的。至于个人的密码则是记录在/etc/shadow这个文件下。 此外，Linux所有的组名都纪录在/etc/group内！这三个文件可以说是Linux系统里面账号、密码、群组信息的集中地.

## 2. Linux文件权限概念

目录的x代表的是用户能否进入该目录成为工作目录
要开放目录给任何人浏览时，应该至少也要给予r及x的权限，但w权限不可随便给；
chgrp ：改变文件所属群组
chown ：改变文件拥有者
chmod ：改变文件的权限, SUID, SGID, SBIT等等的特性

```shell
[root@www ~]# chgrp [-R] dirname/filename ...

[root@www ~]# chown [-R] 账号名称 文件或目录
[root@www ~]# chown [-R] 账号名称:组名 文件或目录

[root@www ~]# chmod [-R] xyz 文件或目录
[root@www ~]# chmod 777 .bashrc
[root@www ~]# chmod  u=rwx,go=rx  .bashrc
[root@www ~]# chmod  a+w  .bashrc
[root@www ~]# chmod  a-x  .bashrc
```

## 3. Linux目录配置

很多读者都会误会/usr为user的缩写，其实usr是Unix Software Resource的缩写，
![Centos目录结构图](3.3.directory_tree.png "Centos目录结构图")

# Linux文件与目录管理 
## 1.目录与路径
cd：变换目录
pwd：显示目前的目录, -P 的选项可以让我们取得正确的目录名称，而不是连结档的路径.
mkdir：创建一个新的目录
rmdir：删除一个空的目录


```shell
[root@www ~]# cd ~vbird
# 代表去到 vbird 这个使用者的家目录，亦即 /home/vbird

[root@www ~]# pwd [-P]
选项与参数：
-P  ：显示出确实的路径，而非使用连结 (link) 路径。

[root@www ~]# mkdir [-mp] 目录名称
选项与参数：
-m ：配置文件的权限喔！直接配置，不需要看默认权限 (umask) 的脸色～
-p ：帮助你直接将所需要的目录(包含上一级目录)递回创建起来！

[root@www ~]# rmdir [-p] 目录名称
选项与参数：
-p ：连同上一级『空的』目录也一起删除
```