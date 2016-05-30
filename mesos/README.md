# 资源统一管理和调度平台的特点

* 多种计算框架支持
* 易于扩展
* 高度容错
* 资源利用率高
* 细粒度资源分配


# mesos基本术语

* Mesos-master：Mesos master，主要负责管理各个framework和slave，并将slave上的资源分配给各个framework
* Mesos-slave：Mesos slave，负责管理本节点上的各个mesos-task，比如：为各个executor分配资源
* Framework：计算框架，如：Hadoop，Spark等，通过MesosSchedulerDiver接入Mesos
* Executor：执行器，安装到mesos-slave上，用于启动计算框架中的task。

当用户试图添加一种新的计算框架到Mesos中时，需要实现一个Framework scheduler和executor以接入Mesos。

来源: [董的博客](http://dongxicheng.org/apache-mesos/meso-architecture/)
