# 指令操作

python 中导入 os

指令顺序：python、windows、linux

1. 获得当前路径
   os.getcwd()
   cd
   pwd
2. 切换路径
   os.chdir("")
   cd
3. 创建目录
   os.mkdir()
   mkdir
4. 删除目录
   os.removedirs()
   rd
5. 查找当前目录的文件
   os.listdir()
   dir
   ls
6. 找到程序在哪

    where python
    which python

7. 显示文本文件的内容
   type
   cat

# 额外

.是当前目录
..是上一级目录
NT 是微软操作系统

操作系统文件名 禁用 > < : ? " " \* \ / |

路径名：
Windows 使用\\
Linux、Mac 使用/

#!是环境路径的意思，加在.py 的文件里面

Linux 下，-rwx，r 是读权限，w 是写权限，x 是运行权限。（例：只读，-r--）
可以通过命令：chmod u+x test.py 更改

ls -s 可以看到文件的一些信息，其中三个-rwx 分别是文件创建者、同组下的其他人、其他人

在 Linux 下直接运行.py 文件，./test.py（需要选择默认打开方式）

# Python

python 导入模块，直接运行

右结合：赋值运算，一元运算，乘方，三元运算
(): 将一行写成多行
; : 将多行写成一行
