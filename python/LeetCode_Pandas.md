# [175. 组合两个表](https://leetcode.cn/problems/combine-two-tables/)

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



```python
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    merge_pd = pd.merge(person, address, how = 'left', on = 'personId')
    result = merge_pd.loc[:,['firstName', 'lastName', 'city', 'state']]
    
    return result
```



# [176. 第二高的薪水](https://leetcode.cn/problems/second-highest-salary/)

`Employee` 表：

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是这个表的主键。
表的每一行包含员工的工资信息。
```

 

查询并返回 `Employee` 表中第二高的 **不同** 薪水 。如果不存在第二高的薪水，查询应该返回 `null(Pandas 则返回 None)` 。

查询结果如下例所示。

 

**示例 1：**

```
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
```

**示例 2：**

```
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

1. 利用`groupby()`进行归类，然后统计一下去重后的工资有多少人
2. 当去重复后的数据长度小于2的时候，则表示没有第二高的工资，返回`null`
3. 当大于等于2时，将用`salary`作为key值进行排序（从大到小）
4. 然后去除原有的index，重新按照新的顺序给一个index
5. 取index=1的salary进行输出

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_info = employee.groupby('salary').count().reset_index()
    
    if len(unique_info) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        unique_info.sort_values('salary',ascending=False, inplace=True)
        unique_info = unique_info.reset_index(drop=True)
        return pd.DataFrame({'SecondHighestSalary':[unique_info['salary'][1]]})
```

或者在第一步的时，使用`drop_duplicats()`进行去重。

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_info = employee.drop_duplicates('salary')
    print(unique_info)
    
    if len(unique_info) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        unique_info.sort_values('salary',ascending=False, inplace=True)
        unique_info = unique_info.reset_index(drop=True)
        return pd.DataFrame({'SecondHighestSalary':[unique_info['salary'][1]]})
```

# [177. 第N高的薪水](https://leetcode.cn/problems/nth-highest-salary/)

表: `Employee`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是该表的主键。
该表的每一行都包含有关员工工资的信息。
```

 

查询 `Employee` 表中第 `n` 高的工资。如果没有第 `n` 个最高工资，查询结果应该为 `null` 。

查询结果格式如下所示。

 

**示例 1:**

```
输入: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
输出: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

**示例 2:**

```
输入: 
Employee 表:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
输出: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```

需要注意的：

1. 首先需要将salary去重复
2. 在重复的基础上再进行降序排列，重新给index
3. 在判断是否存在第N位的时候，需要考虑给入的N是0和负数的情况（这种方法是按照index去取值，所在在index为0或负数的时候也能出值，但是不是正确的答案）

```python
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    top_n_df = pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    drop_duplicates = employee.drop_duplicates('salary')
    sorted_df = drop_duplicates.sort_values('salary',ascending = False)
    sorted_df.reset_index(drop=True, inplace=True)

    if len(sorted_df) < N or N <= 0:
        return top_n_df
    else:
        top_n_df.iloc[0,0] = sorted_df.iloc[N-1]['salary']
        return top_n_df
```

推荐用下面这种

1. 使用`df['col'].rank()`标记出序列列
2. 筛选ranks列中等于N的salary，可以规避到当N小于等于0的时候，按照index在pandas中取值的情况

```python
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    drop_duplicates = employee.drop_duplicates('salary')
    drop_duplicates['ranks'] = drop_duplicates['salary'].rank(method='dense',ascending=False)
    ans = drop_duplicates[drop_duplicates['ranks'] == N][['salary']]
    if len(ans) == 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        ans = ans.rename(columns = {'salary':f'getNthHighestSalary({N})'})
        return ans

```

# [178. 分数排名](https://leetcode.cn/problems/rank-scores/)

表: `Scores`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id 是该表的主键（有不同值的列）。
该表的每一行都包含了一场比赛的分数。Score 是一个有两位小数点的浮点值。
```

 

编写一个解决方案来查询分数的排名。排名按以下规则计算:

- 分数应按从高到低排列。
- 如果两个分数相等，那么两个分数的排名应该相同。
- 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。

按 `score` 降序返回结果表。

查询结果格式如下所示。

 

**示例 1:**

```
输入: 
Scores 表:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
输出: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

- 分数应按从高到低排列.   -------  `ascending = False`
- 如果两个分数相等，那么两个分数的排名应该相同。  -------  `rank()`:进行标记
- 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。  -----使用`method = dense`

```python
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores.sort_values('rank', ascending = True, inplace = True)

    return scores[['score','rank']]
```



# [1107. 每日新用户统计](https://leetcode.cn/problems/new-users-daily-count/)

`Traffic` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
该表可能有重复的行。
activity 列是 ENUM 类型，可能取 ('login', 'logout', 'jobs', 'groups', 'homepage') 几个值之一。
```

 

编写解决方案，找出从今天起最多 90 天内，每个日期该日期首次登录的用户数。假设今天是 **2019-06-30** 。

以 **任意顺序** 返回结果表。

结果格式如下所示。

 

 

**示例 1：**

```
输入：
Traffic 表：
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+
输出：
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+
解释：
请注意，我们只关心用户数非零的日期.
ID 为 5 的用户第一次登陆于 2019-03-01，因此他不算在 2019-06-21 的的统计内。
```



```python
import pandas as pd
import datetime
def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    
    # calculate limited date
    date_str = '2019-06-30'
    date_format = '%Y-%m-%d'
    date_obj = datetime.datetime.strptime(date_str, date_format)
    limited_date = date_obj + datetime.timedelta(days=-90)

    # get first login date of each user, filter data
    mask1 = (traffic['activity'] == 'login') 
    first_login_date = traffic[mask1].groupby('user_id').min()
    mask2 = (first_login_date['activity_date'] >= limited_date)
    login_user = first_login_date[mask2]

    # get each day's login user number
    result = login_user.groupby('activity_date').count().reset_index()
    result = result.rename(columns={'activity_date':'login_date','activity':'user_count'})
    result.sort_values('login_date', inplace=True)

    return result
```



```python
import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:

    # calculate limited date
    now = pd.to_datetime('2019-06-30')
    ago = now - pd.Timedelta(days=90)

    # get first login date of each user, filter data
    mask1 = (traffic['activity'] == 'login') 
    first_login_date = traffic[mask1].groupby('user_id').min()
    mask2 = (first_login_date['activity_date'] >= ago)
    login_user = first_login_date[mask2]

    # get each day's login user number
    result = login_user.groupby('activity_date').count().reset_index()
    result = result.rename(columns={'activity_date':'login_date','activity':'user_count'})
    result.sort_values('login_date', inplace=True)

    return result
```





# [1113. 报告的记录](https://leetcode.cn/problems/reported-posts/)

动作表：`Actions`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    | 
| action        | enum    |
| extra         | varchar |
+---------------+---------+
此表可能会有重复的行。
action 字段是 ENUM 类型的，包含:('view', 'like', 'reaction', 'comment', 'report', 'share')
extra 包含关于 action 的可选信息，例如举报的原因或反馈的类型。
当 action 为 'report' 时 extra 不会为 NULL。
```

 

编写解决方案，针对每个举报原因统计昨天的举报帖子数量。假设今天是 `2019-07-05` 。每天同一个post_id发布的同原因投诉，不做重复统计

返回结果表 **无顺序要求** 。

结果格式如下示例所示。

 

**示例 1：**

```
输入：
Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 4       | 2019-07-04  | view   | null   |
| 2       | 4       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-04  | view   | null   |
| 5       | 2       | 2019-07-04  | report | racism |
| 5       | 5       | 2019-07-04  | view   | null   |
| 5       | 5       | 2019-07-04  | report | racism |
+---------+---------+-------------+--------+--------+
输出：
+---------------+--------------+
| report_reason | report_count |
+---------------+--------------+
| spam          | 1            |
| racism        | 2            |
+---------------+--------------+ 
解释：注意，我们只关心举报帖数量非零的举报原因。
```

```python
import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    
    report_df = actions[actions['action'] == 'report']
    yesteday_df = report_df[report_df['action_date'] == '2019-07-04'].loc[:,['post_id','extra']]
    unique_post = yesteday_df.drop_duplicates(['post_id','extra'])
    post_count = unique_post.groupby('extra').count().reset_index()
    result = post_count.rename(columns={'extra':'report_reason','post_id':'report_count'})

    return result
```

