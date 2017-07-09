# Redis cluster 选举

* 选举过程是集群中所有 master 都需要参与的, 当半数以上 master 节点与其他 master 节点通信超过 (cluster-node-timeout), 认为当前 master 节点挂掉.

不保证强一致性, 因为使用了异步复制的机制。
