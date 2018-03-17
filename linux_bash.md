#bash语法学习

## 查看进程是干什么的

ll /proc/进程号

##Linux help

### 登录机器免密配置自动执行脚本：
参考: https://chu888chu888.gitbooks.io/shellstudy/content/shellexample.html
```
登录机器免密配置：
1、在原始自己机器当前用户的家目录下执行“ssh-keygen -t rsa ”，产生一对公钥（文件名：id_rsa.pub)私钥（文件名：id_rsa）
   注意每次执行ssh –keygen –t rsa都会产生一对公钥私钥对，如果已有的话可以不需要再执行，否则会覆盖以前的配置

2、在原始自己机器上执行“ssh-copy-id -i ~/.ssh/id_rsa.pub 目的机器user@目的机器主机server” 就可以将自己的公钥id_rsa.pub中内容放到目标服务器的/home/用户名user/.ssh/authorized_keys文件中（也可以在目的机器通过vim打开写入）

3、直接ssh  目的机器user@目的机器主机serve 就会发现不需要输入密码啦

本质：就是将自己的公钥写到对方的授权文件：authorized_keys 

user ~/tools $  cat autossh.sh
#!/bin/bash
ssh user@hostname << SSHEND
    cd /home/test/
    >> test_temp.txt
    echo "helo"
    exit
SSHEND
echo "done!"
```


###并行化命令  cat cmd.txt  | parallel -j 3
注意cmd.txt里面不要带`&`号
### scp
```
# cp单个文件:
scp user@hostname:/home/files/temp.tar.gz .
# cp文件夹
scp -r user@hostname:/home/files  .
```

###rev 以最后一个字母进行排序:
rev abc.txt | sort | rev > sorted.txt

### cat -n 000005_0 |  awk -F "\001" '{print $1, $29}' |  grep "20185376423"

### find
```
# 从当前目录开始查找所有扩展名为.conf.rb的文本文件，并找出包含”SortedKeyGroup”的文件
find . -name "*.conf.rb" | xargs grep "SortedKeyGroup"
find . -name "*.sh" | xargs grep 'Linux-amd64-64'
```
### mail发邮件
```bash
cmd='wget ftp://hostname:/home/files/data.tar.gz'
echo "Please execute this command to get data: ${cmd}" | mail -s data_${stat_date} -c aaa@163.com bbb@163.com ccc@163.com

echo 'mail content' | mail -s test -c aaa@163.com bbb@163.com
```
参考链接:
linux mail命令用法
http://www.cnblogs.com/xiaoshi1991/archive/2012/09/20/2695061.html

### split把文件分解成小文件
```bash
split ${file_name} -d ${file_name}_ -n 40 -a 5
# part_00001, part_00002, ..., part_00040
```

###sort
sort -k 1,1
LC_ALL=C sort就可以使用ASCII编码
###awk
```
awk -F '\t' '{print $1}' exp0226 
 cat a.txt  | awk '{sum+=$5} END {print sum}'
 cat a.txt  | awk '{sum+=$5} END {print sum/1024/1024/1024}'

ls -ls files/* | awk '{sum+=$5} END {print sum/1024/1024/1024}'  #求文件大小

# 把一个文件里的各行打乱
awk 'BEGIN{srand()}{b[rand()NR]=$0}END{for(x in b)print b[x]}' data  
```


- AWK使用总结(2)使用split()时指定多个分隔符，使用-F时指定多个分隔符
- http://blog.csdn.net/feliciafay/article/details/8282780

### ls设置日期格式
```bash
ls -l --time-style '+%Y/%m/%d %H:%M:%S'
ls -l --time-style '+%Y-%m-%d %H:%M:%S'
```
### head, tail
tail -n +100 /etc/man.config,  代表该文件从100行以后都会被列出
tail -n  100 /etc/man.config,  代表只取最后100行

###cut
```
cat ${data_file} | grep 'TaggerKey' | grep 'CLICK' | head -n 1 | cut -f 1-8 > cut_file
```

###tar解压：
```bash
[root@linux ~]# tar -cvf /tmp/etc.tar /etc <==仅打包，不压缩！
[root@linux ~]# tar -czvf /tmp/etc.tar.gz /etc <==打包后，以 gzip 压缩

# 打包files文件夹, 不包含files/large_datas
tar -czvf files.tar.gz files --exclude=files/large_datas
tar -xvf file.tar //解压 tar包
tar -xzvf file.tar.gz //解压tar.gz
tar -xjvf file.tar.bz2   //解压 tar.bz2
tar -xZvf file.tar.Z   //解压tar.Z
unrar e file.rar //解压rar
unzip file.zip //解压zip
```

### nslookup 11.35.120.19

###统计demo目录下所有js文件代码行数，过滤了空行：
```
find /demo -name "*.js" |xargs cat|grep -v "^$"|wc -l
cat mapper.py | grep -v "^$" | wc -l

grep -v  "^\t$"
```
###查看文件夹的大小，包括里面的文件
du -sh /home
du -s home
du -sh ./
du -sh

###linux 命令反引号引起来是什么意思
比如
```
rm `cat rm_file.txt`
```
命令转换，使``中的命令执行结果复制给一个变量。
```

``的作用是运行``之间的命令,并且将命令运行的结果返回.一般shell脚本应该是这样:
result=`ls -l` (用你的命令替换ls -l,这里只是举例)
这样,result就有``里面的运行结果了
你可以用echo $result来检验下
```
参考链接:
[学习共享] shell十三问? 
http://bbs.chinaunix.net/forum.php?mod=viewthread&tid=218853&page=7#pid1617953
Bash Pitfalls
http://bash.cumulonim.biz/BashPitfalls.html?utm_campaign=Manong_Weekly_Issue_11&utm_medium=EDM&utm_source=Manong_Weekly#for_i_in_.24.28ls_.2A.mp3.29

###vim编码
vim中有时候编码有些有错是不能转换, 这里要强制下
```vim
:e ++enc=utf8
```
###tail, head
```
tail -n 100 ~/hadoop-mnt-stoff/ps/ubs/zhangshaohua02/display/20150725/part-00000 | python get_qid.py
```

###怎么查看linux文件夹下有多少个文件
ls | wc -w是查看有多少个文件及文件夹
ls -l | wc -l

###显示文件中的部分文件
ls | head -n 20
ls | head -n 20 | tail -n +10

###linux find
find   -name april*                     在当前目录下查找以april开始的文件
http://www.cnblogs.com/wanqieddy/archive/2011/06/09/2076785.html



### ssh密钥登录及远程执行命令
参考链接
http://www.cnblogs.com/chencye/p/6130476.html


###查看进程

ps
ps -l
查看进程, 且显示cmd命令
ps aux   //如果只显示自己的, 可以ps ux

###kill进程
kill -9 pid
kill pid

###netstat -lnp | grep 8500


###终端打开GBK编码的文件
head newcookiesort_20150824 | iconv -f gb18030 -t utf8
iconv -f gbk -t utf-8


###vim
```bash
:s/vivian/sky/   #替换当前行第一个 vivian 为 sky 
:s/vivian/sky/g   #替换当前行所有 vivian 为 sky 
:n,$s/vivian/sky/   #替换第 n 行开始到最后一行中每一行的第一个 vivian 为 sky 
:n,$s/vivian/sky/g   #替换第 n 行开始到最后一行中每一行所有 vivian 为 sky 
:%s/vivian/sky/  #（等同于 ：g/vivian/s//sky/） 替换每一行的第一个 vivian 为 sky 
:%s/vivian/sky/g  #（等同于 ：g/vivian/s//sky/g） 替换每一行中所有 vivian 为 sky 
```

#linux下批量替换文件内容
sed -i 's/data_20160724/data_20160803_20160810/g' `grep data_20160724 -rl ./`

linux下批量替换文件内容
1、网络上现成的资料
　　格式: sed -i "s/查找字段/替换字段/g" `grep 查找字段 -rl 路径`

　　linux sed 批量替换多个文件中的字符串

　　sed -i "s/oldstring/newstring/g" `grep oldstring -rl yourdir`

　　例如：替换/home下所有文件中的www.admin99.net为admin99.net

　　sed -i "s/www.admin99.net/admin99.net/g" `grep www.admin99.net -rl /home`

　　exp:sed -i "s/shabi/$/g" `grep shabi -rl ./`

2、自己额外附加

　　2.1 将文件1.txt内的文字“garden”替换成“mirGarden”
```
　　# sed -i "s/garden/mirGarden/g" 1.txt   //sed -i 很简单

　　2.2 将当前目录下的所有文件内的“garden”替换成“mirGarden”

　　## sed -i "s/garden/mirGarden/g" `ls` //其实也就是ls出多个文件名而已


**参考链接** http://www.cnblogs.com/end/archive/2012/05/24/2517131.html
```
#日期相关
```bash
stat_date=`date -d "+1 day $stat_date" +%Y%m%d`
/home/work/cron_run.sh `date --date yesterday +\%Y\%m\%d` >> ~/cron_run_log.txt 2>&1
```

##for ((i=0; i<10; i++))
```bash
for ((i=0; i<10; i++)); do
    echo $i
done
```
#while if
```bash
if [ $# -lt 2 ]; then
    echo " You should give no less than one day argument , you can use below two execute methods..."
    echo " ./get_query_data.sh experiment [date_start] [date_end] "
    echo " ./get_query_data.sh experiment [date]"
    exit 1
fi
exp_name=$1
if [ $# -lt 3 ]; then
    start_date=$2
    end_date=$2
else
    start_date=$2
    end_date=$3
fi
script=$(readlink -f "$0")
scriptpath=$(dirname "$script")
framework_path=$(dirname "$scriptpath")
src_path=$framework_path/src
exp_path=$framework_path/exp/$exp_name
exp_data_path=$framework_path/exp_data/$exp_name

hadoop_client='/bin/hadoop'
if [ ! -e "$hadoop_client" ];  then
    hadoop_client=`cat $framework_path/config.conf | grep '^hadoop_client' | cut -d'=' -f 2 ` 
fi
user_name=`cat $framework_path/config.conf | grep '^username' | cut -d'=' -f 2 `
temp_date=$start_date

while [[ $start_date -le $end_date ]]; do
    if [ ! -e "$exp_data_path/${start_date}_Q" ]; then
        $hadoop_client fs -cat /ps/.../*-Q > $exp_data_path/${start_date}_Q
    fi
    start_date=`date -d "+1 day $start_date" +%Y%m%d`
done

echo "starting output the query_data"
#cd $src_path
python $src_path/query_parser.py $exp_name $temp_date $end_date
echo "finished output query_data"
```

#日期循环
```bash
start_date=20160430
end_date=20160508


stat_date=$start_date
while [[ $stat_date -le $end_date ]]; do
    cmd="
    ...
        "
    echo $cmd
    # eval $cmd
    stat_date=`date -d "+1 day $stat_date" +%Y%m%d`
done
```

#for part-00000
###for i in `seq 100` 
```bash
for i in `seq 100` 
do 
    part_name=$(printf "part-%05d" $i)
    cmd=" head -n 5 ${part_name} | ruby ~/logstat/jtab.rb - -j 1 -c query_cnt >> ~/log_cnt.txt 
        "
    echo $cmd
    eval $cmd
done 
```
###for((i=1;i<100;i++))
```bash
for((i=1;i<100;i++))
do 
    part_name=$(printf "part-%05d" $i)
    cmd=" head -n 5 ${part_name} | ruby ~/logstat/jtab.rb - -j 1 -c query_cnt >> ~/log_cnt.txt 
        "
    echo $cmd
    eval $cmd
done 
```

# 获取脚本所在路径
```bash
SHELL_FOLDER=$(dirname $(readlink -f "$0")) #
path=$(dirname $0)

/home/work/projects/exp/exp_name_20170101/script

exp_name=${SHELL_FOLDER#*exp/} #掐头，最小匹配（去除从前往后第一个exp/及前面的所有字符）
exp_name=${exp_name%%/script*} #去尾，最大匹配（去除从后往前最后一个/script及后面的所有字符）
```




## shell bash判断文件或文件夹是否存在
```shell
#shell判断文件夹是否存在

#如果文件夹不存在，创建文件夹
if [ ! -d "/myfolder" ]; then
  mkdir /myfolder
fi

#shell判断文件,目录是否存在或者具有权限


folder="/var/www/"
file="/var/www/log"

# -x 参数判断 $folder 是否存在并且是否具有可执行权限
if [ ! -x "$folder"]; then
  mkdir "$folder"
fi

# -d 参数判断 $folder 是否存在
if [ ! -d "$folder"]; then
  mkdir "$folder"
fi

# -f 参数判断 $file 是否存在
if [ ! -f "$file" ]; then
  touch "$file"
fi

# -n 判断一个变量是否有值
if [ ! -n "$var" ]; then
  echo "$var is empty"
  exit 0
fi

# 判断两个变量是否相等
if [ "$var1" = "$var2" ]; then
  echo '$var1 eq $var2'
else
  echo '$var1 not eq $var2'
fi
```

# 有用代码片段

```
cat -n 000005_0 |  awk -F "\001" '{print $1, $29}' |  grep "20185376423"

for((i=0;i<10;i++))
do 
    part_name=$(printf "%06d_0" $i)
    
    cmd="cat -n ${part_name} |  awk -F \"\001\" '{print \$1, \$29}' |  grep '1814482761' "
    echo $cmd
    eval $cmd
done 
```





