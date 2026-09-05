# npm 常用命令速查手册

## 一、查看已安装的包

```bash
# 查看全局安装的包
npm list -g --depth=0

# 查看本地安装的包
npm list --depth=0

# 输出
# 包名@版本号
```

## 二、安装包

```bash
# 全局安装
npm install -g <包名>

# 指定版本安装
npm install -g <包名>@<版本号>

# 本地安装
npm install <包名>
```

## 三、卸载包

```bash
# 卸载全局包
npm uninstall -g <包名>

# 卸载本地包
npm uninstall <包名>
```

## 四、更新包

```bash
# 更新全局包
npm update -g <包名>

# 更新本地包
npm update <包名>
```

## 五、其他常用命令

### 清理缓存

```bash
npm cache clean --force
```

### 查看包信息

```bash
npm info <包名>
```

### 查看包的所有版本

```bash
npm view <包名> versions
```

### 设置镜像源

```bash
npm config set registry https://registry.npmmirror.com
```
