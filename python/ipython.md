# ipython

## 避免每次更改import的代码都要重启终端
Basically all you have to do is the following: and changes you make are reflected automatically after you save.
```
In [1]: %load_ext autoreload

In [2]: %autoreload 2

In [3]: Import MODULE

In [4]: my_class = Module.class()
        my_class.printham()
Out[4]: ham

In [5]: #make changes to printham and save
In [6]: my_class.printham() 
Out[6]: hamlet
```
**参考链接:**
- Need to restart python in Terminal every time a change is made to script
http://stackoverflow.com/questions/3374542/need-to-restart-python-in-terminal-every-time-a-change-is-made-to-script



## windows平台下: Ipython slows down after plotting
windows平台,  使用ipython画图后打字开始变慢, 之后平均每秒显示一个字母.

**原因:** the default plotting backend for iPython to be intolerably slow on my Windows 7 box.

**解决:**
1,  可以使用`$ ipython --matplotlib`gives me the Using `matplotlib backend: Qt4Agg `which works ok.
2,  even better - try the iPython qtconsole`$ ipython qtconsole`

PS: 如果`$ ipython qtconsole`如果少一些模块的话可能会出错, 这时可以`conda install pygments pyzmq`

**测试代码:**
```python
import matplotlib.pyplot as plt 
plt.plot([1,2,3], [4,5,6])
plt.show()
```

**参考链接:**
1. Ipython slows down after plotting with pylab
http://stackoverflow.com/questions/26420039/ipython-slows-down-after-plotting-with-pylab
2. Ipython interpreter turns slow (Anaconda, Windows)
http://stackoverflow.com/questions/30004595/ipython-interpreter-turns-slow-anaconda-windows
3. A Qt Console for IPython
http://ipython.org/ipython-doc/stable/interactive/qtconsole.html


# ipython qtconsole/jupyter qtconsole 画图内嵌
use `%pylab inline` or `%matplotlib inline` in the qtconsole itself.
