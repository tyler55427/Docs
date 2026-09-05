# 代理

## 一、使用代理

### 方式一：直接开启 Clash 的 TUN 模式，通过虚拟网卡全局接管

### 方式二：当部分需要代理的时候，为工具配置环境变量

## 二、代理配置验证

```bash
# 测试 HTTP 代理是否可用
curl -I https://www.google.com
```

## 三、系统代理

影响图形界面（浏览器等），在系统设置中配置。

## 四、工具代理

影响命令行工具，通过环境变量或工具自身配置生效。

### 环境变量代理（适用于 curl、wget、npm、pip、conda、apt 等）

#### Linux / WSL

```bash
# 设置代理（临时，当前终端有效）
export http_proxy=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897
export all_proxy=socks5://127.0.0.1:7897
export no_proxy=localhost,127.0.0.1,.local

# 取消代理
unset http_proxy
unset https_proxy
unset all_proxy
unset no_proxy

# 查看当前代理
echo $http_proxy
echo $https_proxy

# 永久写入配置（追加到 ~/.bashrc 或 ~/.zshrc）
echo 'export http_proxy=http://127.0.0.1:7897' >> ~/.bashrc
echo 'export https_proxy=http://127.0.0.1:7897' >> ~/.bashrc
source ~/.bashrc   # 立即生效
```

#### Windows（CMD）

```cmd
REM 设置代理（临时，当前窗口有效）
set http_proxy=http://127.0.0.1:7897
set https_proxy=http://127.0.0.1:7897

REM 取消代理
set http_proxy=
set https_proxy=

REM 查看代理
echo %http_proxy%
echo %https_proxy%
```

#### Windows（PowerShell）

```powershell
# 设置代理（临时，当前会话有效）
$env:http_proxy="http://127.0.0.1:7897"
$env:https_proxy="http://127.0.0.1:7897"

# 取消代理
$env:http_proxy=$null
$env:https_proxy=$null

# 查看代理
$env:http_proxy

# 永久设置（用户级别）
[Environment]::SetEnvironmentVariable("http_proxy", "http://127.0.0.1:7897", "User")
[Environment]::SetEnvironmentVariable("https_proxy", "http://127.0.0.1:7897", "User")

# 删除永久设置
[Environment]::SetEnvironmentVariable("http_proxy", $null, "User")
[Environment]::SetEnvironmentVariable("https_proxy", $null, "User")
```

---

### 需要手动配置的工具

#### git

```bash
# 设置 HTTP/HTTPS 代理
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897

# 设置 socks 代理
git config --global http.proxy socks5://127.0.0.1:7897

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy

# 仅对特定域名使用代理（如 GitHub）
git config --global http.https://github.com.proxy http://127.0.0.1:7897

# 查看当前代理配置
git config --global --get http.proxy

# 查看所有代理相关配置
git config --global --list | grep proxy
```

#### SSH

SSH 代理通过 `ProxyCommand` 或 `nc` 配合 `-X` 选项实现，推荐使用 `nc`（netcat）：

```bash
# 方式一：在 ~/.ssh/config 中配置
# 编辑 ~/.ssh/config，添加：
Host github.com
  HostName github.com
  User git
  ProxyCommand nc -X connect -x 127.0.0.1:7897 %h %p

# 方式二：配合 corkscrew（需要安装）
# 编辑 ~/.ssh/config：
Host github.com
  HostName github.com
  User git
  ProxyCommand corkscrew 127.0.0.1 7897 %h %p

# 方式三：使用 connect-proxy（Linux）
# 安装：sudo apt install connect-proxy
# 编辑 ~/.ssh/config：
Host github.com
  ProxyCommand connect-proxy -H 127.0.0.1:7897 %h %p

# 测试 SSH 代理是否生效
ssh -T git@github.com
```

#### Docker

```bash
# 方式一：Docker 客户端代理（拉取镜像时使用）
# 创建或编辑 ~/.docker/config.json（Linux/macOS）
# Windows 路径：%USERPROFILE%\.docker\config.json
{
  "proxies": {
    "default": {
      "httpProxy": "http://127.0.0.1:7897",
      "httpsProxy": "http://127.0.0.1:7897",
      "noProxy": "localhost,127.0.0.1"
    }
  }
}

# 方式二：Docker daemon 全局代理（所有容器使用）
# 创建或编辑 /etc/systemd/system/docker.service.d/proxy.conf（Linux）
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7897"
Environment="HTTPS_PROXY=http://127.0.0.1:7897"
Environment="NO_PROXY=localhost,127.0.0.1"

# 重启 Docker 使配置生效
sudo systemctl daemon-reload
sudo systemctl restart docker

# 验证代理是否生效
docker info | grep -i proxy

# 方式三：Docker Desktop（Windows/macOS）
# 在 Docker Desktop 设置 → Resources → Proxies 中配置
```

### 无法使用代理

```bash
# ping 使用 ICMP 协议，不是 TCP/UDP 协议，无法走 HTTP/SOCKS 代理
ping google.com    # 不走代理，直接连接

# 其他无法使用代理的工具：
# - nslookup / dig（DNS 查询）
# - traceroute / tracert（路由追踪）
```

---

## 附录

### linux 开关代理脚本

需要使用windows的真实IP地址，不能使用127.0.0.1

```bash
#!/bin/bash

# ============================================
# WSL 代理开关脚本
# 代理地址: 127.0.0.1:7897
# ============================================

PROXY_HOST=$(ip route show default | awk '{print $3}')
PROXY_PORT="7897"
PROXY_URL="http://$PROXY_HOST:$PROXY_PORT"

# 不代理的地址（局域网、本地等）
NO_PROXY="localhost,127.*,192.168.*,10.*,172.16.*,172.17.*,172.18.*,172.19.*,172.20.*,172.21.*,172.22.*,172.23.*,172.24.*,172.25.*,172.26.*,172.27.*,172.28.*,172.29.*,172.30.*,172.31.*"

# ============================================
# 功能函数
# ============================================

# 开启代理
proxy_on() {
    # 检查代理是否已开启
    if [ -n "$http_proxy" ] || [ -n "$HTTP_PROXY" ]; then
        echo "⚠️  代理可能已经开启"
        echo "当前 http_proxy: $http_proxy"
        read -p "是否重新设置？(y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            return
        fi
    fi

    # 设置代理环境变量（小写）
    export http_proxy="$PROXY_URL"
    export https_proxy="$PROXY_URL"
    export ftp_proxy="$PROXY_URL"
    export all_proxy="$PROXY_URL"
    export no_proxy="$NO_PROXY"

    # 设置代理环境变量（大写，某些应用需要）
    export HTTP_PROXY="$PROXY_URL"
    export HTTPS_PROXY="$PROXY_URL"
    export FTP_PROXY="$PROXY_URL"
    export ALL_PROXY="$PROXY_URL"
    export NO_PROXY="$NO_PROXY"

    echo "✅ 代理已开启: $PROXY_URL"
    echo "📋 不代理: $NO_PROXY"
}

# 关闭代理
proxy_off() {
    unset http_proxy https_proxy ftp_proxy all_proxy no_proxy
    unset HTTP_PROXY HTTPS_PROXY FTP_PROXY ALL_PROXY NO_PROXY

    echo "❌ 代理已关闭"
}

# 显示当前代理状态
proxy_status() {
    echo "========== 代理状态 =========="
    if [ -n "$http_proxy" ] || [ -n "$HTTP_PROXY" ]; then
        echo "🔴 代理已开启"
        echo "http_proxy  : ${http_proxy:-$HTTP_PROXY}"
        echo "https_proxy : ${https_proxy:-$HTTPS_PROXY}"
        echo "no_proxy    : ${no_proxy:-$NO_PROXY}"
    else
        echo "🟢 代理未开启"
    fi
    echo "================================"
}

# 测试代理是否生效
proxy_test() {
    echo "🔍 测试代理连接..."

    # 测试 Google（通过代理）
    if curl -s -o /dev/null -w "%{http_code}" --proxy "$PROXY_URL" https://www.google.com 2>/dev/null | grep -q "200"; then
        echo "✅ 代理连接正常（Google 可访问）"
    else
        echo "❌ 代理连接失败（Google 不可访问）"
    fi

    # 测试国内网站（直连）
    if curl -s -o /dev/null -w "%{http_code}" https://www.baidu.com 2>/dev/null | grep -q "200"; then
        echo "✅ 国内网站直连正常"
    else
        echo "⚠️  国内网站连接异常"
    fi
}

# 显示帮助
show_help() {
    cat << EOF
WSL 代理管理脚本

用法:
    source proxy.sh [命令]     # 注意：必须用 source 才能生效

命令:
    on          开启代理
    off         关闭代理
    status      查看代理状态
    test        测试代理连接
    help        显示此帮助

示例:
    source proxy.sh on        # 开启代理
    source proxy.sh off       # 关闭代理
    source proxy.sh status    # 查看状态

注意:
    必须使用 'source' 命令执行，否则环境变量不会生效！
    或者你可以先执行: chmod +x proxy.sh
    然后: ./proxy.sh on

EOF
}

# ============================================
# 主逻辑
# ============================================

case "$1" in
    on)
        proxy_on
        ;;
    off)
        proxy_off
        ;;
    status)
        proxy_status
        ;;
    test)
        proxy_test
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        # 默认显示状态
        proxy_status
        echo
        echo "💡 使用 'source proxy.sh on' 开启代理"
        echo "   'source proxy.sh off' 关闭代理"
        ;;
    *)
        echo "❌ 未知命令: $1"
        echo "使用 'source proxy.sh help' 查看帮助"
        return 1
        ;;
esac
```
