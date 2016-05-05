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
