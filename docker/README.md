# Docker能做什么

* 隔离应用间的依赖
* 容易创建可复制的应用镜像
* 容易分发，可直接使用
* 允许实例便利的进行扩展
* 允许销毁

# Docker中比较重要的概念

* 镜像
    比我们一般使用的虚拟机快照还要轻量一些，必须要完全可移植

* 容器
    可以从镜像中创建容器，应用由容器运行

* 数据卷
    不受容器生命周期的影响进行数据持久化

* 链接
    对其他容器的引用，就是链接

# Docker如何完成它需要完成的东西

* cgroups提供容器隔离
* union文件系统用于保存镜像

# eg.

```
docker pull ubuntu:latest

docker images

# --rm 是当容器退出就删除， -ti 是分配一个伪终端进入交互模式
docker run --rm -ti ubuntu /bin/bash
```

# Docker的三个组件

* Docker Client 用户界面，支持用户和Docker Daemon之间通信
* Docker Daemon 运行于主机上，处理服务请求
* Docker Index是中央registry，支持有访问权限的Docker容器镜像的备份

# Docker的三个基本要素

* Docker Containers负责应用程序运行，包括操作系统，用户添加的文件和元数据
* Docker Images是一个只读模板，用来运行Docker容器
* DockerFile是文件指令集，用来说明如何自动创建Docker镜像

# 部分操作

```
docker stop $job_name # 停止
docker restart $job_name # 重启
docker logs $job_name # 查看日志
docker rm $job_name # 移除
docker commit $job_name $new_name # 把状态保存成为镜像

docker pull image # pull镜像
```

* 进入container
    ```
    docker attach $container_id # 这种方式局限性太大. 不建议

    # 修改docker以lxc方式启动
    vim /etc/default/docker 增加 DOCKER_OPTS="-e lxc"
    sudo service docker restart

    sudo lxc-attach -n id # 这样的前提是docker要以lxc方式启动

    # 还有一种使用nsenter 的方式,还没研究过.

    # 1.3版本后增加了exec的命令, 很方便,我很喜欢
    docker exec -it $container_id cmd
    ```

# Dockerfile

可以使用 `docker build`命令进行构建

所有的Dockerfile都必须从FROM命令开始，相当于是在指定base image

* `MAINTAINER` <author name> 作者
* `RUN` <command> 在新镜像上添加新的层面
* `ADD` <source> <destination>
* `CMD` 容器默认执行的命令。这个命令只允许执行一次，最后一次执行
* `EXPOSE` <port>; 容器运行时监听的端口
* `ENTRYPOINT` 相当于是给容器一个默认执行的程序(也仅仅能执行这个)，这个命令和CMD一样，只执行最后的。
* `WORKDIR` 工作目录 `WORKDIR /path/to/workdir`
* `ENV` 环境变量 `ENV <key> <value>`
* `USER` 运行时设置uid
* `VOLUME` 授权访问从容器内到主机上的目录 `VOLUME ['/data']`

# Redis

可以通过下面的命令来把redis container 的6379端口映射到本地
```
docker run -d --name redis -p 6379:6379 redis
```
