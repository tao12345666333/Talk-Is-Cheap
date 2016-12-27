# 介绍 (10分钟)

* 是什么

    - web服务器&&框架
    - 异步网络库

    Tornado 全称是Tornado web server， 既是
    web服务器也有web框架的功能，可能有同学会问
    为什么Tornado是web服务器？  
    同时也是一个异步网络
    库， 

* 用途

    *举例*

    - web应用
    - 后端
    - 异步任务管理

* 特点
  
    - 优势

        - C10k
        - 轻量(对比django, web部分对比flask)
        - 异步非阻塞(举例)
        - 长连接的支持（知乎等公司使用的原因）

    - 缺点

        - 缺乏相关中间件(相比django) 


# 环境搭建

* 装Python2

    - windows (配置环境变量)
    - Linux/Mac

* 装pip 或者 源码安装

    - Linux、Mac 
        
        ```bash
        wget http://pypa.pypi.org/get_pip.py
        ```

* 安装Tornado

    ```bash
    pip install tornado
    ```

* 演示
    - 写个应用跑起来


--------------------------------
同步 |  异步  |  阻塞  |  非阻塞 
--------------------------------
