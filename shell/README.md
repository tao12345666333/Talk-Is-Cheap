## 终端颜色
* 重置=0, 黑色=30, 红色=31, 绿色=32, 黄色=33, 蓝色=34, 洋红=35, 青色=36, 白色=37 
```bash
echo -e "\e[1;31m This is red text\e[0m"
```

## awk 文本处理

```bash
awk 'BEGIN{ print "start" } pattern { commands } END{ print "end" }'
```

## 四则运算

* 整数运算
    ```bash
    num1=1;
    num2=3;
    let result=num1+num2
    result=$[ num1 + num2 ]
    result=$(( num1 + num2 ))
    result=`expr $num1 + $num2`
    ```
* 浮点数运算
    - 使用 `bc`
        ```bash
        num1=1.2;
        num2=3;
        result=$(echo "$num1 * $num2" | bc)
        ```
    - 使用awk
        ```bash
        result=$(awk -v num1=1.2 -v num2=3 'BEGIN {printf "%.2f", num1*num2}')
        ```

## date

```bash
date "+%Y %B %d %A %H %M %S %N %s"
```

## 调试

```bash
bash -xv xx.sh
```

## 判断

test


## tr

* alnum 字母和数字
* alpha 字母
* cntrl 控制字符
* digit 数字
* graph 图形字符
* lower 小写字母
* print 可打印字符
* punct 标点符号
* space 空白字符
* upper 大写字母
* xdigit 十六进制字符


## bash执行的优先顺序

1. 别名：alias
2. 关键字：keyword
3. 函数：function
4. 内建命令：built in
5. 哈希索引：hash
6. 外部命令：command


# bash中开启alias

```bash
shopt -s expand_aliases
```

# 生成目录树

```bash
tree PATH -H PATH -o tree.html
```

# wget

```bash
wget --limit-rate 20k http://moelove.info # 限速
wget -Q 100m http://moelove.info https://github.com/tao12345666333 # 队列
```


# bash脚本中 `$#` 代表参数数量

```bash
if [ $# -eq 0 ];
then
    echo "need param"
    exit -1
fi
```
