# git
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
