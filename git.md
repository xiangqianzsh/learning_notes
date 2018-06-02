# git
## 参考资料
- 猴子都能看懂的git入门
http://backlogtool.com/git-guide/cn/
- git - 简明指南
http://rogerdudler.github.io/git-guide/index.zh.html


## 常用操作
git checkout 2a
git reset --hard




##git 502 Bad Gateway错误
git里出现错误`error: RPC failed; HTTP 502 curl 22 The requested URL returned error: 502 Bad Gateway`, 

**解决1**, 先前在.bash_profile里设置了公司的http代理, 是这个代理的问题, 现在把代理去掉
```bash
#~/.bash_profile

#add http proxy, 设置了git会出错
#export http_proxy=http://agent.xxx:8188
#export https_proxy=https://agent.xxx:8188
#add .bashrc
source ~/.bashrc
```
**解决2**
```bash
alias git='http_proxy= git'
#这样在运行git这个命令时http_proxy为空, 也不影响其它要用到http代理的操作
```


## Git中tag的用法
打标签
`git tag -a v1.01 -m 'Relase version 1.01'`
注解：git tag 是打标签的命令，-a 是添加标签，其后要跟新标签号，-m 及后面的字符串是对该标签的注释。

提交标签到远程仓库
`git push origin --tags`
注解：就像git push origin master 把本地修改提交到远程仓库一样，-tags可以把本地的打的标签全部提交到远程仓库。
- Git中tag的用法
http://blog.csdn.net/rainnings/article/details/9821027

## GIT push, HTTP code = 502 error

```bash
git config --local http.postBuffer 157286400
```

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```
**参考链接**
- http://stackoverflow.com/questions/24322896/git-push-http-code-502-error


## 如何删除提交历史
有时提交历史有错误或是有敏感信息, 需要清空提交历史, 则可以使用如下命令
```bash
$ rm  -rf .git/
$ git init
$ git add c++.md
$ git commit -m "new"
$ git remote add origin git@github.com:xiangqianzsh/learning_notes.git
$ git push -f  origin master
# set tracking information for this branch
$ git branch --set-upstream-to=origin/master master
```
参考链接:
- git仓库删除所有提交历史记录，成为一个干净的新仓库

  http://blog.csdn.net/yc1022/article/details/56487680


## 新建仓库
Quick setup — if you’ve done this kind of thing before
`git clone xxx.git`

...or create a new repository on the command line
```
echo "# leetcode" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:xiangqianzsh/leetcode.git
git push -u origin master
```
...or push an existing repository from the command line
```
git remote add origin git@github.com:xiangqianzsh/leetcode.git
git push -u origin master
```
