

# 查询

## [1757. 可回收且低脂的产品](https://leetcode.cn/problems/recyclable-and-low-fat-products/)

表：`Products`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id 是该表的主键（具有唯一值的列）。
low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。
```

 

编写解决方案找出既是低脂又是可回收的产品编号。

返回结果 **无顺序要求** 。

返回结果格式如下例所示：

 

**示例 1：**

```
输入：
Products 表：
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
输出：
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
解释：
只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。
```

Oracle:

```sql
/* Write your PL/SQL query statement below */

select product_id from Products where low_fats = 'Y' and recyclable = 'Y';
```

Pandas:

```python
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

    product_id_frame = pd.DataFrame(products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]['product_id'])

    return product_id_frame
```



## [584. 寻找用户推荐人](https://leetcode.cn/problems/find-customer-referee/)

表: `Customer`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
在 SQL 中，id 是该表的主键列。
该表的每一行表示一个客户的 id、姓名以及推荐他们的客户的 id。
```

找出那些 **没有被** `id = 2` 的客户 **推荐** 的客户的姓名。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1：**

```
输入： 
Customer 表:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
输出：
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

Oracle:

```sql
/* Write your PL/SQL query statement below */
select name from Customer where referee_id != 2 or referee_id is null;
```

Pandas:

```python
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    
    name = pd.DataFrame(customer.loc[~customer['referee_id'].isin([2])]['name'])
    
    return name
```

## [595. 大的国家](https://leetcode.cn/problems/big-countries/)

`World` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name 是该表的主键（具有唯一值的列）。
这张表的每一行提供：国家名称、所属大陆、面积、人口和 GDP 值。
```

 

如果一个国家满足下述两个条件之一，则认为该国是 **大国** ：

- 面积至少为 300 万平方公里（即，`3000000 km2`），或者
- 人口至少为 2500 万（即 `25000000`）

编写解决方案找出 **大国** 的国家名称、人口和面积。

按 **任意顺序** 返回结果表。

返回结果格式如下例所示。

 

**示例：**

```
输入：
World 表：
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
输出：
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

MySQL:

```sql
# Write your MySQL query statement below

select name, population, area from World where area >= 3000000 or population >= 25000000;
```

Pandas:

```Python
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    big_coutries_info = pd.DataFrame(world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000),['name','population','area']])

    return big_coutries_info
```

可以通过loc或者iloc进行条件查找，也可以直接使用`query`来简化代码，结果作为 DataFrame 返回。原始 DataFrame 保持不变。如果要更新原始 DataFrame，需要使用 `inplace` 参数

`query()` 方法中的[表达式](https://zhida.zhihu.com/search?q=表达式&zhida_source=entity&is_preview=1)类似于 SQL 中的 WHERE 语句。

```python
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    big_coutries_info = world.query('area>= 3000000 or population >= 25000000' )[['name','population','area']]

    return big_coutries_info

```

## [1148. 文章浏览 I](https://leetcode.cn/problems/article-views-i/)

`Views` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
此表可能会存在重复行。（换句话说，在 SQL 中这个表没有主键）
此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
请注意，同一人的 author_id 和 viewer_id 是相同的。
```

 

请查询出所有浏览过自己文章的作者

结果按照 `id` 升序排列。

查询结果的格式如下所示：

 

**示例 1：**

```
输入：
Views 表：
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

输出：
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

Mysql:

```sql
# Write your MySQL query statement below

select distinct(author_id) id from Views where viewer_id = author_id order by author_id asc
```

Pandas:

```python
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # find author_id = viewer_id
    id_list = views.query("author_id==viewer_id")[['author_id']]
    # duplicate same id
    id_unique = id_list.drop_duplicates()
    # sort id by asc
    sorted_id = id_unique.sort_values('author_id', ascending=True)
    # rename column name
    sorted_id.rename(columns={'author_id':'id'}, inplace = True)

    return sorted_id
```

## [1683. 无效的推文](https://leetcode.cn/problems/invalid-tweets/)

表：`Tweets`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
在 SQL 中，tweet_id 是这个表的主键。
这个表包含某社交媒体 App 中所有的推文。
```

 

查询所有无效推文的编号（ID）。当推文内容中的字符数**严格大于** `15` 时，该推文是无效的。

以**任意顺序**返回结果表。

查询结果格式如下所示：

 

**示例 1：**

```
输入：
Tweets 表：
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+

输出：
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
解释：
推文 1 的长度 length = 14。该推文是有效的。
推文 2 的长度 length = 32。该推文是无效的。
```

Mysql:

`length()`: 返回以**字节为单位的字符串**的长度

`char_length()`: 返回**字符串**长度

```sql
# Write your MySQL query statement below

select tweet_id from Tweets where char_length(content) > 15;
```

Oracle:  没有`char_length()`

```sql
/* Write your PL/SQL query statement below */

select tweet_id from Tweets where length(content) > 15;
```

Pandas:

```python
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    tweets['content_len'] = tweets['content'].str.len()

    invalid_id = pd.DataFrame(tweets.loc[tweets['content_len'] > 15]['tweet_id'])

    return invalid_id
```

## [1821. 寻找今年具有正收入的客户](https://leetcode.cn/problems/find-customers-with-positive-revenue-this-year/)

表：`Customers`

```
+--------------+------+
| Column Name  | Type |
+--------------+------+
| customer_id  | int  |
| year         | int  |
| revenue      | int  |
+--------------+------+
(customer_id, year) 是该表的主键（具有唯一值的列的组合）。
这个表包含客户 ID 和不同年份的客户收入。
注意，这个收入可能是负数。
```

 

编写一个解决方案来报告 2021 年具有 **正收入** 的客户。

可以以 **任意顺序** 返回结果表。

结果格式如下示例所示。

 

**示例 1:**

```
Input:
Customers
+-------------+------+---------+
| customer_id | year | revenue |
+-------------+------+---------+
| 1           | 2018 | 50      |
| 1           | 2021 | 30      |
| 1           | 2020 | 70      |
| 2           | 2021 | -50     |
| 3           | 2018 | 10      |
| 3           | 2016 | 50      |
| 4           | 2021 | 20      |
+-------------+------+---------+

Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 4           |
+-------------+
客户 1 在 2021 年的收入等于 30 。
客户 2 在 2021 年的收入等于 -50 。
客户 3 在 2021 年没有收入。
客户 4 在 2021 年的收入等于 20 。
因此，只有客户 1 和 4 在 2021 年有正收入。
```

```sql
/* Write your PL/SQL query statement below */

select customer_id
from customers
where revenue > 0 and year = 2021
```

## [183. 从不订购的客户](https://leetcode.cn/problems/customers-who-never-order/)

`Customers` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
在 SQL 中，id 是该表的主键。
该表的每一行都表示客户的 ID 和名称。
```

`Orders` 表：

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
在 SQL 中，id 是该表的主键。
customerId 是 Customers 表中 ID 的外键( Pandas 中的连接键)。
该表的每一行都表示订单的 ID 和订购该订单的客户的 ID。
```

 

找出所有从不点任何东西的顾客。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1：**

```
输入：
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
输出：
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

```sql
/* Write your PL/SQL query statement below */

select c.name customers
from customers c
left join orders o
on c.id = o.customerId
where o.customerId is null
```

## [1873. 计算特殊奖金](https://leetcode.cn/problems/calculate-special-bonus/)

表: `Employees`

```
+-------------+---------+
| 列名        | 类型     |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id 是这个表的主键(具有唯一值的列)。
此表的每一行给出了雇员id ，名字和薪水。
```

 

编写解决方案，计算每个雇员的奖金。如果一个雇员的 id 是 **奇数** 并且他的名字不是以 `'M'` **开头**，那么他的奖金是他工资的 `100%` ，否则奖金为 `0` 。

返回的结果按照 `employee_id` 排序。

返回结果格式如下面的例子所示。

 

**示例 1:**

```
输入：
Employees 表:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
输出：
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
解释：
因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
其他的雇员得到了百分之百的奖金。
```

```sql
/* Write your PL/SQL query statement below */

select employee_id,
case when name not like 'M%' and mod(employee_id,2)=1 then salary else 0 end as bonus
from employees
order by employee_id asc
```

## [1398. 购买了产品 A 和产品 B 却没有购买产品 C 的顾客](https://leetcode.cn/problems/customers-who-bought-products-a-and-b-but-not-c/)

 `Customers` 表：

```
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id 是这张表中具有唯一值的列。
customer_name 是顾客的名称。
```

 

`Orders` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id 是这张表中具有唯一值的列。
customer_id 是购买了名为 "product_name" 产品顾客的id。
```

 

请你编写解决方案，报告购买了产品 **"A"**，**"B"** 但没有购买产品 **"C"** 的客户的 customer_id 和 customer_name，因为我们想推荐他们购买这样的产品。

返回按 `customer_id` **排序** 的结果表。

返回结果格式如下所示。

 

**示例 1：**

```
输入：
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+

Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
输出：
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
解释：
只有 customer_id 为 3 的顾客购买了产品 A 和产品 B ，却没有购买产品 C 。
```

```sql
/* Write your PL/SQL query statement below */


select pl.customer_id customer_id, c.customer_name customer_name
from customers c,
(
select customer_id, 
listagg(product_name,',') within group (order by product_name) product_list
from orders
group by customer_id
) pl
where pl.product_list  like '%A%B%' and pl.product_list not like '%C%' and pl.customer_id = c.customer_id
```

## [1112. 每位学生的最高成绩](https://leetcode.cn/problems/highest-grade-for-each-student/)

表：`Enrollments`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) 是该表的主键（具有唯一值的列的组合）。
grade 不会为 NULL。
```

 

编写解决方案，找出每位学生获得的最高成绩和它所对应的科目，若科目成绩并列，取 `course_id` 最小的一门。查询结果需按 `student_id` 增序进行排序。

查询结果格式如下所示。

 

**示例 1：**

```
输入：
Enrollments 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
输出：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```

```sql
/* Write your PL/SQL query statement below */


select student_id, course_id, grade
from
(
    select student_id, course_id, grade,
rank() over (partition by student_id order by grade desc, course_id asc) ranks
from enrollments
)
where ranks=1
```



# 连接

![img](https://www.runoob.com/wp-content/uploads/2019/01/sql-join.png)



## [1378. 使用唯一标识码替换员工ID](https://leetcode.cn/problems/replace-employee-id-with-the-unique-identifier/)

`Employees` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
在 SQL 中，id 是这张表的主键。
这张表的每一行分别代表了某公司其中一位员工的名字和 ID 。
```

 

`EmployeeUNI` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
在 SQL 中，(id, unique_id) 是这张表的主键。
这张表的每一行包含了该公司某位员工的 ID 和他的唯一标识码（unique ID）。
```

 

展示每位用户的 **唯一标识码（unique ID ）**；如果某位员工没有唯一标识码，使用 null 填充即可。

你可以以 **任意** 顺序返回结果表。

返回结果的格式如下例所示。

 

**示例 1：**

```
输入：
Employees 表:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI 表:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
输出：
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
解释：
Alice and Bob 没有唯一标识码, 因此我们使用 null 替代。
Meir 的唯一标识码是 2 。
Winston 的唯一标识码是 3 。
Jonathan 唯一标识码是 1 。
```

sql

```sql
# Write your MySQL query statement below

select b.unique_id, a.name from Employees a
left join EmployeeUNI b 
on  a.id = b.id
```

pandas

### `merge()`进行合并，类似sql的`join`

[pandas.DataFrame.merge — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)

`DataFrame.merge(right,how='inner',on=None,left_on=None,right_on=None,left_index=False,right_index=False,sort=False,suffixes=('_x', '_y'),copy=None,indicator=False,validate=None)`

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    new_pd = employees.merge(employee_uni, how = 'left', on = 'id')
    order = ['unique_id','name']
    new_pd = new_pd[order]
    return new_pd
    
```

## [1068. 产品销售分析 I](https://leetcode.cn/problems/product-sales-analysis-i/)

销售表 `Sales`：

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) 是销售表 Sales 的主键（具有唯一值的列的组合）。
product_id 是关联到产品表 Product 的外键（reference 列）。
该表的每一行显示 product_id 在某一年的销售情况。
注意: price 表示每单位价格。
```

产品表 `Product`：

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id 是表的主键（具有唯一值的列）。
该表的每一行表示每种产品的产品名称。
```

 

编写解决方案，以获取 `Sales` 表中所有 `sale_id` 对应的 `product_name` 以及该产品的所有 `year` 和 `price` 。

返回结果表 **无顺序要求** 。

结果格式示例如下。

 

**示例 1：**

```
输入：
Sales 表：
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product 表：
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
输出：
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
```

sql

```sql
/* Write your PL/SQL query statement below */

select p.product_name, s.year, s.price
from Sales s
left join Product p
on s.product_id = p.product_id
```

pandas

```python
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    combination = sales.merge(product, how = 'left', on = 'product_id')
    col = ['product_name', 'year', 'price']
    combination = combination[col]
    return combination
```

## [1070. Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/)

```
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 

Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
```

```sql
/* Write your PL/SQL query statement below */

select product_id, year first_year, quantity, price
from(
select product_id, year, quantity, price,
rank() over (partition by product_id order by year) ranks
from sales)
where ranks=1
```

## [1581. 进店却未进行过交易的顾客](https://leetcode.cn/problems/customer-who-visited-but-did-not-make-any-transactions/)

表：`Visits`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id 是该表中具有唯一值的列。
该表包含有关光临过购物中心的顾客的信息。
```

 

表：`Transactions`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id 是该表中具有唯一值的列。
此表包含 visit_id 期间进行的交易的信息。
```

 

有一些顾客可能光顾了购物中心但没有进行交易。请你编写一个解决方案，来查找这些顾客的 ID ，以及他们只光顾不交易的次数。

返回以 **任何顺序** 排序的结果表。

返回结果格式如下例所示。

 

**示例 1：**

```
输入:
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
输出:
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
解释:
ID = 23 的顾客曾经逛过一次购物中心，并在 ID = 12 的访问期间进行了一笔交易。
ID = 9 的顾客曾经逛过一次购物中心，并在 ID = 13 的访问期间进行了一笔交易。
ID = 30 的顾客曾经去过购物中心，并且没有进行任何交易。
ID = 54 的顾客三度造访了购物中心。在 2 次访问中，他们没有进行任何交易，在 1 次访问中，他们进行了 3 次交易。
ID = 96 的顾客曾经去过购物中心，并且没有进行任何交易。
如我们所见，ID 为 30 和 96 的顾客一次没有进行任何交易就去了购物中心。顾客 54 也两次访问了购物中心并且没有进行任何交易。
```

sql

```sql
/* Write your PL/SQL query statement below */

select customer_id,count(customer_id) count_no_trans
from
(select v.customer_id customer_id, t.transaction_id transaction_id
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is null)
group by customer_id

```

pandas

```python
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # drop duplicated visit id
    visited = transactions['visit_id'].drop_duplicates()
    # using visited id to find out which customers did't visit or visited but not shopping.
    # using value_counts to count how many times for each customer. Then index is customer_id
    # using reset_index to release customer_id to a column.
    not_visited = visits[~visits['visit_id'].isin(visited)].value_counts('customer_id').reset_index()
    order = {'customer_id':'customer_id','count':'count_no_trans'}
    not_visited = not_visited.rename(columns = order)

    return not_visited
```

## [197. 上升的温度](https://leetcode.cn/problems/rising-temperature/)

表： `Weather`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id 是该表具有唯一值的列。
没有具有相同 recordDate 的不同行。
该表包含特定日期的温度信息
```

 

编写解决方案，找出与之前（昨天的）日期相比温度更高的所有日期的 `id` 。

返回结果 **无顺序要求** 。

结果格式如下例子所示。

 

**示例 1：**

```
输入：
Weather 表：
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
输出：
+----+
| id |
+----+
| 2  |
| 4  |
+----+
解释：
2015-01-02 的温度比前一天高（10 -> 25）
2015-01-04 的温度比前一天高（20 -> 30）
```

sql

### 日期转换，以及加减

Mysql:

- `date_sub(date, interval number day)`  减多少天
- `date_sub(date, interval number year)` 减多少年
- `date_add(date, interval number day)` 加多少天

Oracle:

先将数据转换为日期格式，然后字节加减。例如`to_date(date) -1`  减一天

或者：

`add_days(to_date(date, 'yyyy-mm-dd'),  days)`



```sql
# Write your MySQL query statement below

select a.id
from Weather a
left join  Weather b
on date_sub(a.recordDate, interval 1 day) = b.recordDate
where a.Temperature > b.Temperature
```

```sql
/* Write your PL/SQL query statement below */

select a.id
from Weather a
left join  Weather b
on to_date(a.recordDate) -1  = b.recordDate
where a.Temperature > b.Temperature
```

pandas

```python
import pandas as pd
import datetime

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    # check type of each column
    #print(weather.dtypes)
    # if recordDate isn't a datetime type then transform it to date
    #weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    merge_weather = weather.merge(weather, how = 'left', left_on = (weather['recordDate'] + datetime.timedelta(days=-1)), right_on = 'recordDate')
    y = merge_weather.query('temperature_x > temperature_y')
    pd_id = y[['id_x']]
    pd_id = pd_id.rename(columns = {'id_x':'id'})
    
    return pd_id
```

## [1661. 每台机器的进程平均运行时间](https://leetcode.cn/problems/average-time-of-process-per-machine/)

表: `Activity`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
该表展示了一家工厂网站的用户活动。
(machine_id, process_id, activity_type) 是当前表的主键（具有唯一值的列的组合）。
machine_id 是一台机器的ID号。
process_id 是运行在各机器上的进程ID号。
activity_type 是枚举类型 ('start', 'end')。
timestamp 是浮点类型,代表当前时间(以秒为单位)。
'start' 代表该进程在这台机器上的开始运行时间戳 , 'end' 代表该进程在这台机器上的终止运行时间戳。
同一台机器，同一个进程都有一对开始时间戳和结束时间戳，而且开始时间戳永远在结束时间戳前面。
```

 

现在有一个工厂网站由几台机器运行，每台机器上运行着 **相同数量的进程** 。编写解决方案，计算每台机器各自完成一个进程任务的平均耗时。

完成一个进程任务的时间指进程的`'end' 时间戳` 减去 `'start' 时间戳`。平均耗时通过计算每台机器上所有进程任务的总耗费时间除以机器上的总进程数量获得。

结果表必须包含`machine_id（机器ID）` 和对应的 **average time（平均耗时）** 别名 `processing_time`，且**四舍五入保留3位小数。**

以 **任意顺序** 返回表。

具体参考例子如下。

**示例 1:**

```
输入：
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
输出：
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+
解释：
一共有3台机器,每台机器运行着两个进程.
机器 0 的平均耗时: ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
机器 1 的平均耗时: ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
机器 2 的平均耗时: ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456
```

sql

```sql
# Write your MySQL query statement below

select a.machine_id, round(sum(b.timestamp-a.timestamp) / count(a.process_id),3) 'processing_time'
from Activity a
left join (select * from Activity where activity_type = 'end') b
on a.machine_id = b.machine_id and a.process_id = b.process_id
where a.activity_type = 'start'
group by a.machine_id
```

pandas

### using `groupby()` to calculate average number based on each group.

```python
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    
    # fetch end time for each start point
    result = activity[activity['activity_type'] == 'start'].merge(activity[activity['activity_type'] == 'end'], how = 'left', on =['machine_id','process_id'])
    # calculate each process using time
    result['processing_time'] = result['timestamp_y'] - result['timestamp_x']
    # get average time based on group by machine_id
    average_time = result.groupby(['machine_id'])['processing_time'].mean().reset_index()
    # set processing_time to three decimal places
    average_time['processing_time'] = average_time['processing_time'].round(3)

    return average_time
```

## [577. 员工奖金](https://leetcode.cn/problems/employee-bonus/)

表：`Employee` 

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId 是该表中具有唯一值的列。
该表的每一行都表示员工的姓名和 id，以及他们的工资和经理的 id。
```

 

表：`Bonus`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId 是该表具有唯一值的列。
empId 是 Employee 表中 empId 的外键(reference 列)。
该表的每一行都包含一个员工的 id 和他们各自的奖金。
```

 

编写解决方案，报告每个奖金 **少于** `1000` 的员工的姓名和奖金数额。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1：**

```
输入：
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
输出：
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
```

sql

```sql
/* Write your PL/SQL query statement below */

select e.name name , b.bonus bonus
from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null
```

pandas

```python
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    # Find each employee's bonus, using left join
    merge_pd = employee.merge(bonus, how = 'left', on = 'empId')
    # Find whose bonus is less than 1000 or no bonus
    condition_pd = merge_pd.query('bonus < 1000 or bonus.isnull()')
    # write target column to a dataframe
    result = condition_pd[['name', 'bonus']]

    return result
```



## [1280. 学生们参加各科测试的次数](https://leetcode.cn/problems/students-and-examinations/)

学生表: `Students`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
在 SQL 中，主键为 student_id（学生ID）。
该表内的每一行都记录有学校一名学生的信息。
```

 

科目表: `Subjects`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
在 SQL 中，主键为 subject_name（科目名称）。
每一行记录学校的一门科目名称。
```

 

考试表: `Examinations`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
这个表可能包含重复数据（换句话说，在 SQL 中，这个表没有主键）。
学生表里的一个学生修读科目表里的每一门科目。
这张考试表的每一行记录就表示学生表里的某个学生参加了一次科目表里某门科目的测试。
```

 

查询出每个学生参加每一门科目测试的次数，结果按 `student_id` 和 `subject_name` 排序。

查询结构格式如下所示。

 

**示例 1：**

```
输入：
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
输出：
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
解释：
结果表需包含所有学生和所有科目（即便测试次数为0）：
Alice 参加了 3 次数学测试, 2 次物理测试，以及 1 次编程测试；
Bob 参加了 1 次数学测试, 1 次编程测试，没有参加物理测试；
Alex 啥测试都没参加；
John  参加了数学、物理、编程测试各 1 次。
```

sql

```sql
/* Write your PL/SQL query statement below */

select s.student_id, s.student_name, s.subject_name, count(e.student_id) attended_exams
from (select * from Students cross join Subjects) s
left join Examinations e
on s.student_id = e.student_id and s.subject_name  = e.subject_name 
group by s.student_id, s.subject_name, s.student_name
order by s.student_id, s.subject_name
```

pandas

```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    # create a big table mapping each student to subjects
    student_subject = students.merge(subjects, how = 'cross')

    # Using examinations to calculate attended nums for each student-subject
    examinations['attended_exams'] = examinations['subject_name']
    count_exam = examinations.groupby(['student_id','subject_name'])['attended_exams'].count().reset_index()

    # Making a mapping based on step1 and step2 to show attended number for each student for each subject
    student_examination = student_subject.merge(count_exam, how = 'left', on = ['student_id', 'subject_name'])

    # inplace null to 0 on attended_exams column
    student_examination['attended_exams'].fillna(value=0, inplace= True)

    # sort columns
    student_examination.sort_values(['student_id','subject_name'], inplace = True, ascending = True)


    return student_examination
```

## [570. 至少有5名直接下属的经理](https://leetcode.cn/problems/managers-with-at-least-5-direct-reports/)

表: `Employee`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id 是此表的主键（具有唯一值的列）。
该表的每一行表示雇员的名字、他们的部门和他们的经理的id。
如果managerId为空，则该员工没有经理。
没有员工会成为自己的管理者。
```

 

编写一个解决方案，找出至少有**五个直接下属**的经理。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

**示例 1:**

```
输入: 
Employee 表:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | Null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
输出: 
+------+
| name |
+------+
| John |
+------+
```

sql

```sql
# Write your MySQL query statement below
select e.name
from Employee e
right join (select managerId, count(managerId) manager_count
from Employee group by managerId) m
on m.managerId = e.id
where m.manager_count >= 5 and m.managerId = e.id
```

pandas

```python
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    # count mangerId
    managers_id = employee['managerId'].value_counts().reset_index()
    
    # find managers' name whose employees' num is more 5
    managers = managers_id.merge(employee, how = 'left', left_on = 'managerId', right_on = 'id').query('count>=5 and managerId_x == id')

    return managers[['name']]
```

## [1934. 确认率](https://leetcode.cn/problems/confirmation-rate/)

表: `Signups`

```
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
User_id是该表的主键。
每一行都包含ID为user_id的用户的注册时间信息。
```

 

表: `Confirmations`

```
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp)是该表的主键。
user_id是一个引用到注册表的外键。
action是类型为('confirmed'， 'timeout')的ENUM
该表的每一行都表示ID为user_id的用户在time_stamp请求了一条确认消息，该确认消息要么被确认('confirmed')，要么被过期('timeout')。
```

 

用户的 **确认率** 是 `'confirmed'` 消息的数量除以请求的确认消息的总数。没有请求任何确认消息的用户的确认率为 `0` 。确认率四舍五入到 **小数点后两位** 。

编写一个SQL查询来查找每个用户的 确认率 。

以 任意顺序 返回结果表。

查询结果格式如下所示。

**示例1:**

```
输入：
Signups 表:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations 表:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
输出: 
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
解释:
用户 6 没有请求任何确认消息。确认率为 0。
用户 3 进行了 2 次请求，都超时了。确认率为 0。
用户 7 提出了 3 个请求，所有请求都得到了确认。确认率为 1。
用户 2 做了 2 个请求，其中一个被确认，另一个超时。确认率为 1 / 2 = 0.5。
```

sql

```sql
# Write your MySQL query statement below

select s.user_id, case when r.confirmation_rate is null then 0 else r.confirmation_rate end confirmation_rate
from Signups s
left join (select t.user_id, t.total_action, c.confirmed , round(c.confirmed/t.total_action,2) confirmation_rate 
from (select user_id, count(action) total_action
from Confirmations
group by user_id) t
left join (select user_id, count(action) confirmed
from Confirmations
where action = 'confirmed'
group by user_id) c
on t.user_id = c.user_id ) r
on s.user_id = r.user_id
```

```sql
# Write your MySQL query statement below

SELECT
    s.user_id,
    ROUND(IFNULL(AVG(c.action='confirmed'), 0), 2) AS confirmation_rate
FROM
    Signups AS s
LEFT JOIN
    Confirmations AS c
ON
    s.user_id = c.user_id
GROUP BY
    s.user_id
```

pandas

### `round()` 设置小数点位数。

### `fillna()`填充空值

```python
import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    # count confirmed for each user
    count_actions = confirmations.groupby('user_id')['action'].value_counts('confirmed').reset_index()
    count_confirmed = count_actions[count_actions['action']=='confirmed']
    # keep two decimal places
    count_confirmed['proportion'] = count_confirmed['proportion'].round(2)
    # find confirmed rate for each user
    confirmed = signups.merge(count_confirmed, how='left',on='user_id')
    # replace null to zero
    confirmed['proportion'].fillna(value=0, inplace=True)
    # change column name
    confirmed.rename(columns={'proportion':'confirmation_rate'}, inplace=True)


    return confirmed[['user_id','confirmation_rate']]
```

## [175. 组合两个表](https://leetcode.cn/problems/combine-two-tables/)

表: `Person`

```
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
personId 是该表的主键（具有唯一值的列）。
该表包含一些人的 ID 和他们的姓和名的信息。
```

 

表: `Address`

```
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
addressId 是该表的主键（具有唯一值的列）。
该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。
```

 

编写解决方案，报告 `Person` 表中每个人的姓、名、城市和州。如果 `personId` 的地址不在 `Address` 表中，则报告为 `null` 。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1:**

```
输入: 
Person表:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address表:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
输出: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
解释: 
地址表中没有 personId = 1 的地址，所以它们的城市和州返回 null。
addressId = 1 包含了 personId = 2 的地址信息。
```

```sql
/* Write your PL/SQL query statement below */

select p.firstname, p.lastname, a.city, a.state
from person p
left join address a
on p.personid = a.personid
```

## [1607. 没有卖出的卖家](https://leetcode.cn/problems/sellers-with-no-sales/)

表: `Customer`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id 是该表具有唯一值的列。
该表的每行包含网上商城的每一位顾客的信息。
```

 

表: `Orders`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| sale_date     | date    |
| order_cost    | int     |
| customer_id   | int     |
| seller_id     | int     |
+---------------+---------+
order_id 是该表具有唯一值的列。
该表的每行包含网上商城的所有订单的信息.
sale_date 是顾客 customer_id 和卖家 seller_id 之间交易的日期.
```

 

表: `Seller`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| seller_id     | int     |
| seller_name   | varchar |
+---------------+---------+
seller_id 是该表主具有唯一值的列。
该表的每行包含每一位卖家的信息.
```

 

写一个解决方案, 报告所有在 `2020` 年度没有任何卖出的卖家的名字。

返回结果按照 `seller_name` **升序排列。**

查询结果格式如下例所示。

 

**示例 1:**

```
输入：
Customer 表:
+--------------+---------------+
| customer_id  | customer_name |
+--------------+---------------+
| 101          | Alice         |
| 102          | Bob           |
| 103          | Charlie       |
+--------------+---------------+
Orders 表:
+-------------+------------+--------------+-------------+-------------+
| order_id    | sale_date  | order_cost   | customer_id | seller_id   |
+-------------+------------+--------------+-------------+-------------+
| 1           | 2020-03-01 | 1500         | 101         | 1           |
| 2           | 2020-05-25 | 2400         | 102         | 2           |
| 3           | 2019-05-25 | 800          | 101         | 3           |
| 4           | 2020-09-13 | 1000         | 103         | 2           |
| 5           | 2019-02-11 | 700          | 101         | 2           |
+-------------+------------+--------------+-------------+-------------+
Seller 表:
+-------------+-------------+
| seller_id   | seller_name |
+-------------+-------------+
| 1           | Daniel      |
| 2           | Elizabeth   |
| 3           | Frank       |
+-------------+-------------+
输出：
+-------------+
| seller_name |
+-------------+
| Frank       |
+-------------+
解释：
Daniel 在 2020 年 3 月卖出 1 次。
Elizabeth 在 2020 年卖出 2 次, 在 2019 年卖出 1 次。
Frank 在 2019 年卖出 1 次, 在 2020 年没有卖出。
```

```sql
/* Write your PL/SQL query statement below */

select s.seller_name
from seller s
left join (select * from orders where to_char(sale_date,'yyyy') = '2020') o
on s.seller_id = o.seller_id 
where o.seller_id is null 
order by seller_name asc
```

## [1407. 排名靠前的旅行者](https://leetcode.cn/problems/top-travellers/)

表：`Users`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id 是该表中具有唯一值的列。
name 是用户名字。
```

 

表：`Rides`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id 是该表中具有唯一值的列。
user_id 是本次行程的用户的 id, 而该用户此次行程距离为 distance 。
```

 

编写解决方案，报告每个用户的旅行距离。

返回的结果表单，以 `travelled_distance` **降序排列** ，如果有两个或者更多的用户旅行了相同的距离, 那么再以 `name` **升序排列** 。

返回结果格式如下例所示。

 

**示例 1：**

```
输入：
Users 表：
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 7    | Lee       |
| 13   | Jonathan  |
| 19   | Elvis     |
+------+-----------+

Rides 表：
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 7        | 100      |
| 5    | 13       | 312      |
| 6    | 19       | 50       |
| 7    | 7        | 120      |
| 8    | 19       | 400      |
| 9    | 7        | 230      |
+------+----------+----------+
输出：
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+
解释：
Elvis 和 Lee 旅行了 450 英里，Elvis 是排名靠前的旅行者，因为他的名字在字母表上的排序比 Lee 更小。
Bob, Jonathan, Alex 和 Alice 只有一次行程，我们只按此次行程的全部距离对他们排序。
Donald 没有任何行程, 他的旅行距离为 0。
```

```sql
/* Write your PL/SQL query statement below */

select u.name, nvl(d.total_distance,0) travelled_distance
from users u
left join (select user_id, sum(distance) total_distance from rides group by user_id) d
on u.id = d.user_id
order by  nvl(d.total_distance,0) desc, u.name asc
```

## [607. 销售员](https://leetcode.cn/problems/sales-person/)

表: `SalesPerson`

```
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id 是该表的主键列(具有唯一值的列)。
该表的每一行都显示了销售人员的姓名和 ID ，以及他们的工资、佣金率和雇佣日期。
```

 

表: `Company`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id 是该表的主键列(具有唯一值的列)。
该表的每一行都表示公司的名称和 ID ，以及公司所在的城市。
```

 

表: `Orders`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id 是该表的主键列(具有唯一值的列)。
com_id 是 Company 表中 com_id 的外键（reference 列）。
sales_id 是来自销售员表 sales_id 的外键（reference 列）。
该表的每一行包含一个订单的信息。这包括公司的 ID 、销售人员的 ID 、订单日期和支付的金额。
```

 

编写解决方案，找出没有任何与名为 **“RED”** 的公司相关的订单的所有销售人员的姓名。

以 **任意顺序** 返回结果表。

返回结果格式如下所示。

 

**示例 1：**

```
输入：
SalesPerson 表:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+
Company 表:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+
Orders 表:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+
输出：
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+
解释：
根据表 orders 中的订单 '3' 和 '4' ，容易看出只有 'John' 和 'Pam' 两个销售员曾经向公司 'RED' 销售过。
所以我们需要输出表 salesperson 中所有其他人的名字。
```

```sql
/* Write your PL/SQL query statement below */

select name
from salesperson
where sales_id not in (
select o.sales_id
from orders o 
left join company c
on o.com_id = c.com_id
where c.name = 'RED')
```

## [1440. 计算布尔表达式的值](https://leetcode.cn/problems/evaluate-boolean-expression/)

表 `Variables`:

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
在 SQL 中，name 是该表主键.
该表包含了存储的变量及其对应的值.
```

 

表 `Expressions`:

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
在 SQL 中，(left_operand, operator, right_operand) 是该表主键.
该表包含了需要计算的布尔表达式.
operator 是枚举类型, 取值于('<', '>', '=')
left_operand 和 right_operand 的值保证存在于 Variables 表单中.
```

 

计算表 `Expressions` 中的布尔表达式。

返回的结果表 **无顺序要求** 。

结果格式如下例所示。

 

**示例 1：**

```
输入：
Variables 表:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+

Expressions 表:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+

输出:
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
解释：
如上所示, 你需要通过使用 Variables 表来找到 Expressions 表中的每一个布尔表达式的值.
```

```sql
/* Write your PL/SQL query statement below */

select l.left_operand ,l.operator, l.right_operand, 
case when l.operator = '>' and to_number(l.left_value) > to_number(v.value) then 'true' 
when l.operator = '<' and to_number(l.left_value) < to_number(v.value) then 'true' 
when l.operator = '=' and to_number(l.left_value) = to_number(v.value) then 'true' 
else 'false' end value
from 
(select e.left_operand, e.operator , e.right_operand, v.value left_value
from expressions e
left join variables v
on e.left_operand = v.name) l
left join variables v
on l.right_operand = v.name
```

## [1212. 查询球队积分](https://leetcode.cn/problems/team-scores-in-football-tournament/)

表: `Teams`

```
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+
team_id 是该表具有唯一值的列。
表中的每一行都代表一支独立足球队。
```

 

表: `Matches`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     | 
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+
match_id 是该表具有唯一值的列。
表中的每一行都代表一场已结束的比赛。
比赛的主客队分别由它们自己的 id 表示，他们的进球由 host_goals 和 guest_goals 分别表示。
```

 

你希望在所有比赛之后计算所有球队的比分。积分奖励方式如下:

- 如果球队赢了比赛(即比对手进更多的球)，就得 **3** 分。
- 如果双方打成平手(即，与对方得分相同)，则得 **1** 分。
- 如果球队输掉了比赛(例如，比对手少进球)，就 **不得分** 。

编写解决方案，以找出每个队的 `team_id`，`team_name` 和 `num_points`。

返回的结果根据 `num_points` **降序排序**，如果有两队积分相同，那么这两队按 `team_id` **升序排序**。

返回结果格式如下。

 

**示例 1:**

```
输入：
Teams table:
+-----------+--------------+
| team_id   | team_name    |
+-----------+--------------+
| 10        | Leetcode FC  |
| 20        | NewYork FC   |
| 30        | Atlanta FC   |
| 40        | Chicago FC   |
| 50        | Toronto FC   |
+-----------+--------------+
Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
+------------+--------------+---------------+-------------+--------------+
| 1          | 10           | 20            | 3           | 0            |
| 2          | 30           | 10            | 2           | 2            |
| 3          | 10           | 50            | 5           | 1            |
| 4          | 20           | 30            | 1           | 0            |
| 5          | 50           | 30            | 1           | 0            |
+------------+--------------+---------------+-------------+--------------+
输出：
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+
```



```sql
/* Write your PL/SQL query statement below */

select t.team_id, t.team_name, nvl(p.num_points,0) num_points
from teams t
left join
(select team_id, sum(points) num_points from
((select host_team team_id,
case when host_goals > guest_goals then 3
when host_goals = guest_goals then 1
else 0 end as points
from matches  )
union all
(select guest_team team_id,
case when guest_goals > host_goals then 3
when guest_goals = host_goals then 1
else 0 end as points
from matches))
group by team_id) p
on t.team_id = p.team_id
order by nvl(p.num_points,0) desc, t.team_id asc
```







# 聚合函数

## [620. 有趣的电影](https://leetcode.cn/problems/not-boring-movies/)

表：`cinema`

```
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id 是该表的主键(具有唯一值的列)。
每行包含有关电影名称、类型和评级的信息。
评级为 [0,10] 范围内的小数点后 2 位浮点数。
```

 

编写解决方案，找出所有影片描述为 **非** `boring` (不无聊) 的并且 **id 为奇数** 的影片。

返回结果按 `rating` **降序排列**。

结果格式如下示例。

 

**示例 1：**

```
输入：
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
输出：
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
解释：
我们有三部电影，它们的 id 是奇数:1、3 和 5。id = 3 的电影是 boring 的，所以我们不把它包括在答案中。
```

sql

### `mod()`求余数

```sql
/* Write your PL/SQL query statement below */

select id, movie, description, rating
from cinema
where description != 'boring' and mod(id,2) = 1
order by rating desc
```

pandas

### `sort_values(colunm, ascending = , inplace = )` dataframe 排序

```python
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    
    not_boring = cinema[cinema['description'] != 'boring']
    odd_id_not_boring = not_boring[not_boring['id']%2 == 1]
    odd_id_not_boring.sort_values('rating',ascending = False ,inplace=True)

    return odd_id_not_boring
```

## [1251. 平均售价](https://leetcode.cn/problems/average-selling-price/)

表：`Prices`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id，start_date，end_date) 是 prices 表的主键（具有唯一值的列的组合）。
prices 表的每一行表示的是某个产品在一段时期内的价格。
每个产品的对应时间段是不会重叠的，这也意味着同一个产品的价格时段不会出现交叉。
```

 

表：`UnitsSold`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
该表可能包含重复数据。
该表的每一行表示的是每种产品的出售日期，单位和产品 id。
```

 

编写解决方案以查找每种产品的平均售价。`average_price` 应该 **四舍五入到小数点后两位**。如果产品没有任何售出，则假设其平均售价为 0。

返回结果表 **无顺序要求** 。

结果格式如下例所示。

 

**示例 1：**

```
输入：
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
输出：
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
解释：
平均售价 = 产品总价 / 销售的产品数量。
产品 1 的平均售价 = ((100 * 5)+(15 * 20) )/ 115 = 6.96
产品 2 的平均售价 = ((200 * 15)+(30 * 30) )/ 230 = 16.96
```

sql-oracle

### `nvl(表达式1，表达式2)`

如果表达式1为空值，NVL返回值为表达式2的值，否则返回表达式1的值。该函数的目的是把一个空值（null）转换成一个实际的值。其表达式的值可以是数字型、字符型和日期型。但是表达式1和表达式2的数据类型必须为同一个类型。

### `nvl2(表达式1，表达式2，表达式3)`

如果表达式1为空，返回值为表达式3的值。如果表达式1不为空，返回值为表达式2的值。

```sql
/* Write your PL/SQL query statement below */

select p.product_id, nvl(round(sum(p.price*u.units)/sum(u.units),2),0) average_price
from Prices p
left join UnitsSold u
on (p.product_id = u.product_id) and (p.start_date <= u.purchase_date and  u.purchase_date<= p.end_date)
group by p.product_id
```

pandas

```python
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    # match purchase units to each record
    prices_sold = prices.merge(units_sold, how='left', on='product_id').query('start_date <= purchase_date <= end_date or purchase_date.isnull()')
    # calculate total sales for each record
    prices_sold['sold_price'] = prices_sold['price'] * prices_sold['units']
    # get sum of unites and sold price for each product
    product_unit_sum = prices_sold.groupby('product_id').agg(
        total_unit = pd.NamedAgg(column='units',aggfunc='sum'),
        total_price = pd.NamedAgg(column='sold_price', aggfunc = 'sum')
    ).reset_index()
    # calculate average price for each product
    product_unit_sum['average_price'] = (product_unit_sum['total_price']/product_unit_sum['total_unit']).round(2)
    # when a product doesn't sale any unit, then average price is 0 
    product_unit_sum['average_price'][product_unit_sum['total_unit']==0] = 0

    return product_unit_sum[['product_id','average_price']]
```

## [1075. 项目员工 I](https://leetcode.cn/problems/project-employees-i/)

项目表 `Project`： 

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
主键为 (project_id, employee_id)。
employee_id 是员工表 Employee 表的外键。
这张表的每一行表示 employee_id 的员工正在 project_id 的项目上工作。
```

 

员工表 `Employee`：

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
主键是 employee_id。数据保证 experience_years 非空。
这张表的每一行包含一个员工的信息。
```

 

请写一个 SQL 语句，查询每一个项目中员工的 **平均** 工作年限，**精确到小数点后两位**。

以 **任意** 顺序返回结果表。

查询结果的格式如下。

 

**示例 1:**

```
输入：
Project 表：
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee 表：
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

输出：
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
解释：第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
```

sql

```sql
/* Write your PL/SQL query statement below */

select p.project_id, round(avg(e.experience_years),2) average_years
from Project p
left join Employee e
on p.employee_id = e.employee_id
group by p.project_id
```

pandas

```python
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    result = project.merge(employee, how='left', on='employee_id').groupby('project_id')['experience_years'].mean().round(2).reset_index()
    result.rename(columns = {'experience_years':'average_years'}, inplace = True)

    return result
```

## [1633. 各赛事的用户注册率](https://leetcode.cn/problems/percentage-of-users-attended-a-contest/)

用户表： `Users`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id 是该表的主键(具有唯一值的列)。
该表中的每行包括用户 ID 和用户名。
```

 

注册表： `Register`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) 是该表的主键(具有唯一值的列的组合)。
该表中的每行包含用户的 ID 和他们注册的赛事。
```

 

编写解决方案统计出各赛事的用户注册百分率，保留两位小数。

返回的结果表按 `percentage` 的 **降序** 排序，若相同则按 `contest_id` 的 **升序** 排序。

返回结果如下示例所示。

 

**示例 1：**

```
输入：
Users 表：
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+

Register 表：
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
输出：
+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+
解释：
所有用户都注册了 208、209 和 210 赛事，因此这些赛事的注册率为 100% ，我们按 contest_id 的降序排序加入结果表中。
Alice 和 Alex 注册了 215 赛事，注册率为 ((2/3) * 100) = 66.67%
Bob 注册了 207 赛事，注册率为 ((1/3) * 100) = 33.33%
```

sql

```sql
/* Write your PL/SQL query statement below */

select r.contest_id, round((count(r.user_id)/u.user_count)*100,2) percentage
from (
    select count(user_id) user_count
    from Users
)u, Register r
group by r.contest_id, u.user_count
order by percentage desc, r.contest_id asc

```

pandas

### `sort_values()` 多列多条件排序

`sort_values(by = ['col_1','col_2'], ascending=[False,True], inplace=True)`

```python
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    # get user number
    user_num = users['user_id'].count()

    # get register number for each contest
    contest_register = register.groupby('contest_id')['user_id'].count().reset_index()

    # calculate percentage of registration rate
    contest_register['percentage'] = contest_register['user_id'].apply(lambda x : (x/user_num)*100).round(2)

    # sort result
    contest_register.sort_values(by = ['percentage','contest_id'], ascending=[False,True], inplace=True)

    return contest_register[['contest_id','percentage']]
```

## [1211. 查询结果的质量和占比](https://leetcode.cn/problems/queries-quality-and-percentage/)

`Queries` 表： 

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
此表可能有重复的行。
此表包含了一些从数据库中收集的查询信息。
“位置”（position）列的值为 1 到 500 。
“评分”（rating）列的值为 1 到 5 。评分小于 3 的查询被定义为质量很差的查询。
```

 

将查询结果的质量 `quality` 定义为：

> 各查询结果的评分与其位置之间比率的平均值。

将劣质查询百分比 `poor_query_percentage` 定义为：

> 评分小于 3 的查询结果占全部查询结果的百分比。

编写解决方案，找出每次的 `query_name` 、 `quality` 和 `poor_query_percentage`。

`quality` 和 `poor_query_percentage` 都应 **四舍五入到小数点后两位** 。

以 **任意顺序** 返回结果表。

结果格式如下所示：

 

**示例 1：**

```
输入：
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
输出：
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+
解释：
Dog 查询结果的质量为 ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33

Cat 查询结果的质量为 ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33
```

sql

### `sign()`判断值与0的关系

函数根据某个值是0、正数还是负数，分别返回0、1、-1 

### `decode(条件,值1,翻译值1,值2,翻译值2,...值n,翻译值n,缺省值)` 判断

该函数的含义如下：

```
IF 条件=值1 THEN
　　　　RETURN(翻译值1)
ELSIF 条件=值2 THEN
　　　　RETURN(翻译值2)
　　　　......
ELSIF 条件=值n THEN
　　　　RETURN(翻译值n)
ELSE
　　　　RETURN(缺省值)
END IF
decode(字段或字段的运算，值1，值2，值3）
```

### `over (partition by)`窗口函数

[【Oracle】OVER(PARTITION BY)函数用法 - ruiser - 博客园 (cnblogs.com)](https://www.cnblogs.com/ruiser/p/5687238.html)

[Oracle 理解 over() 和 partition by|极客教程 (geek-docs.com)](https://geek-docs.com/oracle/oracle-questions/192_oracle_trying_to_understand_over_and_partition_by.html)

提供分析函数，分析函数用于计算基于组的某种聚合值，它和聚合函数的不同之处是：对于每个组返回多行，而聚合函数对于每个组只返回一行。

over() 语句用于定义窗口或分析域，用于指定要应用窗口函数的行集。partition by 语句用于分组数据，并将窗口函数应用于每个分组内的数据。

Oracle

```sql
/* Write your PL/SQL query statement below */

select q.query_name, 
round(sum(q.rating/q.position)/count(q.query_name),2) quality, 
round((nvl(b.poor/count(q.query_name),0))*100,2) poor_query_percentage
from Queries q
left join (select query_name, count(query_name) poor from Queries where rating < 3 and query_name is not null group by query_name) b
on q.query_name = b.query_name
where q.query_name is not null
group by q.query_name,b.poor
```

```sql
select distinct(query_name),
round(avg(rating/position) over (partition by query_name) ,2) quality,
round(avg(decode(sign(rating-3),-1,1,0)) over (partition by query_name),4)*100 poor_query_percentage
from Queries
where query_name is not null
```

pandas

### `round()` 四舍五入注意事项

在Python中的round函数和NumPy中的np.round函数默认使用的是"四舍五入"规则。具体来说，当要舍入的数字是正好在5的一半上方时，它们将向最接近的偶数舍入。这种规则被称为"银行家舍入法"或"四舍六入五留双"，它旨在减少舍入误差的累积，从而提高精度。

"四舍六入五留双"规则的工作方式如下：

```
如果要舍入的数字小于5，它将被舍去。
如果要舍入的数字大于5，它将被进位。
如果要舍入的数字等于5，那么取决于它前面的数字是奇数还是偶数。如果前面的数字是奇数，那么向上进位；如果前面的数字是偶数，那么向下舍去。
舍去小数点后的数字（小于5）：
  5.1234 被舍入为 5.12
  3.456 被舍入为 3.45
  7.891 被舍入为 7.89
进位小数点后的数字（大于5）：
  6.789 被舍入为 6.79
  9.8765 被舍入为 9.88
  8.5 被舍入为 8.6
等于5并且前面数字是偶数（舍去）：
  2.5 被舍入为 2.0
  4.5 被舍入为 4.0
  10.5 被舍入为 10.0
等于5并且前面数字是奇数（进位）：
  3.5 被舍入为 4.0
  7.5 被舍入为 8.0
  11.5 被舍入为 12.0如果我们想要使用不同的舍入规则，需要通过指定精度来使用decimal模块中的ROUND_HALF_UP等舍入模式，或者自定义舍入逻辑。
```

[15. 浮点算术：争议和限制 — Python 3.12.6 文档](https://docs.python.org/zh-cn/3/tutorial/floatingpoint.html#tut-fp-issues)

[decimal --- 十进制定点和浮点算术 — Python 3.12.6 文档](https://docs.python.org/zh-cn/3/library/decimal.html#module-decimal)

round函数使用是四舍六入五留双，ROUND_HALF_UP，才是通常意义的四舍五入

```python
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

def my_round(x):
    return Decimal(x).quantize(Decimal('.00'), rounding=ROUND_HALF_UP)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    grouped = queries.groupby('query_name').agg(
        quality=('quality', lambda x: my_round(x.mean())),
        poor_query_percentage=('rating', lambda x: my_round((x < 3).sum() / len(x) * 100))
    ).reset_index()

    return grouped
```

## [1193. 每月交易 I](https://leetcode.cn/problems/monthly-transactions-i/)

表：`Transactions`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id 是这个表的主键。
该表包含有关传入事务的信息。
state 列类型为 ["approved", "declined"] 之一。
```

 

编写一个 sql 查询来查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

**示例 1:**

```
输入：
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
输出：
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
```

sql

```sql
/* Write your PL/SQL query statement below */
select distinct to_char(trans_date,'yyyy-mm') month, country, 
count(id) trans_count,
sum(decode(state,'approved',1,0)) approved_count,
sum(amount) trans_total_amount,
sum(decode(state,'approved',amount,0)) approved_total_amount

from Transactions
group by to_char(trans_date,'yyyy-mm'), country
```

pandas

### `pd.groupby()`如果key值中有null，该行会被忽略

在使用`groupby()`的时候，要确保key不存在空值，可以先替换空值再进行聚合。下面是遇到的案例

输出

`grouped = transactions.groupby(['month','country'])`

```
输入
Transactions =
| id  | country | state    | amount | trans_date |
| --- | ------- | -------- | ------ | ---------- |
| 121 | US      | approved | 1000   | 2018-12-18 |
| 122 | US      | declined | 2000   | 2018-12-19 |
| 123 | US      | approved | 2000   | 2019-01-01 |
| 124 | null    | approved | 2000   | 2019-01-07 |

输出
| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
| ------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |

预期结果
| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
| ------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01 | null    | 1           | 1              | 2000               | 2000                  |
```



```python
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    # define expression to calculate count and sum amount when state is approved
    def approved_count(x):
        return sum(x == 'approved')
    def approved_amount(x):
        return sum(x[transactions['state'] == 'approved'])
    
    # set value to 999, when value is null in country column
    transactions['country'] = transactions['country'].fillna(999)
    # transform date to year-month format
    transactions['month'] = transactions['trans_date'].map(lambda x :x.strftime('%Y-%m'))
    # define group conditions
    grouped = transactions.groupby(['month','country'])
    trans_amount = grouped.agg(
        {
            'id':[('trans_count', 'count')],
            'state':[('approved_count', approved_count)],
            'amount':[('trans_total_amount','sum'), ('approved_total_amount', approved_amount)]
        }
    ).reset_index()
    # rename column name
    trans_amount.columns = ['month','country','trans_count','approved_count','trans_total_amount','approved_total_amount']
    # replace null cell to None
    trans_amount['country'][trans_amount['country']==999] = None

    return trans_amount
```

## [1174. 即时食物配送 II](https://leetcode.cn/problems/immediate-food-delivery-ii/)

配送表: `Delivery`

```
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id 是该表中具有唯一值的列。
该表保存着顾客的食物配送信息，顾客在某个日期下了订单，并指定了一个期望的配送日期（和下单日期相同或者在那之后）。
```

 

如果顾客期望的配送日期和下单日期相同，则该订单称为 「**即时订单**」，否则称为「**计划订单**」。

「**首次订单**」是顾客最早创建的订单。我们保证一个顾客只会有一个「首次订单」。

编写解决方案以获取即时订单在所有用户的首次订单中的比例。**保留两位小数。**

结果示例如下所示：

 

**示例 1：**

```
输入：
Delivery 表：
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
输出：
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
解释：
1 号顾客的 1 号订单是首次订单，并且是计划订单。
2 号顾客的 2 号订单是首次订单，并且是即时订单。
3 号顾客的 5 号订单是首次订单，并且是计划订单。
4 号顾客的 7 号订单是首次订单，并且是即时订单。
因此，一半顾客的首次订单是即时的。
```

sql

```sql
/* Write your PL/SQL query statement below */

select round(100*sum(d.first_immediate)/sum(decode(d.rank,1,1,0)),2) immediate_percentage

from (
    select delivery_id, customer_id, order_date,customer_pref_delivery_date,
    rank() over (partition by customer_id order by order_date) as rank,
    case when (order_date=customer_pref_delivery_date and rank() over (partition by customer_id order by order_date) =1) then 1 else 0 end first_immediate
    from Delivery
    ) d

```

pandas

```python
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    # fetch delivery id for immediate order and first order
    immediate_id = list(delivery['delivery_id'][delivery['order_date'] == delivery['customer_pref_delivery_date']])
    first_order = delivery.groupby('customer_id')['order_date'].min().reset_index()
    first_order_id = list(first_order.merge(delivery, how='left', on=['customer_id','order_date'])['delivery_id'])
    
    # calculate how many order are both first and immediate order, and get number of first order
    first_order_count = len(first_order_id)
    first_immediate = 0
    for i in immediate_id:
        if i in first_order_id:
            first_immediate += 1
    
    # get immediate percentage and transform it to a DataFrame
    immediate_percentage  = [round(100*first_immediate/first_order_count,2)]
    pd_first_emmidiate = pd.DataFrame(immediate_percentage, columns=['immediate_percentage'])

    return pd_first_emmidiate
```



## [550. 游戏玩法分析 IV](https://leetcode.cn/problems/game-play-analysis-iv/)

Table: `Activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
（player_id，event_date）是此表的主键（具有唯一值的列的组合）。
这张表显示了某些游戏的玩家的活动情况。
每一行是一个玩家的记录，他在某一天使用某个设备注销之前登录并玩了很多游戏（可能是 0）。
```

 

编写解决方案，报告在首次登录的第二天再次登录的玩家的 **比率**，**四舍五入到小数点后两位**。换句话说，你需要计算从首次登录日期开始至少连续两天登录的玩家的数量，然后除以玩家总数。

结果格式如下所示：

 

**示例 1：**

```
输入：
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
输出：
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
解释：
只有 ID 为 1 的玩家在第一天登录后才重新登录，所以答案是 1/3 = 0.33
```

```sql
/* Write your PL/SQL query statement below */

select 
round(count(a.login_rank)/count(distinct r.player_id),2) fraction
from 
(select player_id,event_date,
    rank() over (partition by player_id order by event_date) login_rank
    from Activity) r
left join (select player_id,event_date,
    rank() over (partition by player_id order by event_date) login_rank
    from Activity)a
on a.player_id = r.player_id and r.login_rank=1 and a.login_rank=2 and to_date(r.event_date)+1 = a.event_date 
```

pandas

### `pd.DateOffset()` 时间加减操作



```python
import pandas as pd
import datetime

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    # get first login day and supposed continue login day for each player
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login['next_day'] = first_login['event_date'] + datetime.timedelta(days=1)

    # compare with activity to figue out if the player continue login
    continue_login = first_login.merge(activity, how='left', left_on=['player_id','next_day'], right_on=['player_id','event_date'])

    # count total player number and continue login number
    player_num = first_login['player_id'].count()
    continue_login_num = continue_login['games_played'].count()
    
    # calculate fraction and store it into a list. Then create a daraframe to show result
    fraction = [round(continue_login_num/player_num,2)]
    fraction_pd = pd.DataFrame(fraction, columns=['fraction'])

    return fraction_pd
```

```python
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    # get first login day and supposed continue login day for each player
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login['next_day'] = first_login['event_date'] + pd.DateOffset(days=1)

    # compare with activity to figue out if the player continue login
    continue_login = first_login.merge(activity, how='left', left_on=['player_id','next_day'], right_on=['player_id','event_date'])

    # count total player number and continue login number
    player_num = first_login['player_id'].count()
    continue_login_num = continue_login['games_played'].count()
    
    # calculate fraction and store it into a list. Then create a daraframe to show result
    fraction = [round(continue_login_num/player_num,2)]
    fraction_pd = pd.DataFrame(fraction, columns=['fraction'])

    return fraction_pd
```

### `transform()` python的窗口函数



```python
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    # using groupby and transform to get each player's second time login date
    second_login = activity.groupby('player_id')['event_date'].transform(lambda x: x.min() + pd.DateOffset(days=1))
    
    # get row num of second login equal actual date
    matching_rows_count = (second_login == activity['event_date']).sum()

    # calculate fraction
    fraction = round(matching_rows_count / activity['player_id'].nunique(), 2)

    # creat dataframe
    fraction_df = pd.DataFrame({'fraction': [fraction]})

    return fraction_df
```

## [1890. 2020年最后一次登录](https://leetcode.cn/problems/the-latest-login-in-2020/)

表: `Logins`

```
+----------------+----------+
| 列名           | 类型      |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
(user_id, time_stamp) 是这个表的主键(具有唯一值的列的组合)。
每一行包含的信息是user_id 这个用户的登录时间。
```

 

编写解决方案以获取在 `2020` 年登录过的所有用户的本年度 **最后一次** 登录时间。结果集 **不** 包含 `2020` 年没有登录过的用户。

返回的结果集可以按 **任意顺序** 排列。

返回结果格式如下例。

 

**示例 1:**

```
输入：
Logins 表:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+
输出：
+---------+---------------------+
| user_id | last_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
+---------+---------------------+
解释：
6号用户登录了3次，但是在2020年仅有一次，所以结果集应包含此次登录。
8号用户在2020年登录了2次，一次在2月，一次在12月，所以，结果集应该包含12月的这次登录。
2号用户登录了2次，但是在2020年仅有一次，所以结果集应包含此次登录。
14号用户在2020年没有登录，所以结果集不应包含。
```

```sql
select user_id, max(time_stamp) last_stamp
from logins
where user_id in (select user_id from logins where to_char(time_stamp,'yyyy') = '2020') and to_char(time_stamp,'yyyy') = '2020'
group by user_id
```

## [511. 游戏玩法分析 I](https://leetcode.cn/problems/game-play-analysis-i/)

活动表 `Activity`：

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
在 SQL 中，表的主键是 (player_id, event_date)。
这张表展示了一些游戏玩家在游戏平台上的行为活动。
每行数据记录了一名玩家在退出平台之前，当天使用同一台设备登录平台后打开的游戏的数目（可能是 0 个）。
```

 

查询每位玩家 **第一次登录平台的日期**。

查询结果的格式如下所示：

```
Activity 表：
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result 表：
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```

```sql
/* Write your PL/SQL query statement below */

select player_id, to_char(min(event_date),'yyyy-mm-dd') first_login
from activity
group by player_id
```

## [1571. 仓库经理](https://leetcode.cn/problems/warehouse-manager/)

表: `Warehouse`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| name         | varchar |
| product_id   | int     |
| units        | int     |
+--------------+---------+
(name, product_id) 是该表主键(具有唯一值的列的组合).
该表的行包含了每个仓库的所有商品信息.
```

 

表: `Products`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| Width         | int     |
| Length        | int     |
| Height        | int     |
+---------------+---------+
product_id 是该表主键(具有唯一值的列).
该表的行包含了每件商品以英尺为单位的尺寸(宽度, 长度和高度)信息.
```

 

编写解决方案报告每个仓库的存货量是多少立方英尺。

返回结果没有顺序要求。

返回结果格式如下例所示。

 

**示例 1:**

```
输入：
Warehouse 表:
+------------+--------------+-------------+
| name       | product_id   | units       |
+------------+--------------+-------------+
| LCHouse1   | 1            | 1           |
| LCHouse1   | 2            | 10          |
| LCHouse1   | 3            | 5           |
| LCHouse2   | 1            | 2           |
| LCHouse2   | 2            | 2           |
| LCHouse3   | 4            | 1           |
+------------+--------------+-------------+
Products 表:
+------------+--------------+------------+----------+-----------+
| product_id | product_name | Width      | Length   | Height    |
+------------+--------------+------------+----------+-----------+
| 1          | LC-TV        | 5          | 50       | 40        |
| 2          | LC-KeyChain  | 5          | 5        | 5         |
| 3          | LC-Phone     | 2          | 10       | 10        |
| 4          | LC-T-Shirt   | 4          | 10       | 20        |
+------------+--------------+------------+----------+-----------+
输出：
+----------------+------------+
| warehouse_name | volume     | 
+----------------+------------+
| LCHouse1       | 12250      | 
| LCHouse2       | 20250      |
| LCHouse3       | 800        |
+----------------+------------+
解释：
Id为1的商品(LC-TV)的存货量为 5x50x40 = 10000
Id为2的商品(LC-KeyChain)的存货量为 5x5x5 = 125 
Id为3的商品(LC-Phone)的存货量为 2x10x10 = 200
Id为4的商品(LC-T-Shirt)的存货量为 4x10x20 = 800
仓库LCHouse1: 1个单位的LC-TV + 10个单位的LC-KeyChain + 5个单位的LC-Phone.
          总存货量为: 1*10000 + 10*125  + 5*200 = 12250 立方英尺
仓库LCHouse2: 2个单位的LC-TV + 2个单位的LC-KeyChain.
          总存货量为: 2*10000 + 2*125 = 20250 立方英尺
仓库LCHouse3: 1个单位的LC-T-Shirt.
          总存货量为: 1*800 = 800 立方英尺.
```

```sql
/* Write your PL/SQL query statement below */

select w.name warehouse_name, sum(p.width*p.length*p.height*w.units) volume
from warehouse w
left join products p
on w.product_id=p.product_id
group by w.name
```

## [586. 订单最多的客户](https://leetcode.cn/problems/customer-placing-the-largest-number-of-orders/)

表: `Orders`

```
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
在 SQL 中，Order_number是该表的主键。
此表包含关于订单ID和客户ID的信息。
```

 

查找下了 **最多订单** 的客户的 `customer_number` 。

测试用例生成后， **恰好有一个客户** 比任何其他客户下了更多的订单。

查询结果格式如下所示。

 

**示例 1:**

```
输入: 
Orders 表:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
输出: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
解释: 
customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单。
所以结果是该顾客的 customer_number ，也就是 3 。
```

**进阶：** 如果有多位顾客订单数并列最多，你能找到他们所有的 `customer_number` 吗？

```sql
/* Write your PL/SQL query statement below */

select customer_number
from(
select customer_number
from orders
group by customer_number
order by  count(order_number) desc )
where rownum = 1
```

## [1741. 查找每个员工花费的总时间](https://leetcode.cn/problems/find-total-time-spent-by-each-employee/)

表: `Employees`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
在 SQL 中，(emp_id, event_day, in_time) 是这个表的主键。
该表显示了员工在办公室的出入情况。
event_day 是此事件发生的日期，in_time 是员工进入办公室的时间，而 out_time 是他们离开办公室的时间。
in_time 和 out_time 的取值在1到1440之间。
题目保证同一天没有两个事件在时间上是相交的，并且保证 in_time 小于 out_time。
```

 

计算每位员工每天在办公室花费的总时间（以分钟为单位）。 请注意，在一天之内，同一员工是可以多次进入和离开办公室的。 在办公室里一次进出所花费的时间为out_time 减去 in_time。

返回结果表单的顺序无要求。
查询结果的格式如下：

 

**示例 1：**

```
输入：
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
输出：
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
解释：
雇员 1 有三次进出: 有两次发生在 2020-11-28 花费的时间为 (32 - 4) + (200 - 55) = 173, 有一次发生在 2020-12-03 花费的时间为 (42 - 1) = 41。
雇员 2 有两次进出: 有一次发生在 2020-11-28 花费的时间为 (33 - 3) = 30,  有一次发生在 2020-12-09 花费的时间为 (74 - 47) = 27。
```

```sql
/* Write your PL/SQL query statement below */

select to_char(event_day,'yyyy-mm-dd') day, emp_id, sum(out_time-in_time) total_time
from employees
group by event_day, emp_id
```

## [1173. 即时食物配送 I](https://leetcode.cn/problems/immediate-food-delivery-i/)

配送表: `Delivery`

```
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id 是表的主键(具有唯一值的列)。
该表保存着顾客的食物配送信息，顾客在某个日期下了订单，并指定了一个期望的配送日期（和下单日期相同或者在那之后）。
```

 

如果顾客期望的配送日期和下单日期相同，则该订单称为 「即时订单」，否则称为「计划订单」。

编写解决方案统计即时订单所占的百分比， **保留两位小数。**

返回结果如下所示。

 

**示例 1:**

```
输入：
Delivery 表:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
输出：
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
解释：2 和 3 号订单为即时订单，其他的为计划订单。
```

```sql
/* Write your PL/SQL query statement below */

select round(sum(immediate_order)/count(delivery_id)*100,2) immediate_percentage
from (select delivery_id, 
case when order_date = customer_pref_delivery_date then 1 else 0 end immediate_order
from delivery)

```

## [1445. 苹果和桔子](https://leetcode.cn/problems/apples-oranges/)

表: `Sales`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    | 
| sold_num      | int     | 
+---------------+---------+
(sale_date, fruit) 是该表主键(具有唯一值的列的组合)。
该表包含了每一天中"苹果" 和 "桔子"的销售情况。
```

 

编写解决方案报告每一天 **苹果** 和 **桔子** 销售的数目的差异.

返回的结果表, 按照格式为 ('YYYY-MM-DD') 的 `sale_date` 排序.

返回结果表如下例所示:

 

**示例 1：**

```
输入：
Sales 表:
+------------+------------+-------------+
| sale_date  | fruit      | sold_num    |
+------------+------------+-------------+
| 2020-05-01 | apples     | 10          |
| 2020-05-01 | oranges    | 8           |
| 2020-05-02 | apples     | 15          |
| 2020-05-02 | oranges    | 15          |
| 2020-05-03 | apples     | 20          |
| 2020-05-03 | oranges    | 0           |
| 2020-05-04 | apples     | 15          |
| 2020-05-04 | oranges    | 16          |
+------------+------------+-------------+
输出：
+------------+--------------+
| sale_date  | diff         |
+------------+--------------+
| 2020-05-01 | 2            |
| 2020-05-02 | 0            |
| 2020-05-03 | 20           |
| 2020-05-04 | -1           |
+------------+--------------+
解释：
在 2020-05-01, 卖了 10 个苹果 和 8 个桔子 (差异为 10 - 8 = 2).
在 2020-05-02, 卖了 15 个苹果 和 15 个桔子 (差异为 15 - 15 = 0).
在 2020-05-03, 卖了 20 个苹果 和 0 个桔子 (差异为 20 - 0 = 20).
在 2020-05-04, 卖了 15 个苹果 和 16 个桔子 (差异为 15 - 16 = -1).
```

```sql
/* Write your PL/SQL query statement below */

select to_char(a.sale_date,'yyyy-mm-dd') sale_date, a.apple-o.orange diff
from
(select sale_date,sold_num apple
from
(select sale_date,fruit,sold_num, rownum rn
from sales
order by sale_date, fruit asc)
where mod(rn,2) = 1)a
,
(select sale_date,sold_num orange
from
(select sale_date,fruit,sold_num, rownum rn
from sales
order by sale_date, fruit asc)
where mod(rn,2) = 0)o
where a.SALE_DATE=o.SALE_DATE
```

## [1699. 两人之间的通话次数](https://leetcode.cn/problems/number-of-calls-between-two-persons/)

表： `Calls`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
该表没有主键(具有唯一值的列)，它可能包含重复项。
该表包含 from_id 与 to_id 间的一次电话的时长。
from_id != to_id
```

 

编写解决方案，统计每一对用户 `(person1, person2)` 之间的通话次数和通话总时长，其中 `person1 < person2` 。

以 **任意顺序** 返回结果表。

返回结果格式如下示例所示。

 

**示例 1：**

```
输入：
Calls 表：
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
输出：
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+
解释：
用户 1 和 2 打过 2 次电话，总时长为 70 (59 + 11)。
用户 1 和 3 打过 1 次电话，总时长为 20。
用户 3 和 4 打过 4 次电话，总时长为 999 (100 + 200 + 200 + 499)。
```

```sql
/* Write your PL/SQL query statement below */

select person1, person2, count(1) call_count, sum(duration) total_duration
from(
select
case when from_id > to_id then to_id else from_id end as person1,
case when from_id > to_id then from_id else to_id end as person2,
duration
from calls
)
group by person1, person2
```

# 排序和分组

## [2356. 每位教师所教授的科目种类的数量](https://leetcode.cn/problems/number-of-unique-subjects-taught-by-each-teacher/)

表: `Teacher`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
在 SQL 中，(subject_id, dept_id) 是该表的主键。
该表中的每一行都表示带有 teacher_id 的教师在系 dept_id 中教授科目 subject_id。
```

 

查询每位老师在大学里教授的科目种类的数量。

以 **任意顺序** 返回结果表。

查询结果格式示例如下。

 

**示例 1:**

```
输入: 
Teacher 表:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
输出:  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
解释: 
教师 1:
  - 他在 3、4 系教科目 2。
  - 他在 3 系教科目 3。
教师 2:
  - 他在 1 系教科目 1。
  - 他在 1 系教科目 2。
  - 他在 1 系教科目 3。
  - 他在 1 系教科目 4。
```

sql

```sql
/* Write your PL/SQL query statement below */

select teacher_id, count(distinct subject_id) cnt
from teacher
group by teacher_id
```

pandas

### `unique()`相当于`distinct()`

```python
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    
    # distinct subject_id of each teacher 
    teacher_unique_subject= teacher.groupby('teacher_id')['subject_id'].unique().reset_index()
    # count subject number for each teacher
    teacher_unique_subject['cnt'] = teacher_unique_subject['subject_id'].apply(lambda x: len(x))

    return teacher_unique_subject[['teacher_id','cnt']]
```

## [1141. 查询近30天活跃用户数](https://leetcode.cn/problems/user-activity-for-the-past-30-days-i/)

表：`Activity`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
该表没有包含重复数据。
activity_type 列是 ENUM(category) 类型， 从 ('open_session'， 'end_session'， 'scroll_down'， 'send_message') 取值。
该表记录社交媒体网站的用户活动。
注意，每个会话只属于一个用户。
```

 

编写解决方案，统计截至 `2019-07-27`（包含2019-07-27），近 `30` 天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。

以 **任意顺序** 返回结果表。

结果示例如下。

 

**示例 1:**

```
输入：
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
输出：
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ 
解释：注意非活跃用户的记录不需要展示。
```

sql

```sql
/* Write your PL/SQL query statement below */

select to_char(activity_date,'yyyy-mm-dd') day, count(distinct user_id) active_users
from activity
where  (to_date('2019-07-27') -30) <activity_date and activity_date<= to_date('2019-07-27')
group by activity_date
order by day asc;
```

pandas

### f-string in query

不要用`{}`来引入变量，要用`@`.

Using `{}` in a query string without proper context doesn't work because `pandas`' `query` method doesn't automatically evaluate variables like an f-string does. Here's a breakdown:

1. **Using `{}`**: When you include `{}` in a string, Python interprets it as a placeholder for the `.format()` method or f-string substitution. However, `pandas`' `query` method doesn’t automatically replace `{}` with variable values.
2. **Using `@`**: The `@` symbol is specifically used in `pandas`' `query` method to indicate that you want to reference a variable from the local namespace. This tells `pandas` to treat what follows the `@` as a variable, allowing it to evaluate the expression correctly.



```python
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    
    # get start day
    start_date = pd.to_datetime('2019-07-27') + pd.DateOffset(days=-30)
    start_date = start_date.strftime('%Y-%m-%d')

    data_set = activity.query(f'@start_date < activity_date <= "2019-07-27"').groupby('activity_date')['user_id'].unique().reset_index()
    data_set['active_users'] = data_set['user_id'].apply(lambda x:len(x))

    # rename column
    data_set.rename(columns={'activity_date':'day'}, inplace=True)

    return data_set[['day','active_users']]
```

## [1084. 销售分析III](https://leetcode.cn/problems/sales-analysis-iii/)

表： `Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id 是该表的主键（具有唯一值的列）。
该表的每一行显示每个产品的名称和价格。
```

表：`Sales`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+------ ------+---------+
这个表可能有重复的行。
product_id 是 Product 表的外键（reference 列）。
该表的每一行包含关于一个销售的一些信息。
```

 

编写解决方案，报告 `2019年春季` 才售出的产品。即 **仅** 在 `**2019-01-01**` （含）至 `**2019-03-31**` （含）之间出售的商品。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1:**

```
输入：
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
输出：
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
解释:
id 为 1 的产品仅在 2019 年春季销售。
id 为 2 的产品在 2019 年春季销售，但也在 2019 年春季之后销售。
id 为 3 的产品在 2019 年春季之后销售。
我们只返回 id 为 1 的产品，因为它是 2019 年春季才销售的产品。
```

sql

```sql
select product_id, product_name
from product
where  product_id in (
    select product_id from Sales 
    group by product_id
    having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31') 
```

pandas

```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    date_cal = sales.groupby('product_id').agg(
        {'sale_date':[('min_date','min'),('max_date','max')]}
    ).reset_index()

    spring_sale = date_cal[(date_cal['sale_date','min_date']>='2019-01-01') & (date_cal['sale_date','max_date'] <= '2019-03-31')]

    product_id_pd = pd.DataFrame(spring_sale['product_id'], columns=['product_id'])

    spring_product_info = product_id_pd.merge(product, how='left', on='product_id')

    return spring_product_info[['product_id','product_name']]
```

## [596. 超过 5 名学生的课](https://leetcode.cn/problems/classes-more-than-5-students/)

表: `Courses`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class)是该表的主键（不同值的列的组合）。
该表的每一行表示学生的名字和他们注册的班级。
```

 

查询 **至少有 5 个学生** 的所有班级。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

**示例 1:**

```
输入: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
输出: 
+---------+ 
| class   | 
+---------+ 
| Math    | 
+---------+
解释: 
-数学课有 6 个学生，所以我们包括它。
-英语课有 1 名学生，所以我们不包括它。
-生物课有 1 名学生，所以我们不包括它。
-计算机课有 1 个学生，所以我们不包括它。
```

SQL

```sql
/* Write your PL/SQL query statement below */

select class
from Courses
group by class
having count(student) >= 5
```

## [1729. 求关注者的数量](https://leetcode.cn/problems/find-followers-count/)

```
表： Followers

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) 是这个表的主键（具有唯一值的列的组合）。
该表包含一个关注关系中关注者和用户的编号，其中关注者关注用户。
 

编写解决方案，对于每一个用户，返回该用户的关注者数量。

按 user_id 的顺序返回结果表。

查询结果的格式如下示例所示。

 

示例 1：

输入：
Followers 表：
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
输出：
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
解释：
0 的关注者有 {1}
1 的关注者有 {0}
2 的关注者有 {0,1}
```

```sql
/* Write your PL/SQL query statement below */

select user_id, count(follower_id) followers_count
from Followers
group by user_id
order by user_id
```

## [619. 只出现一次的最大数字](https://leetcode.cn/problems/biggest-single-number/)

```
MyNumbers 表：

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
该表可能包含重复项（换句话说，在SQL中，该表没有主键）。
这张表的每一行都含有一个整数。
 

单一数字 是在 MyNumbers 表中只出现一次的数字。

找出最大的 单一数字 。如果不存在 单一数字 ，则返回 null 。

查询结果如下例所示。

 

示例 1：

输入：
MyNumbers 表：
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
输出：
+-----+
| num |
+-----+
| 6   |
+-----+
解释：单一数字有 1、4、5 和 6 。
6 是最大的单一数字，返回 6 。
示例 2：

输入：
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
输出：
+------+
| num  |
+------+
| null |
+------+
解释：输入的表中不存在单一数字，所以返回 null 。
```

```sql
/* Write your PL/SQL query statement below */

select max(max(num)) num
from mynumbers
group by num
having count(num)=1
```

## [1045. 买下所有产品的客户](https://leetcode.cn/problems/customers-who-bought-all-products/)

```
Customer 表：

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
该表可能包含重复的行。
customer_id 不为 NULL。
product_key 是 Product 表的外键(reference 列)。
Product 表：

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key 是这张表的主键（具有唯一值的列）。
 

编写解决方案，报告 Customer 表中购买了 Product 表中所有产品的客户的 id。

返回结果表 无顺序要求 。

返回结果格式如下所示。

 

示例 1：

输入：
Customer 表：
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product 表：
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
输出：
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
解释：
购买了所有产品（5 和 6）的客户的 id 是 1 和 3 。
```

```sql
/* Write your PL/SQL query statement below */

select c.customer_id
from customer c, (select count(product_key) k from product) p
group by c.customer_id, p.k
having count(distinct c.product_key)=p.k

```

# 高级查询和连接

## [1731. 每位经理的下属员工数量](https://leetcode.cn/problems/the-number-of-employees-which-report-to-each-employee/)

表：`Employees`

```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id 是这个表中具有不同值的列。
该表包含员工以及需要听取他们汇报的上级经理的 ID 的信息。 有些员工不需要向任何人汇报（reports_to 为空）。
```

 

对于此问题，我们将至少有一个其他员工需要向他汇报的员工，视为一个经理。

编写一个解决方案来返回需要听取汇报的所有经理的 ID、名称、直接向该经理汇报的员工人数，以及这些员工的平均年龄，其中该平均年龄需要四舍五入到最接近的整数。

返回的结果集需要按照 `employee_id` 进行排序。

结果的格式如下：

 

**示例 1:**

```
输入：
Employees 表：
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
输出：
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
解释：
Hercy 有两个需要向他汇报的员工, 他们是 Alice and Bob. 他们的平均年龄是 (41+36)/2 = 38.5, 四舍五入的结果是 39.
```

**示例 2:**

```
输入： 
Employees 表：
+-------------+---------+------------+-----+ 
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+ 
输出： 
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
```

```sql
/* Write your PL/SQL query statement below */

select distinct m.reports_to employee_id, e.name , count(m.employee_id) reports_count, round(avg(m.age),0) average_age
from employees m
left join employees e
on m.reports_to = e.employee_id
where m.reports_to is not null
group by m.reports_to, e.name
order by m.reports_to asc
```

## [1789. 员工的直属部门](https://leetcode.cn/problems/primary-department-for-each-employee/)

```
表：Employee

+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
这张表的主键为 employee_id, department_id (具有唯一值的列的组合)
employee_id 是员工的ID
department_id 是部门的ID，表示员工与该部门有关系
primary_flag 是一个枚举类型，值分别为('Y', 'N'). 如果值为'Y',表示该部门是员工的直属部门。 如果值是'N',则否
 

一个员工可以属于多个部门。当一个员工加入超过一个部门的时候，他需要决定哪个部门是他的直属部门。请注意，当员工只加入一个部门的时候，那这个部门将默认为他的直属部门，虽然表记录的值为'N'.

请编写解决方案，查出员工所属的直属部门。

返回结果 没有顺序要求 。

返回结果格式如下例子所示：

 

示例 1：

输入：
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
输出：
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
解释：
- 员工 1 的直属部门是 1
- 员工 2 的直属部门是 1
- 员工 3 的直属部门是 3
- 员工 4 的直属部门是 3
```

```sql
/* Write your PL/SQL query statement below */

select employee_id, department_id
from employee
where  primary_flag = 'Y' 
union 

select a.employee_id, e.department_id
from
(select employee_id
from employee
group by employee_id
having count(department_id) = 1) a, employee e
where a.employee_id = e.employee_id
```

## [610. 判断三角形](https://leetcode.cn/problems/triangle-judgement/)

```
表: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
在 SQL 中，(x, y, z)是该表的主键列。
该表的每一行包含三个线段的长度。
 

对每三个线段报告它们是否可以形成一个三角形。

以 任意顺序 返回结果表。

查询结果格式如下所示。

 

示例 1:

输入: 
Triangle 表:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
输出: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```

```sql
/* Write your PL/SQL query statement below */

select x,y,z,
case 
when (x+y)>z and (x+z)>y and (y+z)>x then 'Yes'
else 'No'
end as triangle
from Triangle
```

## [180. 连续出现的数字](https://leetcode.cn/problems/consecutive-numbers/)

```
表：Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
在 SQL 中，id 是该表的主键。
id 是一个自增列。
 

找出所有至少连续出现三次的数字。

返回的结果表中的数据可以按 任意顺序 排列。

结果格式如下面的例子所示：

 

示例 1:

输入：
Logs 表：
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
输出：
Result 表：
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
解释：1 是唯一连续出现至少三次的数字。
```

```sql
/* Write your PL/SQL query statement below */


select distinct a.num ConsecutiveNums 
from
(
select id, num,
row_number() over (order by id) rank1 ,
row_number() over (partition by num order by id) rank2,
row_number() over (order by id) - row_number() over (partition by num order by id) subrank
    
from logs
)a

group by  a.num, a.subrank
having count(id) >= 3
```

## [1164. 指定日期的产品价格](https://leetcode.cn/problems/product-price-at-a-given-date/)

```
产品数据表: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) 是此表的主键（具有唯一值的列组合）。
这张表的每一行分别记录了 某产品 在某个日期 更改后 的新价格。
 

编写一个解决方案，找出在 2019-08-16 时全部产品的价格，假设所有产品在修改前的价格都是 10 。

以 任意顺序 返回结果表。

结果格式如下例所示。

 

示例 1:

输入：
Products 表:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
输出：
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
```

```sql
/* Write your PL/SQL query statement below */

select p.product_id, p.new_price price
from products p,
(select product_id,max(change_date) max_date
from products
where change_date <= '2019-08-16'  
group by product_id) m
where p.product_id=m.product_id and p.change_date=m.max_date
union
(select product_id, 10 price
from products
group by product_id
having min(change_date) > '2019-08-16')
```

## [1204. 最后一个能进入巴士的人](https://leetcode.cn/problems/last-person-to-fit-in-the-bus/)

```
表: Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id 是这个表具有唯一值的列。
该表展示了所有候车乘客的信息。
表中 person_id 和 turn 列将包含从 1 到 n 的所有数字，其中 n 是表中的行数。
turn 决定了候车乘客上巴士的顺序，其中 turn=1 表示第一个上巴士，turn=n 表示最后一个上巴士。
weight 表示候车乘客的体重，以千克为单位。
 

有一队乘客在等着上巴士。然而，巴士有1000  千克 的重量限制，所以其中一部分乘客可能无法上巴士。

编写解决方案找出 最后一个 上巴士且不超过重量限制的乘客，并报告 person_name 。题目测试用例确保顺位第一的人可以上巴士且不会超重。

返回结果格式如下所示。

 

示例 1：

输入：
Queue 表
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+
输出：
+-------------+
| person_name |
+-------------+
| John Cena   |
+-------------+
解释：
为了简化，Queue 表按 turn 列由小到大排序。
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (最后一个上巴士)
| 4    | 2  | Marie     | 200    | 1200         | (无法上巴士)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+
```

```sql
/* Write your PL/SQL query statement below */

select t.person_name
from(
select person_id, person_name, weight, turn,
sum(weight) over (order by turn rows between unbounded preceding and current row ) total_weight
from queue
order by total_weight desc) t
where t.total_weight <= 1000 and rownum = 1
```

## [1907. 按分类统计薪水](https://leetcode.cn/problems/count-salary-categories/)

```
表: Accounts

+-------------+------+
| 列名        | 类型  |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
在 SQL 中，account_id 是这个表的主键。
每一行都包含一个银行帐户的月收入的信息。
 

查询每个工资类别的银行账户数量。 工资类别如下：

"Low Salary"：所有工资 严格低于 20000 美元。
"Average Salary"： 包含 范围内的所有工资 [$20000, $50000] 。
"High Salary"：所有工资 严格大于 50000 美元。

结果表 必须 包含所有三个类别。 如果某个类别中没有帐户，则报告 0 。

按 任意顺序 返回结果表。

查询结果格式如下示例。

 

示例 1：

输入：
Accounts 表:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
输出：
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
解释：
低薪: 有一个账户 2.
中等薪水: 没有.
高薪: 有三个账户，他们是 3, 6和 8.
```

```sql
/* Write your PL/SQL query statement below */


select 'Low Salary' category, count(account_id) accounts_count 
from accounts
where income < 20000
union 
select 'Average Salary' category, count(account_id) accounts_count 
from accounts
where income <= 50000 and income >=20000
union 
select 'High Salary' category, count(account_id) accounts_count 
from accounts
where income > 50000
```

# 子查询

## [1978. 上级经理已离职的公司员工](https://leetcode.cn/problems/employees-whose-manager-left-the-company/)

```
表: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
在 SQL 中，employee_id 是这个表的主键。
这个表包含了员工，他们的薪水和上级经理的id。
有一些员工没有上级经理（其 manager_id 是空值）。
 

查找这些员工的id，他们的薪水严格少于$30000 并且他们的上级经理已离职。当一个经理离开公司时，他们的信息需要从员工表中删除掉，但是表中的员工的manager_id  这一列还是设置的离职经理的id 。

返回的结果按照employee_id 从小到大排序。

查询结果如下所示：

 

示例：

输入：
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
输出：
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

解释：
薪水少于 30000 美元的员工有 1 号(Kalel) 和 11号 (Joziah)。
Kalel 的上级经理是 11 号员工，他还在公司上班(他是 Joziah )。
Joziah 的上级经理是 6 号员工，他已经离职，因为员工表里面已经没有 6 号员工的信息了，它被删除了。
```

```sql
/* Write your PL/SQL query statement below */
select employee_id 
from employees 
where salary < 30000 and manager_id not in (select employee_id from employees)
order by employee_id asc
```

## [626. 换座位](https://leetcode.cn/problems/exchange-seats/)

```
表: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id 是该表的主键（唯一值）列。
该表的每一行都表示学生的姓名和 ID。
ID 序列始终从 1 开始并连续增加。
 

编写解决方案来交换每两个连续的学生的座位号。如果学生的数量是奇数，则最后一个学生的id不交换。

按 id 升序 返回结果表。

查询结果格式如下所示。

 

示例 1:

输入: 
Seat 表:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
输出: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
解释:
请注意，如果学生人数为奇数，则不需要更换最后一名学生的座位。
```

### `lag() over()` and `lead() over()` 前后顺移

lag与lead函数是跟偏移量相关的两个分析函数，通过这两个函数可以在一次查询中取出同一字段的前N行的数据(lag)和后N行的数据(lead)作为独立的列,从而更方便地进行进行数据过滤。

### `coalesce()` 返回第一个非NULL表达式

COALESCE是一个函数， (expression_1, expression_2, ...,expression_n)依次参考各参数表达式，遇到非null值即停止并返回该值。如果所有的表达式都是空值，最终将返回一个空值。使用COALESCE在于大部分包含空值的表达式最终将返回空值。

```sql
/* Write your PL/SQL query statement below */

select s.id, case when mod(s.id,2)=1 then coalesce(s.lead,student) else s.lag end student
from(
SELECT ID,STUDENT,lag(student,1,null) over(order by id) lag ,lead(student,1,null) over(order by id) lead
FROM seat) s

```



# 高级字符串函数 / 正则表达式 / 子句

## [1667. 修复表中的名字](https://leetcode.cn/problems/fix-names-in-a-table/)

表： `Users`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id 是该表的主键(具有唯一值的列)。
该表包含用户的 ID 和名字。名字仅由小写和大写字符组成。
```

 

编写解决方案，修复名字，使得只有第一个字符是大写的，其余都是小写的。

返回按 `user_id` 排序的结果表。

返回结果格式示例如下。

 

**示例 1：**

```
输入：
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
输出：
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

### `regexp_replace()`,`regexp_substr()`

`REGEXP_SUBSTR` 函数根据匹配项的模式返回给定字符串。检查语法：

```
  REGEXP_SUBSTR(srcstr, pattern [, position 
[, occurrence [, match_option]]]) 
```

在该函数中：

position:搜索起始位置
occurrence：要搜索的匹配项
match_option：用于更改默认匹配的选项。可以包含以下一个或多个值：

> “c”：使用区分大小写的匹配（默认值）
> “i”：使用区分大小写的匹配
> “n”：允许匹配任何字符的运算符
> “m”：将源字符串作为多行处理

`REGEXP_REPLACE` 函数返回给定字符串中的“已替换的”子字符串。检查语法：

```
  REGEXP_REPLACE(srcstr, pattern [,replacestr [, position 
[, occurrence [, match_option]]]]) 
```

在该函数中：

position:搜索起始位置
occurrence：要搜索的匹配项
replacestr：替换模式的字符串
match_option：用于更改默认匹配的选项。可以包含以下一个或多个值：

> “c”：使用区分大小写的匹配（默认值）
> “i”：使用区分大小写的匹配
> “n”：允许匹配任何字符的运算符
> “m”：将源字符串作为多行处理

```sql
/* Write your PL/SQL query statement below */

select user_id,  REGEXP_REPLACE(lower(name), '(^\w)', upper(REGEXP_SUBSTR(name, '(^\w)'))) name
from users
order by user_id asc
```

## [1527. 患某种疾病的患者](https://leetcode.cn/problems/patients-with-a-condition/)

```
患者信息表： Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
在 SQL 中，patient_id （患者 ID）是该表的主键。
'conditions' （疾病）包含 0 个或以上的疾病代码，以空格分隔。
这个表包含医院中患者的信息。
 

查询患有 I 类糖尿病的患者 ID （patient_id）、患者姓名（patient_name）以及其患有的所有疾病代码（conditions）。I 类糖尿病的代码总是包含前缀 DIAB1 。

按 任意顺序 返回结果表。

查询结果格式如下示例所示。

 

示例 1:

输入：
Patients表：
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
输出：
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
解释：Bob 和 George 都患有代码以 DIAB1 开头的疾病。
```



```sql
/* Write your PL/SQL query statement below */

select patient_id, patient_name, conditions
from patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'
```

## [196. 删除重复的电子邮箱](https://leetcode.cn/problems/delete-duplicate-emails/)

```
表: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id 是该表的主键列(具有唯一值的列)。
该表的每一行包含一封电子邮件。电子邮件将不包含大写字母。
 

编写解决方案 删除 所有重复的电子邮件，只保留一个具有最小 id 的唯一电子邮件。

（对于 SQL 用户，请注意你应该编写一个 DELETE 语句而不是 SELECT 语句。）

（对于 Pandas 用户，请注意你应该直接修改 Person 表。）

运行脚本后，显示的答案是 Person 表。驱动程序将首先编译并运行您的代码片段，然后再显示 Person 表。Person 表的最终顺序 无关紧要 。

返回结果格式如下示例所示。

 

示例 1:

输入: 
Person 表:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
输出: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
解释: john@example.com重复两次。我们保留最小的Id = 1。
```

```sql
/* Write your PL/SQL query statement below */

delete from person where id not in (
select min(id) from person group by email)
```

## [1484. 按日期分组销售产品](https://leetcode.cn/problems/group-sold-products-by-the-date/)

```
表 Activities：

+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
该表没有主键(具有唯一值的列)。它可能包含重复项。
此表的每一行都包含产品名称和在市场上销售的日期。
 

编写解决方案找出每个日期、销售的不同产品的数量及其名称。
每个日期的销售产品名称应按词典序排列。
返回按 sell_date 排序的结果表。
结果表结果格式如下例所示。

 

示例 1:

输入：
Activities 表：
+------------+-------------+
| sell_date  | product     |
+------------+-------------+
| 2020-05-30 | Headphone   |
| 2020-06-01 | Pencil      |
| 2020-06-02 | Mask        |
| 2020-05-30 | Basketball  |
| 2020-06-01 | Bible       |
| 2020-06-02 | Mask        |
| 2020-05-30 | T-Shirt     |
+------------+-------------+
输出：
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
解释：
对于2020-05-30，出售的物品是 (Headphone, Basketball, T-shirt)，按词典序排列，并用逗号 ',' 分隔。
对于2020-06-01，出售的物品是 (Pencil, Bible)，按词典序排列，并用逗号分隔。
对于2020-06-02，出售的物品是 (Mask)，只需返回该物品名。
```

### `listagg() within`

多列记录聚合为一条记录。像聚合函数一样，通过Group by语句，把每个Group的一个字段，拼接起来
`LISTAGG(XXX,XXX) WITHIN GROUP( ORDER BY XXX)`

```sql
/* Write your PL/SQL query statement below */

select  to_char(sell_date,'yyyy-mm-dd') sell_date, count(product) num_sold, listagg(product,',') within group(order by product) products
from (select distinct* from activities)
group by sell_date
```

## [1327. 列出指定时间段内所有的下单产品](https://leetcode.cn/problems/list-the-products-ordered-in-a-period/)

```
表: Products

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id 是该表主键(具有唯一值的列)。
该表包含该公司产品的数据。
 

表: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
该表可能包含重复行。
product_id 是表单 Products 的外键（reference 列）。
unit 是在日期 order_date 内下单产品的数目。
 

写一个解决方案，要求获取在 2020 年 2 月份下单的数量不少于 100 的产品的名字和数目。

返回结果表单的 顺序无要求 。

查询结果的格式如下。

 

示例 1:

输入：
Products 表:
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
Orders 表:
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+
输出：
+--------------------+---------+
| product_name       | unit    |
+--------------------+---------+
| Leetcode Solutions | 130     |
| Leetcode Kit       | 100     |
+--------------------+---------+
解释：
2020 年 2 月份下单 product_id = 1 的产品的数目总和为 (60 + 70) = 130 。
2020 年 2 月份下单 product_id = 2 的产品的数目总和为 80 。
2020 年 2 月份下单 product_id = 3 的产品的数目总和为 (2 + 3) = 5 。
2020 年 2 月份 product_id = 4 的产品并没有下单。
2020 年 2 月份下单 product_id = 5 的产品的数目总和为 (50 + 50) = 100 。
```

```sql
/* Write your PL/SQL query statement below */

select p.product_name,  sum(o.unit) unit
from orders o , products p
where o.product_id = p.product_id
group by to_char(o.order_date,'yyyy-mm'), p.product_name
having to_char(o.order_date,'yyyy-mm') = '2020-02' and sum(o.unit) >= 100
```

## [1517. 查找拥有有效邮箱的用户](https://leetcode.cn/problems/find-users-with-valid-e-mails/)

表: `Users`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id 是该表的主键（具有唯一值的列）。
该表包含了网站已注册用户的信息。有一些电子邮件是无效的。
```

 

编写一个解决方案，以查找具有有效电子邮件的用户。

一个有效的电子邮件具有前缀名称和域，其中：

1.  **前缀** 名称是一个字符串，可以包含字母（大写或小写），数字，下划线 `'_'` ，点 `'.'` 和/或破折号 `'-'` 。前缀名称 **必须** 以字母开头。
2. **域** 为 `'@leetcode.com'` 。

以任何顺序返回结果表。

结果的格式如以下示例所示：

 

**示例 1：**

```
输入：
Users 表:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+
输出：
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
解释：
用户 2 的电子邮件没有域。 
用户 5 的电子邮件带有不允许的 '#' 符号。
用户 6 的电子邮件没有 leetcode 域。 
用户 7 的电子邮件以点开头。
```

```sql
/* Write your PL/SQL query statement below */

select user_id, name, mail
from users
-- where regexp_substr(mail, '@(.*)') = '@leetcode.com' 
where regexp_substr(mail, '^[a-zA-Z][a-zA-Z0-9\_\.\/\-]*@leetcode\.com$') is not null
```

## [176. 第二高的薪水](https://leetcode.cn/problems/second-highest-salary/)

```
Employee 表：
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是这个表的主键。
表的每一行包含员工的工资信息。
 

查询并返回 Employee 表中第二高的 不同 薪水 。如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。

查询结果如下例所示。

 

示例 1：

输入：
Employee 表：
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
输出：
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
示例 2：

输入：
Employee 表：
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
输出：
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```

```sql
/* Write your PL/SQL query statement below */


select max(Salary) as SecondHighestSalary
  from Employee
 where Salary = (select Salary
                   from (select rownum as rw, Salary
                           from (select distinct Salary
                                   from Employee
                                  order by Salary desc))
                  where rw = 2)
```

## [1341. 电影评分](https://leetcode.cn/problems/movie-rating/)

表：`Movies`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id 是这个表的主键(具有唯一值的列)。
title 是电影的名字。
```

表：`Users`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id 是表的主键(具有唯一值的列)。
'name' 列具有唯一值。
```

表：`MovieRating`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) 是这个表的主键(具有唯一值的列的组合)。
这个表包含用户在其评论中对电影的评分 rating 。
created_at 是用户的点评日期。 
```

 

请你编写一个解决方案：

- 查找评论电影数量最多的用户名。如果出现平局，返回字典序较小的用户名。
- 查找在 `February 2020` **平均评分最高** 的电影名称。如果出现平局，返回字典序较小的电影名称。

**字典序** ，即按字母在字典中出现顺序对字符串排序，字典序较小则意味着排序靠前。

返回结果格式如下例所示。

 

**示例 1：**

```
输入：
Movies 表：
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users 表：
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating 表：
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
输出：
Result 表：
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
解释：
Daniel 和 Monica 都点评了 3 部电影（"Avengers", "Frozen 2" 和 "Joker"） 但是 Daniel 字典序比较小。
Frozen 2 和 Joker 在 2 月的评分都是 3.5，但是 Frozen 2 的字典序比较小。
```

```sql
/* Write your PL/SQL query statement below */

select name results from (select u.name
from movierating m, users u
where u.user_id = m.user_id
group by m.user_id, u.name
order by count(m.user_id) desc, u.name asc)
where rownum=1
union all
select title results from( select m.title
from movierating mr, movies m 
where m.movie_id=mr.movie_id and to_char(mr.created_at,'yyyy-mm')='2020-02'
group by mr.movie_id, m.title 
order by avg(mr.rating) desc, m.title asc)
where rownum=1
```

## [1321. 餐馆营业额变化增长](https://leetcode.cn/problems/restaurant-growth/)

```
表: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
在 SQL 中，(customer_id, visited_on) 是该表的主键。
该表包含一家餐馆的顾客交易数据。
visited_on 表示 (customer_id) 的顾客在 visited_on 那天访问了餐馆。
amount 是一个顾客某一天的消费总额。
 

你是餐馆的老板，现在你想分析一下可能的营业额变化增长（每天至少有一位顾客）。

计算以 7 天（某日期 + 该日期前的 6 天）为一个时间段的顾客消费平均值。average_amount 要 保留两位小数。

结果按 visited_on 升序排序。

返回结果格式的例子如下。

 

示例 1:

输入：
Customer 表:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+
输出：
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+
解释：
第一个七天消费平均值从 2019-01-01 到 2019-01-07 是restaurant-growth/restaurant-growth/ (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
第二个七天消费平均值从 2019-01-02 到 2019-01-08 是 (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
第三个七天消费平均值从 2019-01-03 到 2019-01-09 是 (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
第四个七天消费平均值从 2019-01-04 到 2019-01-10 是 (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86
```

```sql
/* Write your PL/SQL query statement below */


select to_char(visited_on,'yyyy-mm-dd') visited_on, sum_amount amount, round(sum_amount/7,2) average_amount
from(
select  visited_on, ranks,
sum(daily_amount) over (order by visited_on range between 6 preceding and current row) sum_amount
from   (
select  visited_on, sum(amount) daily_amount, rank() over(order by visited_on) ranks
from customer
group by visited_on
order by visited_on asc
) )
where ranks >= 7
```

## [602. 好友申请 II ：谁有最多的好友](https://leetcode.cn/problems/friend-requests-ii-who-has-the-most-friends/)

```
RequestAccepted 表：

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) 是这张表的主键(具有唯一值的列的组合)。
这张表包含发送好友请求的人的 ID ，接收好友请求的人的 ID ，以及好友请求通过的日期。
 

编写解决方案，找出拥有最多的好友的人和他拥有的好友数目。

生成的测试用例保证拥有最多好友数目的只有 1 个人。

查询结果格式如下例所示。

 

示例 1：

输入：
RequestAccepted 表：
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
输出：
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
解释：
编号为 3 的人是编号为 1 ，2 和 4 的人的好友，所以他总共有 3 个好友，比其他人都多。
 

进阶：在真实世界里，可能会有多个人拥有好友数相同且最多，你能找到所有这些人吗？
```

### `union , union all`

`union`会去重复， `union all`保留重复

```sql
/* Write your PL/SQL query statement below */

select w.id id, w.num num
from
(select distinct u.id id, 
sum(u.num) num,
rank() over (order by sum(u.num) desc) rn
from (
(select distinct accepter_id id, 
count(accepter_id) over (partition by accepter_id order by accepter_id) num
from requestaccepted
union all
select distinct requester_id id, 
count(requester_id) over (partition by requester_id order by requester_id) num
from requestaccepted)
) u
group by u.id) w
where w.rn = 1
```

## [585. 2016年的投资](https://leetcode.cn/problems/investments-in-2016/)

```
Insurance 表：

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid 是这张表的主键(具有唯一值的列)。
表中的每一行都包含一条保险信息，其中：
pid 是投保人的投保编号。
tiv_2015 是该投保人在 2015 年的总投保金额，tiv_2016 是该投保人在 2016 年的总投保金额。
lat 是投保人所在城市的纬度。题目数据确保 lat 不为空。
lon 是投保人所在城市的经度。题目数据确保 lon 不为空。
 

编写解决方案报告 2016 年 (tiv_2016) 所有满足下述条件的投保人的投保金额之和：

他在 2015 年的投保额 (tiv_2015) 至少跟一个其他投保人在 2015 年的投保额相同。
他所在的城市必须与其他投保人都不同（也就是说 (lat, lon) 不能跟其他任何一个投保人完全相同）。
tiv_2016 四舍五入的 两位小数 。

查询结果格式如下例所示。

 

示例 1：

输入：
Insurance 表：
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
输出：
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
解释：
表中的第一条记录和最后一条记录都满足两个条件。
tiv_2015 值为 10 与第三条和第四条记录相同，且其位置是唯一的。

第二条记录不符合任何一个条件。其 tiv_2015 与其他投保人不同，并且位置与第三条记录相同，这也导致了第三条记录不符合题目要求。
因此，结果是第一条记录和最后一条记录的 tiv_2016 之和，即 45 。
```

```sql
/* Write your PL/SQL query statement below */

select round(sum(tiv_2016),2) tiv_2016
from
(select pid, tiv_2016,
count(tiv_2015) over (partition by tiv_2015) count_tive_2015,
count(lat||lon) over (partition by lat||lon) count_lat_lon_2015
from insurance)
where count_lat_lon_2015 =1 and count_tive_2015 > 1
```

## [185. 部门工资前三高的所有员工](https://leetcode.cn/problems/department-top-three-salaries/)

```
表: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id 是该表的主键列(具有唯一值的列)。
departmentId 是 Department 表中 ID 的外键（reference 列）。
该表的每一行都表示员工的ID、姓名和工资。它还包含了他们部门的ID。
 

表: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id 是该表的主键列(具有唯一值的列)。
该表的每一行表示部门ID和部门名。
 

公司的主管们感兴趣的是公司每个部门中谁赚的钱最多。一个部门的 高收入者 是指一个员工的工资在该部门的 不同 工资中 排名前三 。

编写解决方案，找出每个部门中 收入高的员工 。

以 任意顺序 返回结果表。

返回结果格式如下所示。

 

示例 1:

输入: 
Employee 表:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department  表:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
输出: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
解释:
在IT部门:
- Max的工资最高
- 兰迪和乔都赚取第二高的独特的薪水
- 威尔的薪水是第三高的

在销售部:
- 亨利的工资最高
- 山姆的薪水第二高
- 没有第三高的工资，因为只有两名员工
```

### `dense_rank() , rank(), row_number()`

- `row_number()`：连续排序，如：1 2 3 4
- `rank()`: 跳跃 排序， 如： 1 2 2 4
- `dense_rank()`: 密集排序， 如：1 2 2 3

```sql
/* Write your PL/SQL query statement below */

select  d.name Department ,r.name employee,r.salary salary
from(
select
id, name, salary, departmentid,
dense_rank() over (partition by departmentid order by salary desc) salary_rank
from employee
) r, department d
where salary_rank <=3 and r.departmentid=d.id
order by d.name
```



