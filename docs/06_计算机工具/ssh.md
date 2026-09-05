# SSH 常用命令速查手册

[下载 Win32-OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/releases)

## 一、ssh（客户端）

#### 连接登录

```bash
## 指定端口连接
ssh -p 2222 user@hostname
```

#### 密钥管理

```bash
## 生成 Ed25519 密钥对（推荐，更安全更快）
## -C 指明公钥创建的归属
ssh-keygen -t ed25519 -C "your_email@example.com"

## 复制公钥到远程服务器
ssh-copy-id user@hostname

## 手动添加公钥到远程服务器
cat ~/.ssh/id_rsa.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

###### 本地权限（客户端）

```bash
## 密钥目录仅本人可访问（700 = rwx------）
chmod 700 ~/.ssh
## 私钥仅本人可读写（600 = rw-------），过宽会被拒绝使用
chmod 600 ~/.ssh/id_ed25519
## 公钥可读即可（644 = rw-r--r--）
chmod 644 ~/.ssh/id_ed25519.pub
```

###### 远程权限（服务器）

```bash
## 远程 .ssh 目录仅本人可访问（700）
## authorized_keys 仅本人可读写（600），过宽会被服务器忽略
ssh user@hostname "chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
```

#### 端口转发

###### 本地端口转发

```bash
## 格式：-L [本地端口]:[目标地址]:[目标端口] 跳板机
## 效果：本地开端口，请求经跳板机转发到目标

## 示例：本地 8080 → 远程服务器 → localhost:80
## 访问 http://127.0.0.1:8080 相当于访问远程服务器的 80 端口
ssh -L 8080:localhost:80 user@hostname

## 示例：本地 8080 → 远程服务器 → 内网机器 10.0.0.2:80
## 访问 http://127.0.0.1:8080 相当于访问内网 10.0.0.2 的 80 端口
ssh -L 8080:10.0.0.2:80 user@hostname
```

###### 远程端口转发

```bash
## 格式：-R [远程端口]:[目标地址]:[目标端口] 中转服务器
## 效果：远程服务器开端口，请求经本地转发到目标

## 示例：远程服务器监听 9000 → SSH 隧道 → 本地 → localhost:3000
## 远程服务器访问 http://127.0.0.1:9000 相当于访问本地的 3000 端口
ssh -R 9000:localhost:3000 user@hostname

## 示例：远程服务器监听 2233 → SSH 隧道 → 本地 → ip2:80
## 远程服务器访问 http://127.0.0.1:2233 相当于访问 ip2 的 80 端口
ssh -R 2233:ip2:80 user@hostname -p 2244
```

###### 穿透跳板机

```bash
## 格式：-J [跳板机] [目标服务器]
## 效果：通过跳板机连接目标服务器
ssh -J jump_user@jump_host target_user@target_host
```

###### SOCKS 代理

```bash
## 格式：-D [本地端口]
## 效果：本地开 SOCKS5 代理，所有流量走远程服务器出口

## 本地监听 1080 端口，浏览器设置代理后所有请求经远程服务器发出
ssh -D 1080 user@hostname

## 后台运行，不执行命令（仅代理）
ssh -fN -D 1080 user@hostname
```

#### 配置文件

编辑 `~/.ssh/config`：

```bash
## ssh myserver快捷连接
Host myserver
    HostName 192.168.1.100
    Port 22
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
```

## 二、sshd（服务端）

#### 服务管理

```bash
## 启动 sshd
sudo systemctl start sshd
## 停止 sshd
sudo systemctl stop sshd
## 重启 sshd
sudo systemctl restart sshd
## 查看 sshd 状态
sudo systemctl status sshd
## 设置开机自启
sudo systemctl enable sshd
```

#### 安全配置

编辑 `/etc/ssh/sshd_config`：

> ```bash
> ## 修改默认端口
> Port 2222
>
> ## 禁止 root 直接登录
> PermitRootLogin no
>
> ## 禁止密码登录（仅密钥登录）
> PasswordAuthentication no
>
> ## 允许使用的用户（白名单，可选）
> AllowUsers user1 user2
>
> ## 密钥认证（保持开启）
> PubkeyAuthentication yes
> ```

## 三、sshfs（文件系统挂载）

#### 挂载

```bash

## 指定端口挂载
sshfs user@hostname:/remote/path /local/mountpoint -p 2222
```

#### 卸载

```bash
## 卸载 sshfs 挂载
fusermount -u /local/mountpoint
## 强制卸载
fusermount -uz /local/mountpoint
```
