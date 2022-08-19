# usage of git:

# 配置用户 
git config --global user.name "xxx" 
git config --global user.email xxx@example.com 

cd /home/pan/work/src# 进入工作目录

git init # 初始化git仓库
 

git add test.cpp  #  提交到 git 缓存区 
git add .   # 将当前目录所有文件提交到 git 缓存区


git commit -m "first commit" # 将本地git缓存区代码提交到本地仓库，-m 参数后面是提交备注
 
# 将本地仓库绑定远程仓库 
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
Working Directory (工作区)：我们编辑与变动的代码文件，都在工作区下   pwd；
Stating Area (缓存区)：代码有变动的时候，git add 提交到 git 缓存区。让 git status   git diff 查看代码的变动；
Respository (仓库)：在 git 缓存区的代码，都可以提交到 git 仓库进行托管。从图中可以看到，本地的仓库（一般指我们自己的电脑）可以将代码提交到远程的仓库（一般指 git 服务器）。


# 1, 初始化 git 项目仓库的方法:
第一种是从一个 git 服务器克隆一个现有的 git 仓库。 
git clone https://github.com/Don-yau/PyCalc.git
第二种是在现有项目 或 空项目目录下初始化 git 仓库，并绑定上远端仓库。 

git init  # 初始化git仓库

git remote add origin https://github.com/Don-yau/PyCalc.git  # 绑定绑定远端仓库

# 2. 将工作区文件添加到 git 缓存区 
将文件添加到 git 缓存区后，项目里的文件将会被 git 监控 
git add main.cpp 
可以用 git status 查看缓冲区文件状态

# 3. 将缓存区文件提交到 版本库

git commit -m "first commit"  # -m 参数后面代表的信息备注
运行后看到终端的一些提示信息，包含文件变动的一些基本信息 
git log 可以查看提交记录
 
# 4. 查看文件差异
在 git 仓库中的文件，都会被 git 跟踪，如文件修改历史、是否是新文件、文件提交历史等等。
git diff # 比较所有文件与缓存区文件差异
git diff <file> # 比较当前文件和缓存区文件差异
git diff <id1> <id2> # 比较两次提交之间的差异
git diff <branch1> <branch2> # 在两个分支之间比较
git diff --staged  # 比较缓存区和版本库差异，与下一条指令的效果一样
git diff --cached  # 比较缓存区和版本库差异，与上一条指令的效果一样
git diff --stat  # 仅仅比较统计信息

但要注意的是，只有使用 git add 指令将文件文件到缓存区之后，文件的信息才会被记录，
关键词 a 和 b，分别指的是缓存区和工作区，可以看出在b中的main.cpp文件多了 6 行代码

# 5. 将本地仓库提交同步到远程仓库
git push -u origin main # 将当前分支 (默认是master/main) 推送到远端仓库的 master/main 分支

 

# 分支的基本操作
# 本地分支
#（1）查看分支  
git branch 

# （2）创建与切换分支
git branch develop  # 创建develop分支
git checkout develop # 切换到 develop 分支 
git checkout -b develop #-b参数，创建之后即切换 

#（3）删除分支
下面我们在develop分支创建一个新分支，并删除掉新创建的分支
git checkout -b feature/211031

git checkout develop# 先切换回develop分支
git branch -d feature/211031 # 删除 feature/211031 功能分支

# 远端分支，
# r1 将本地的`develop`分支提交到远端
git push -u origin develop  
	如果远端没有 develop 分支将会自动创建。
	参数是 -u，是 --set-upstream 的简写，与 push 指令联用。
	类似功能的参数--set-upstream-to 用于直接设置关联，该参数与 branch 指令联用。 
git branch --set-upstream-to origin/master develop  # 将远端 master 关联到 本地 develop分支
	
	以上指令将远端 master 分支关联到本地的 develop 分支。换一种说法是，我们将本地 develop 分支追踪远端的 master 分支。
	
# r2 删除远端的 develop 分支
git push -u origin -d develop
origin 关键词指的是一个指针，origin 指向的是本地的代码库托管在远端的仓库，可以说 origin 对应的是远端仓库。  


#  同步远端分支
（1）相关指令
git fetch  # 从远程获取最新版本信息到本地
git merge FETCH_HEAD  # 将远端版本合并到当前分支 

以上的两个指令可以用一个 git pull来代替， 
git pull <远程主机名> <远程分支名>:<本地分支名>

（2）实例
git pull  让当前分支自动与其追踪的分支进行合并 
git pull origin master:develop 远端的 master 分支，与本地的 develop 分支合并，
 

 功能分支要合并到主分支上。上图的合并过程可以通过以下命令来实现


# 分支合并
git checkout develop  #切换到develop分支
git merge feature     # 将feature分支合并到develop分支 
git rebase feature    # 将feature分支合并到develop分支

  rebase 的方式不是直接合并，而是将 feature 分支变化的提交记录直接追加到主分支之上。使得两个分支的代码保持提交的记录是一致的  


# 文件产生冲突和解决的过程

（1）初始化git仓库
mkdir test2  # 创建一个 test2 目录
cd test2  # 进入 test2 目录
git init  # 初始化git仓库
git add .  # 将文件添加git缓存区
git commit -m "first commit" # 将git提交到版本库
 
（2）在新分支写入代码

这时候，我们已经在 master 分支已经有了一个 git 的版本库。现在需要从 master 分支创建新分支，如下命令
git checkout -b develop 
git commit -a 等价于下面的指令
  git add .
  git commit 

（2）在主分支上写入代码
接着我们切换到 master 分支，如下指令
git checkout master
现在我们在 master 分支中对main.cpp文件添加另外一行代码，如 #include<stdlib.h>
再使用以下命令进行提交
git commit -a

（3）产生冲突
此时，master 分支到了第 2 个版本，develop 也在第 2 个版本，并且他们同一行文件代码不一样，代码合并后必定会产生冲突。
接下来我们将 develop 分支合并到 master分支，如下命令
git merge develop  # 在master分支上将develop分支合并进来
提示信息的关键词 CONFLICT，此时代码已经产生了 git 无法自动解决的冲突，合并之后的代码如下所示

<<<<<<< HEAD
#include<stdlib.h>
=======
#include<iostream>
>>>>>>> develop

现在我们打开 main.cpp 文件，可以看到合并的代码中被分成了两栏。上面部分的关键词是HEAD，我们在前面说过 HEAD 指针指向的是当前分支，即 master，而下面的部分是 develop 分支的代码。

（4）解决冲突
 手动解决冲突，假如我们两行代码都想要，那么删除掉 git 产生的临时行，同时保留两个分支的代码即可，最终修改如下：

#include<stdlib.h>
#include<iostream>
最后，我们再将修改之后的代码再次提交到版本库即可，如下指令

git commit -a -m "解决冲突"  


 