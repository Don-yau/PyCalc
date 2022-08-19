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
git remote add origin  https://github.com/Don-yau/PyCalc.git

# 将本地的当前master分支代码提交待远端master/main
git push -u origin main
进行账号验证之后，即可成功将代码推送到远端 git 仓库。 

echo 'text' | sha1sum # 通过SHA1算法生成'text'的摘要


################################
# 对象
每个对象(object) 包括三个部分：类型，大小和内容。大小就是指内容的大小，内容取决于对象的类型，

Git有四种类型的对象：" blob"、" tree"、 " commit" 和" tag"。
	BLOB:用来存储文件数据，通常是一个文件。
	TREE:“tree”有点像一个目录，它管理一些“tree”或是 “blob”（就像文件和子目录）	COMMIT:一个“commit”只指向一个"tree"，它用来标记项目某一个特定时间点的状态。它包括一些关于时间点的元数据，如时间戳、最近一次提交的作者、指向上次提交（commits）的指针等等。
	TAG:一个“tag”是来标记某一个提交(commit) 的方法。

几乎所有的Git功能都是使用这四个简单的对象类型来完成的。它就像是在你本机的文件系统之上构建一个小的文件系统。这个小型的文件系统就是 .git/objects目录。 

# 本地仓库、远端仓库（或者叫远程仓库、服务器仓库）、工作区、缓存区、本地仓库（或者叫 本地版本库）

# 1, 初始化 git 项目仓库的方法:
第一种是从一个 git 服务器克隆一个现有的 git 仓库。
git clone https://gitee.com/xxx/test1.git 
第二种是在现有项目 或 空项目目录下初始化 git 仓库，并绑定上远端仓库。 
# 初始化git仓库
git init
# 绑定绑定远端仓库
git remote add origin https://gitee.com/xxx/test1.git 

# 2. 将工作区文件添加到 git 缓存区 
将文件添加到 git 缓存区后，项目里的文件将会被 git 监控 
git add main.cpp 
可以用 git status 查看缓冲区文件状态

# 3. 将缓存区文件提交到 版本库
# -m 参数后面代表的信息备注
git commit -m "first commit"
运行后看到终端的一些提示信息，包含文件变动的一些基本信息 
git log 可以查看提交记录
 
# 4. 查看文件差异
在 git 仓库中的文件，都会被 git 跟踪，如文件修改历史、是否是新文件、文件提交历史等等。
# 比较所有文件与缓存区文件差异
git diff
# 比较当前文件和缓存区文件差异
git diff <file>
# 比较两次提交之间的差异
git diff <id1> <id2>
# 在两个分支之间比较
git diff <branch1> <branch2>
# 比较缓存区和版本库差异，与下一条指令的效果一样
git diff --staged
# 比较缓存区和版本库差异，与上一条指令的效果一样
git diff --cached
# 仅仅比较统计信息
git diff --stat
但要注意的是，只有使用 git add 指令将文件文件到缓存区之后，文件的信息才会被记录，
关键词 a 和 b，分别指的是缓存区和工作区，可以看出在b中的main.cpp文件多了 6 行代码

# 5. 将本地仓库提交同步到远程仓库
# 将当前分支 (默认是master/main) 推送到远端仓库的 master/main 分支
git push -u origin main
 

