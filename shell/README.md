## 终端颜色

* 重置=0, 黑色=30, 红色=31, 绿色=32, 黄色=33, 蓝色=34, 洋红=35, 青色=36, 白色=37

```bash
echo -e "\e[1;31m This is red text\e[0m"
```

## awk 文本处理

```Bash
awk 'BEGIN{ print "start" } pattern { commands } END{ print "end" }'
```