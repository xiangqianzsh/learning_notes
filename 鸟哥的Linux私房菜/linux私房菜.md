

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



##　2.文件与目录管理

文件与目录的检视： ls
复制、删除与移动： cp, rm, mv

```shell
[root@www ~]# ls [-aAdfFhilnrRSt] 目录名称
[root@www ~]# ls [--color={never,auto,always}] 目录名称
[root@www ~]# ls [--full-time] 目录名称
选项与参数：
-a  ：全部的文件，连同隐藏档( 开头为 . 的文件) 一起列出来(常用)
-A  ：全部的文件，连同隐藏档，但不包括 . 与 .. 这两个目录
-d  ：仅列出目录本身，而不是列出目录内的文件数据(常用)
-f  ：直接列出结果，而不进行排序 (ls 默认会以档名排序！)
-F  ：根据文件、目录等资讯，给予附加数据结构，例如：
      *:代表可运行档； /:代表目录； =:代表 socket 文件； |:代表 FIFO 文件；
-h  ：将文件容量以人类较易读的方式(例如 GB, KB 等等)列出来；
-i  ：列出 inode 号码，inode 的意义下一章将会介绍；
-l  ：长数据串列出，包含文件的属性与权限等等数据；(常用)
-n  ：列出 UID 与 GID 而非使用者与群组的名称 (UID与GID会在帐号管理提到！)
-r  ：将排序结果反向输出，例如：原本档名由小到大，反向则为由大到小；
-R  ：连同子目录内容一起列出来，等於该目录下的所有文件都会显示出来；
-S  ：以文件容量大小排序，而不是用档名排序；
-t  ：依时间排序，而不是用档名。
--color=never  ：不要依据文件特性给予颜色显示；
--color=always ：显示颜色
--color=auto   ：让系统自行依据配置来判断是否给予颜色
--full-time    ：以完整时间模式 (包含年、月、日、时、分) 输出
--time={atime,ctime} ：输出 access 时间或改变权限属性时间 (ctime) 
                       而非内容变更时间 (modification time)
                       
# 完整的呈现文件的修改时间 *(modification time)
[root@www ~]# ls -al --full-time  ./



[root@www ~]# cp [-adfilprsu] 来源档(source) 目标档(destination)
[root@www ~]# cp [options] source1 source2 source3 .... directory
选项与参数：
-a  ：相当於 -pdr 的意思，至於 pdr 请参考下列说明；(常用)
-d  ：若来源档为连结档的属性(link file)，则复制连结档属性而非文件本身；
-f  ：为强制(force)的意思，若目标文件已经存在且无法开启，则移除后再尝试一次；
-i  ：若目标档(destination)已经存在时，在覆盖时会先询问动作的进行(常用)
-l  ：进行硬式连结(hard link)的连结档创建，而非复制文件本身；
-p  ：连同文件的属性一起复制过去，而非使用默认属性(备份常用)；
-r  ：递回持续复制，用於目录的复制行为；(常用)
-s  ：复制成为符号连结档 (symbolic link)，亦即『捷径』文件；
-u  ：若 destination 比 source 旧才升级 destination ！
最后需要注意的，如果来源档有两个以上，则最后一个目的档一定要是『目录』才行！


# 复制目录
[root@www tmp]# cp -r /etc/ /tmp
# 还是要再次的强调喔！ -r 是可以复制目录，但是，文件与目录的权限可能会被改变
# 所以，也可以利用『 cp -a /etc /tmp 』来下达命令喔！尤其是在备份的情况下！

# 复制为软链接
[root@www tmp]# cp -s bashrc bashrc_slink

# 更新复制
[root@www tmp]# cp -u ~/.bashrc /tmp/bashrc
# 这个 -u 的特性，是在目标文件与来源文件有差异时，才会复制的。
# 所以，比较常被用於『备份』的工作当中喔！ ^_^

#　备份
[root@www tmp]# cp -a /var/log/wtmp wtmp_2
# 当我们在进行备份的时候，某些需要特别注意的特殊权限文件， 例如密码档 (/etc/shadow) 以及一些配置档，就不能直接以 cp 来复制，而必须要加上 -a 或者是 -p 等等可以完整复制文件权限的选项才行！
```



http://cn.linux.vbird.org/linux_basic/0220filemanager_2.php



