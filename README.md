#use git:

# 配置用户名
git config --global user.name "xxx"
# 配置邮箱
git config --global user.email xxx@example.com 

# 进入工作目录
cd /home/pan/work/src
# 初始化git仓库
git init 

# 创建一个c++源代码文件
touch test.cpp 

# 将 test.cpp 文件提交到 git 缓存区
git add test.cpp 
# 将当前目录所有文件提交到 git 缓存区
git add . 

# 将本地git缓存区代码提交到本地仓库，-m 参数后面是提交备注
git commit -m "first commit" 

#假如我们在 github 仓库上创建了一个仓库，仓库的 git 地址为 https://github.com/xxx/test.git, 
# 将本地仓库绑定远程仓库
git remote add origin https://github.com/xxx/test.git
# 将本地的当前master分支代码提交待远端master
git push -u origin master
进行账号验证之后，即可成功将代码推送到远端 git 仓库。 

echo 'text' | sha1sum # 通过SHA1算法生成'text'的摘要
对象


每个对象(object) 包括三个部分：类型，大小和内容。大小就是指内容的大小，内容取决于对象的类型，Git有四种类型的对象：" blob"、" tree"、 " commit" 和" tag"。
BLOB:用来存储文件数据，通常是一个文件。
TREE:“tree”有点像一个目录，它管理一些“tree”或是 “blob”（就像文件和子目录）
COMMIT:一个“commit”只指向一个"tree"，它用来标记项目某一个特定时间点的状态。它包括一些关于时间点的元数据，如时间戳、最近一次提交的作者、指向上次提交（commits）的指针等等。
TAG:一个“tag”是来标记某一个提交(commit) 的方法。

几乎所有的Git功能都是使用这四个简单的对象类型来完成的。它就像是在你本机的文件系统之上构建一个小的文件系统。这个小型的文件系统就是 .git/objects目录。 
