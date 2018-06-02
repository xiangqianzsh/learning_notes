#Anaconda使用



## anaconda安装环境
```
conda update conda  #更新

# 建python2.7的环境并安包:
conda create --name ENV2.7 python=2.7
conda install --name ENV2.7  ipython pygments pyzmq numpy scipy pandas matplotlib lxml

# 安装包:
activate ENV3.4
```
>`conda install ipython[all]`不能用
>安装`pygments pyzmq`包使得`ipython qtconsole`可用.

当然也可以 activate 到一个环境里后再安装相应的包
```
# 建立python3.4环境
conda create --name ENV3.4 python=3.4
conda info --envs
source activate ENV3.4  # Linux, OS X
# 安装包
conda install ipython pygments pyzmq numpy scipy pandas matplotlib lxml  # list
conda list
source deactivate  # mac下
```
windows下激活与取消激活方法
```
activate ENV3.4
source deactivate
```

## 安装了Anaconda3, 但是不能使用命令行
这是因为Anaconda3的解释器未加入到环境变量中, 可以在终端输入:
```bash
export PATH=~/anaconda3/bin:$PATH
```
但重新打开个终端或者下次开机又不能用了, 为了一次性解决问题, 可以:
1.  打开/etc/profile文件: $sudo gedit /etc/profile
2.  在文件的最后，加入上面的bash命令. 这样就OK了.

参考链接:
1. I have installed Anaconda on Mac/Linux, but I cannot use the commands.
http://docs.continuum.io/anaconda/faq.html#install-maclinux
2. Ubuntu下设置环境变量及PATH的方法 
http://blog.chinaunix.net/uid-26285146-id-3138789.html


##其它链接
1. Package Documentation (介绍Anaconda中的Python2.7和Python3.4各支持哪些包)
http://docs.continuum.io/anaconda/pkg-docs.html
2. documentation
    http://docs.continuum.io/conda/build.html 



## 在ipython中用python3.4版本
1. 安装python3.4的开发环境
sudo apt-get install python3.4-dev
2. 进入虚拟环境,安装ipython
source ENV3.4/bin/activate
pip install ipython[all]
3. 在虚拟环境下用 python3.4 -m Ipython,就可以了.(有可能前面的步骤不是必需的.)


**参考链接:**
1. IPython Notebook in a virtualenv, using Python 3.3
http://stackoverflow.com/questions/20290357/ipython-notebook-in-a-virtualenv-using-python-3-3

