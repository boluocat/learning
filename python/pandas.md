# [2877. 从表中创建 DataFrame](https://leetcode.cn/problems/create-a-dataframe-from-list/)

编写一个解决方案，基于名为 `student_data` 的二维列表 创建 一个 DataFrame 。这个二维列表包含一些学生的 ID 和年龄信息。

DataFrame 应该有两列， `student_id` 和 `age`，并且与原始二维列表的顺序相同。

返回结果格式如下示例所示。

示例 1：

```
输入：
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
输出：
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
解释：
基于 student_data 创建了一个 DataFrame，包含 student_id 和 age 两列。
```

```python
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    pd_student = pd.DataFrame(student_data, columns = ['student_id','age'])

    return pd_student
```

# [2878. 获取 DataFrame 的大小](https://leetcode.cn/problems/get-the-size-of-a-dataframe/)

```
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
```

编写一个解决方案，计算并显示 `players` 的 行数和列数。

将结果返回为一个数组：

```
[number of rows, number of columns]
```

返回结果格式如下示例所示。

示例 1：

```
输入：
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
输出：
[10, 5]
解释：
这个 DataFrame 包含 10 行和 5 列。
```

## pandas获取dataframe的结构信息

- 显示行数，列数等，`df.info()`
- 获取行数，`len(df)`
- 获取列数，`len(df.columns)`
- 获取行数和列数，`df.shape`
- 获取元素总数（大小），`df.size`

## Tuple转换为list

`list()`

```python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
    row = len(players)
    col = len(players.columns)

    return [row, col]
```

```python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return list(players.shape)
```

# [2879. 显示前三行](https://leetcode.cn/problems/display-the-first-three-rows/)

```
DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
```

编写一个解决方案，显示这个 DataFrame 的 前 `3` 行。

 

示例 1:

```
输入：
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
输出：
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
解释：
只有前 3 行被显示。
```

## slice

- 只取行（仅使用行号）

  - 单行 `df.iloc[1]`或`df[1]`  => pandas series, 单行 `df.iloc[[1]]`或`df[[1]]`  => dataframe
  - 连续多行`df.iloc[2:4]`或`df[2:4]`  => dataframe
  - 不连续多行`df.iloc[[1,3,5,7]]` ，用逗号，用冒号的时候是连续的索引

- 只取列（仅使用列号）

  - 单列
    - `df['column_name']`  使用列名提取
    - `df.iloc[:,1]`   不知道到列名的时候，使用index提取。也可以省略iloc
  - 不连续多列
    - `df['column_name_1','column_name_2','column_name_3']`  使用列名提取
    - `df.iloc[:,[1,3,5,7]]`   不知道到列名的时候，使用index提取。也可以省略iloc
  - 连续列
    - `df[:,'column_name_1':'column_name_3']`  使用列名提取，这里取了3列
    - `df.iloc[:,0:4]`   不知道到列名的时候，使用index提取。也可以省略iloc

- 同时取行和列。必须使用`iloc`或`loc`，不能省略

  - 使用列index

    ```text
    df.iloc[[1,3],[0]] # dataframe
    df.iloc[[1,3],0] # series
    df.iloc[[1,3],1:3] # series
    df.iloc[[1,3],[1,3]]# dataframe
    ```

  - 使用列名

    ```text
    df.loc[1,["A","D"]] # series 
    df.loc[[1],["A","D"]] # dataframe
    df.loc[[1,3],"A":"D"] # series
    df.loc[[1,3],["A","D"]] # dataframe
    ```

```python
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
    return employees[:3]
```

# [2880. 数据选取](https://leetcode.cn/problems/select-data/)

```
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

编写一个解决方案，选择 `student_id = 101` 的学生的 name 和 age 并输出。

返回结果格式如下示例所示。

 

示例 1:

```
输入：
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
输出：
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
解释：
学生 Ulysses 的 student_id = 101，所以我们输出了他的 name 和 age。
```

```python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
    # fetch row data which student_id = 101
    target_student = students[students['student_id'] == 101]
    info = target_student.iloc[:,1:]

    return info
```

# [2881. 创建新列](https://leetcode.cn/problems/create-a-new-column/)

```
DataFrame employees
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+
```

一家公司计划为员工提供奖金。

编写一个解决方案，创建一个名为 `bonus` 的新列，其中包含 `salary` 值的 两倍。

返回结果格式如下示例所示。

 

示例 1:

```
输入：
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
输出：
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  |  593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
解释：
通过将 salary 列中的值加倍创建了一个新的 bonus 列。
```

```python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['bonus'] = employees['salary']2

    return employees
```

# [2882. 删去重复的行](https://leetcode.cn/problems/drop-duplicate-rows/)

```
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
```

在 DataFrame 中基于 `email` 列存在一些重复行。

编写一个解决方案，删除这些重复行，仅保留第一次出现的行。

返回结果格式如下例所示。

 

示例 1:

```
输入：
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
输出：
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
解释：
Alice (customer_id = 4) 和 Finn (customer_id = 5) 都使用 john@example.com，因此只保留该邮箱地址的第一次出现。
```

## `duplicated()`找到重复的行

重复出现的行标记为true(同样的行数据，第二次出现才算重复)

```python
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    
    unique_customers = customers[~customers['email'].duplicated()]

    return unique_customers
```

# [2883. 删去丢失的数据](https://leetcode.cn/problems/drop-missing-data/)

```
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

在 `name` 列里有一些具有缺失值的行。

编写一个解决方案，删除具有缺失值的行。

返回结果格式如下示例所示。

 

示例 1:

```
输入：
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
输出：
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 779        | Georgia | 20  | 
| 849        | Willow  | 14  | 
+------------+---------+-----+
解释：
学号为 217 的学生所在行在 name 列中有空值，因此这一行将被删除。
```

## 删除空值所在的行/列

- 整张表进行空值查询，然后删除行/列：`df.dropna()`/`df.dropna(axis=1)`
- 如果针对特定的列进行查询，然后删除行：`df[~df['colunm_name'].isnull()]`
- 

```python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    dropna_student = students[~students['name'].isnull()]

    return dropna_student
```

# [2884. 修改列](https://leetcode.cn/problems/modify-columns/)

```
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
```

一家公司决定增加员工的薪水。

编写一个解决方案，将每个员工的薪水乘以2来 修改 `salary` 列。

返回结果格式如下示例所示。

 

示例 1:

```
输入：
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
输出：
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
解释：
每个人的薪水都被加倍。
```

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['salary'] = employees['salary']2

    return employees
```

# [2885. 重命名列](https://leetcode.cn/problems/rename-columns/)

```
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
```

编写一个解决方案，按以下方式重命名列：

- `id` 重命名为 `student_id`
- `first` 重命名为 `first_name`
- `last` 重命名为 `last_name`
- `age` 重命名为 `age_in_years`

返回结果格式如下示例所示。

 

示例 1:

```
输入：
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
输出：
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
解释：
列名已相应更换。
```

```python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    
    students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'}, inplace=True)

    return students
```

# [2886. 改变数据类型](https://leetcode.cn/problems/change-data-type/)

```
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
```

编写一个解决方案来纠正以下错误：

 `grade` 列被存储为浮点数，将它转换为整数。

返回结果格式如下示例所示。

 

示例 1:

```
输入：
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
输出：
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
解释：
grade 列的数据类型已转换为整数。
```

## 数据类型转换`astype`

`df['column_name'].astype('int')` =  `df.astype({'column_name':'int'})`

## 查看数据类型`dtypes`

`df.dtypes()`会返回每个字段的数据类型，以及DataFrame整体的类型。

如果是针对series,需要使用`dtype()`

```python
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    
    students['grade'] = students['grade'].astype('int')

    return students
```

# [2887. 填充缺失值](https://leetcode.cn/problems/fill-missing-data/)

```
DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
```

编写一个解决方案，在 `quantity` 列中将缺失的值填充为 `0`。

返回结果如下示例所示。

 

示例 1：

```
输入：
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | None     | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
输出：
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 0        | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
解释：
Toaster 和 Headphones 的数量被填充为 0。
```

## 填充空值`fillna`

`fillna(value, inplace=True)`

```python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    
    products['quantity'].fillna(0, inplace=True)

    return products
```

# [2888. 重塑数据：连结](https://leetcode.cn/problems/reshape-data-concatenate/)

```
DataFrame df1
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame df2
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```

编写一个解决方案，将两个 DataFrames 垂直 连接成一个 DataFrame。

结果格式如下示例所示。

 

示例 1：

```
输入：
df1
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
df2
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
输出：
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
解释：
两个 DataFrame 被垂直堆叠，它们的行被合并。
```

## 合并多个dataframe `contact()` [pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

- `pd.concat(objs, , axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=None)`：pandas 内部的一个方便的函数，用于垂直(按行)或水平(按列)连接 DataFrame。

- objs 参数是一个要串联的 Series 或 DataFrame 对象的序列或映射。

- axis 参数决定连接的方向：

- axis=0 设置为缺省值，这意味着它将垂直(按行)连接 DataFrame。

- axis=1 将水平连接 DataFrame(按列)。

- join{‘inner’, ‘outer’}, default ‘outer’

  How to handle indexes on other axis (or axes).

- ignore_indexbool, default False

  If True, do not use the index values along the concatenation axis. The resulting axis will be labeled 0, …, n - 1. This is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information. Note the index values on the other axes are still respected in the join.

```python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    new_df = pd.concat([df1,df2], axis=0)

    return new_df
```

# [2889. 数据重塑：透视](https://leetcode.cn/problems/reshape-data-pivot/)

```
DataFrame weather
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
```

编写一个解决方案，以便将数据 旋转，使得每一行代表特定月份的温度，而每个城市都是一个单独的列。

输出结果格式如下示例所示。

 

示例 1:

```
输入：
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
输出：
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
解释：
表格被旋转，每一列代表一个城市，每一行代表特定的月份。
```

## 透视 `pivot_table`

`pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False) `

- data：[dataframe](https://zhida.zhihu.com/search?content_id=147510197&content_type=Article&match_order=1&q=dataframe&zhida_source=entity)格式数据
- values：需要汇总计算的列，可多选
- index：行分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的行索引
- columns：列分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的列索引
- aggfunc：聚合函数或[函数列表](https://zhida.zhihu.com/search?content_id=147510197&content_type=Article&match_order=1&q=函数列表&zhida_source=entity)，默认为平均值
- fill_value：设定缺失替换值
- margins：是否添加行列的总计
- dropna：默认为True，如果列的所有值都是NaN，将不作为计算列，False时，被保留
- margins_name：汇总行列的名称，默认为All
- observed：是否显示观测值



```python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    
    pivot_weather = pd.pivot_table(weather, values='temperature', index='month', columns='city')

    return pivot_weather

```

# [2890. 重塑数据：融合](https://leetcode.cn/problems/reshape-data-melt/)

```
DataFrame report
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
```

编写一个解决方案，将数据 重塑 成每一行表示特定季度产品销售数据的形式。

结果格式如下例所示：

 

示例 1：

```
输入：
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
输出：
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
解释：
DataFrame 已从宽格式重塑为长格式。每一行表示一个季度内产品的销售情况。
```

## `pd.melt()` 重塑DataFrame

![使用Pandas melt()重塑DataFrame](https://picx.zhimg.com/70/v2-bc8f8306eb20320098f0e17d9241b897_1440w.image?source=172ae18b&biz_tag=Post)

`pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`

The function is useful to massage a DataFrame into a format where one or more columns are identifier variables(id_vars), while all other columns, considered measured variables(value_vars), are "unpivoted" to the row aixs, leaving just two non-identifier columns, 'variable' and 'value'.

- **id_vars**scalar, tuple, list, or ndarray, optional

  Column(s) to use as identifier variables.

- **value_vars**scalar, tuple, list, or ndarray, optional

  Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.

- **var_name**scalar, default None

  Name to use for the ‘variable’ column. If None it uses `frame.columns.name` or ‘variable’.

- **value_name**scalar, default ‘value’

  Name to use for the ‘value’ column, can’t be an existing column label.

- **col_level**scalar, optional

  If columns are a MultiIndex then use this level to melt.

- **ignore_index**bool, default True

  If True, original index is ignored. If False, the original index is retained. Index labels will be repeated as necessary.

```python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    
    melt_report = report.melt(
        id_vars = 'product', 
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name = 'quarter', 
        value_name = 'sales'
        )

    return melt_report
```

# [2891. 方法链](https://leetcode.cn/problems/method-chaining/)

```
DataFrame animals
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |
+-------------+--------+
```

编写一个解决方案来列出体重 **严格超过** `100` 千克的动物的名称。

按体重 **降序** 返回动物。

返回结果格式如下示例所示。

 

**示例 1:**

```
输入：
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
输出：
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
解释：
所有体重超过 100 的动物都应包含在结果表中。
Tatiana 的体重为 464，Jonathan 的体重为 463，Tommy 的体重为 349，Alex 的体重为 328。
结果应按体重降序排序。
```

## 方法链

方法链其实是一种编程风格，可以顺序调用多个方法，其中每个方程都在同一个对象上执行操作并将结果返回。它消除了每个中间步骤命名变量的思维负担，创建面向对象API的方法依赖于方法链（method chaining），类似unix系统的管道操作。

Pandas 提供了非常多的方法链, 例如：

- assign():增加一列，替代（ data['newcolumn'] = data['B'] + 1）方法，参与方法链
- rename()：重命名
- query()： 筛选
- pipe()
- sort_values()
- reset_index()
- loc()

```python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    return animals.query('weight>100').sort_values(by='weight',ascending=False)[['name']]
```

