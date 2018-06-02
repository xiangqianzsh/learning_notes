# datetime.timedelta对象的seconds属性中返回的秒的差别, 并没有考虑天的不同.
```python
from datetime import datetime
start_time = datetime.strptime('2017-01-02 12:30:30', '%Y-%m-%d %H:%M:%S')
# print elapse_time
print (datetime.strptime('2017-01-02 12:29:30', '%Y-%m-%d %H:%M:%S') - start_time).seconds
print (datetime.strptime('2017-01-02 12:31:31', '%Y-%m-%d %H:%M:%S') - start_time).seconds
print (datetime.strptime('2017-01-03 12:31:31', '%Y-%m-%d %H:%M:%S') - start_time).seconds
print (datetime.strptime('2017-01-01 12:31:31', '%Y-%m-%d %H:%M:%S') - start_time).seconds

86340
61
61
61
```
> 如果代码里跨天的, 可以使用 start_time = time.time(); end_time = time.time(); elapse_time = end_time - start_time



## python cube

官方网站：http://cubes.databrewery.org/
开源地址：https://github.com/Stiivi/cubes


- olap cube python - 无极吧
http://ju.outofmemory.cn/entry/67858
- jmontesl/cubesviewer
https://github.com/jjmontesl/cubesviewer

- Cubes - Lightweight Python OLAP (EuroPython 2012 talk)
http://www.slideshare.net/Stiivi/cubes-lightweight-python-olap

