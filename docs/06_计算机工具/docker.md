# Docker 常用命令速查手册

## 一、镜像管理

| 命令 | 说明 |
|:---|:---|
| `docker images` | 列出本地所有镜像 |
| `docker pull <镜像名>:<标签>` | 从仓库拉取镜像 |
| `docker build -t <镜像名>:<标签> .` | 使用当前目录的 Dockerfile 构建镜像 |
| `docker rmi <镜像ID/名>` | 删除指定镜像 |
| `docker tag <源镜像> <新镜像名>:<标签>` | 为镜像打标签 |
| `docker save -o <文件名.tar> <镜像名>` | 将镜像导出为 tar 文件 |
| `docker load -i <文件名.tar>` | 从 tar 文件导入镜像 |
| `docker image prune` | 清理所有未被使用的悬空镜像 |

## 二、容器生命周期

| 命令 | 说明 |
|:---|:---|
| `docker run -d --name <容器名> <镜像>` | 后台运行一个容器并命名 |
| `docker run -it <镜像> /bin/bash` | 以交互模式启动容器并进入终端 |
| `docker ps` | 列出正在运行的容器 |
| `docker ps -a` | 列出所有容器（包括已停止的） |
| `docker start <容器ID/名>` | 启动一个已停止的容器 |
| `docker stop <容器ID/名>` | 停止一个运行中的容器 |
| `docker restart <容器ID/名>` | 重启容器 |
| `docker rm <容器ID/名>` | 删除一个已停止的容器 |
| `docker rm -f <容器ID/名>` | 强制删除容器（即使是运行中） |
| `docker exec -it <容器ID/名> /bin/bash` | 进入运行中的容器 |
| `docker logs -f <容器ID/名>` | 实时查看容器日志 |
| `docker cp <容器ID>:<容器内路径> <宿主机路径>` | 从容器中拷贝文件到宿主机 |

## 三、容器运行常用参数

| 参数 | 说明 |
|:---|:---|
| `-d` | 后台运行 |
| `-it` | 交互式终端 |
| `--name` | 指定容器名称 |
| `-p 8080:80` | 端口映射（宿主机:容器） |
| `-v /host/path:/container/path` | 挂载宿主机目录到容器 |
| `-e MYSQL_ROOT_PASSWORD=123456` | 设置环境变量 |
| `--restart=always` | 容器退出时自动重启 |
| `--network <网络名>` | 指定容器使用的网络 |
| `--rm` | 容器退出时自动删除 |

## 四、网络管理

| 命令 | 说明 |
|:---|:---|
| `docker network ls` | 列出所有网络 |
| `docker network create <网络名>` | 创建自定义网络 |
| `docker network inspect <网络名>` | 查看网络详情 |
| `docker network connect <网络名> <容器ID>` | 将容器连接到网络 |
| `docker network disconnect <网络名> <容器ID>` | 将容器从网络断开 |
| `docker network rm <网络名>` | 删除指定网络 |

## 五、数据卷管理

| 命令 | 说明 |
|:---|:---|
| `docker volume ls` | 列出所有数据卷 |
| `docker volume create <卷名>` | 创建一个数据卷 |
| `docker volume inspect <卷名>` | 查看卷的详细信息 |
| `docker volume rm <卷名>` | 删除指定数据卷 |
| `docker volume prune` | 清理未使用的数据卷 |

## 六、系统信息与清理

| 命令 | 说明 |
|:---|:---|
| `docker info` | 查看 Docker 系统信息 |
| `docker stats` | 实时监控容器资源使用情况 |
| `docker system df` | 查看 Docker 磁盘使用情况 |
| `docker system prune -a` | 清理所有未使用的镜像、容器、网络和构建缓存（慎用） |

## 七、Docker Compose（常用子命令）

| 命令 | 说明 |
|:---|:---|
| `docker compose up -d` | 根据 docker-compose.yml 启动服务（后台） |
| `docker compose down` | 停止并删除服务相关容器、网络 |
| `docker compose ps` | 查看 compose 管理的容器状态 |
| `docker compose logs -f` | 查看所有服务的实时日志 |
| `docker compose restart` | 重启所有服务 |
| `docker compose build --no-cache` | 重新构建镜像（不使用缓存） |
| `docker compose exec <服务名> /bin/bash` | 进入 compose 管理的某个服务容器 |