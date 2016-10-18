# Replica-Set-Primary

The primary is The only member in the replica set that receives write operations. MongoDB applies write operations on the primary and then records the operations on the primary’s **oplog**. Secondary members replicate this log and apply the operations to their data sets.


# 选举

当Primary不可用时, Replica set处于没有Primary的状态, 此刻, 所有节点将变成只读节点.


# 心跳

Replica set中的成员每两秒发送一次心跳包, 如果10秒没有返回, 那么将会标记该成员不可访问.


# Perform Two Phase Commits

[Perform Two Phase Commits](https://docs.mongodb.com/manual/tutorial/perform-two-phase-commits/)
