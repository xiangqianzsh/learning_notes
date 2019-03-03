#pig

Hadoop pig进阶语法
http://www.cnblogs.com/siwei1988/archive/2012/08/06/2624912.html

## pig运行模式
pig test.pig  -useHCatalog
pig app_sdk_label.pig -p dt=2017-09-20 -useHCatalog

本地模式(伪分布式模式下使用): pig -x local test.pig 
MapReduce模式(全分布式下使用): pig test.pig（或者pig -x mapreduce test.pig ,pig test.pig为其简写形式） 

参考:
pig的各种运行模式与运行方式详解
http://blog.csdn.net/zhu_xun/article/details/16820023

## sublime 3安装pig语法高亮
github地址, chrislongo/Pig
https://github.com/chrislongo/Pig


```pig
iras = load 'iris_data_parsed' as (sepalLength:float, sepalWidth:float, petalLength:float, petalWidth:float, species);
iras_grp = group iras by species;
iras_grp_mean = foreach iras_grp generate group, COUNT(iras) as count_, SUM(iras.sepalLength) as sum_, AVG(iras.sepalLength) as mean_;
store iras_grp_mean into 'iris_data_parsed_stats'


describe iras;
describe iras_grp;

describe iras_grp_mean;
dump iras_grp_mean;
```
