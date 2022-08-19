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


 
