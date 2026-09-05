# 常用终端命令

# 一、环境变量

## 查看环境变量

```bash
# linux
# 查看所有环境变量
env
# 查看 PATH 环境变量
echo $PATH
# 查看 HOME 环境变量
echo $HOME
```

```bash
# windows(cmd)
# 查看所有环境变量
set
# 查看 PATH 环境变量
echo %PATH%
# 查看 USERPROFILE 环境变量
echo %USERPROFILE%
```

## 设置环境变量

```bash
# linux
export MY_VAR="hello"
```

```bash
# windows(cmd)
set MY_VAR=hello
```

## 删除环境变量

```bash
# linux
unset MY_VAR
```

```bash
# windows(cmd)
set MY_VAR=
```

# 二、查找

## 按文件名查找

```bash
# linux
# 精确查找文件名
find /path -name "file.txt"
# 模糊查找 .log 文件
find /path -name "*.log"
# 递归查找所有 .conf 文件
find /path -type f -name "*.conf"
```

```bash
# windows(cmd)
# 精确查找文件名
dir /b "file.txt"
# 模糊查找 .log 文件
dir /b "*.log"
# 递归查找文件
dir /s /b "file.txt"
```

## 文件内容搜索

```bash
# linux
# 递归搜索所有文本文件内容，显示行号（自动跳过二进制文件）
grep -rnI "keyword" /path
```

```bash
# windows(cmd)
# 递归搜索所有文件内容，显示行号
findstr /s /n "keyword" *.*
```

# 三、压缩和解压

## 压缩

```bash
# linux
# 压缩为 tar 格式（不压缩）
tar -cvf archive.tar /path/to/dir
# 压缩为 tar.gz 格式
tar -czvf archive.tar.gz /path/to/dir
```

## 解压

```bash
# linux
# 解压 tar
tar -xvf archive.tar
# 解压 tar.gz
tar -xzvf archive.tar.gz
```

# 四、系统信息

## 查看系统信息

```bash
# linux
# 查看内核版本
uname -a
# 查看系统发行版版本（Ubuntu、Debian、CentOS 等通用）
cat /etc/os-release
```

```bash
# windows(cmd)
# 查看系统版本号（最通用）
ver
# 查看详细系统信息
systeminfo
```

## 查看磁盘

```bash
# linux
df -h
```

## 查看内存

```bash
# linux
free -h
```

# 五、链接

## 软链接和硬链接

软链接和硬链接使用上没有区别，只有在删除源文件时，软链接会失效，而硬链接不会失效。

两者都可以实现同步，通常软链接就足够了。

```bash
# linux

# 创建软链接：ln -s <源文件> <链接文件>
ln -s /path/to/target link_name

# 创建硬链接：ln <源文件> <链接文件>
# 1、硬链接不能跨文件系统
# 2、不能链接目录
ln /path/to/target hard_link_name
```

# 六、文件传输

## 上传

```bash
# 上传：本地 → 远程
# scp [选项] <本地文件路径> <用户>@<远程主机>:<远程目标路径>

# 上传整个目录（使用 -r 递归）
scp -P 22 -r ./local_dir/ user@192.168.1.100:/remote/path/

# 使用配置
scp -r ./local_dir/ laptop:/remote/path/
```

## 下载

```bash
# 下载：远程 → 本地
# scp [选项] <用户>@<远程主机>:<远程文件路径> <本地目标路径>

# 下载整个目录（-r 递归）
scp -P 22 -r user@192.168.1.100:/remote/remote_dir/ ./local_dir/

# 使用配置
scp -r laptop:/remote/path/ ./local_dir/
```
