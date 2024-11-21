# **SHELL1** **统计文件的行数**

## 描述

编写一个shell脚本以输出一个文本文件nowcoder.txt中的行数
示例1

输入：

```
#include <iostream>
using namespace std;
int main()
{
    int a = 10;
    int b = 100;
    cout << "a + b:" << a + b << endl;
    return 0;
}
```

输出：

```
9
```

## Code

```shell
# using cat | wc
cat nowcoder.txt | wc -l

# using wc | awk
wc -l nowcoder.txt | awk '{print $1}'

# awk打印每个行号，然后找出最后一个
awk '{print NR}' nowcoder.txt | tail -n -1

# awk找到最后一个
awk 'END {print NR}' nowcoder.txt

# using sed
sed -n '$=' nowcoder.txt
```

# **SHELL2** **打印文件的最后5行**

## 描述

查看日志的时候，经常会从文件的末尾往前查看，请你写一个bash shell脚本以输出一个文本文件nowcoder.txt中的最后5行。
示例1

输入：

```
#include<iostream>
using namespace std;
int main()
{
int a = 10;
int b = 100;
cout << "a + b:" << a + b << endl;
return 0;
}
```

输出：

```
int a = 10;
int b = 100;
cout << "a + b:" << a + b << endl;
return 0;
}
```

## Code

```shell
# cat | tail
cat nowcoder.txt | tail -n 5

# tail
tail -5 nowcoder.txt
```

# **SHELL3** **输出 0 到 500 中 7 的倍数**

## 描述

写一个 bash脚本以输出数字 0 到 500 中 7 的倍数(0 7 14 21...)的命令

## Code

```shell
#!/bin/bash

for i in {0..500} 
do
    if [ $((${i}%7)) == 0 ]; then
        echo ${i}
    fi
done
```

```shell
#!/bin/bash

for i in {0..500..7}
do
    echo ${i}
done
```

```shell
#!/bin/bash

seq 0 7 500
```

# **SHELL4** **输出第5行的内容**

## 描述

编写一个bash脚本以输出一个文本文件nowcoder.txt中第5行的内容。

输入：

```
welcome
to
nowcoder
this
is
shell
code
```

输出：

```
is
```

## Code

```SHELL
#!/bin/bash

awk 'NR==5 {print $0}' nowcoder.txt

sed -n "5p" nowcoder.txt

head -n 5 nowcoder.txt | tail -1
```

# **SHELL5** **打印空行的行号**

## 描述

编写一个shell脚本以输出一个文本文件nowcoder.txt中空行的行号（空行可能连续，从1开始输出）

输入：

```
a
b

c

d

e


f
```

输出：

```
3
5
7
9
10
```

## Code

```shell
#!/bin/bash

awk '$0 == null {print NR}' nowcoder.txt
```

