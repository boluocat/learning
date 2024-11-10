# 数组/字符串

## [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)

给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。

 

**示例 1：**

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

### `sort()`/`sorted()`

- `list.sort()` method that modifies the list in-place.
- `sorted(list)` builds a new sorted list.

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:] = nums2
        print(nums1.sort())
```



双指针：

```python

```

## [27. 移除元素](https://leetcode.cn/problems/remove-element/)

给你一个数组 `nums` 和一个值 `val`，你需要 **[原地](https://baike.baidu.com/item/原地算法)** 移除所有数值等于 `val` 的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。

假设 `nums` 中不等于 `val` 的元素数量为 `k`，要通过此题，您需要执行以下操作：

- 更改 `nums` 数组，使 `nums` 的前 `k` 个元素包含不等于 `val` 的元素。`nums` 的其余元素和 `nums` 的大小并不重要。
- 返回 `k`。

**用户评测：**

评测机将使用以下代码测试您的解决方案：

```
int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有的断言都通过，你的解决方案将会 **通过**。

 

**示例 1：**

```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

**示例 2：**

```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

 

**提示：**

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`



思路：

看着题很复杂的样子。简单说：

1. 不能真正的移除元素
2. `nums` 的其余元素和 `nums` 的大小并不重要。意思是说，在指定index后的实际值是啥，不重要
3. 从0开始定义指针，然后依次比较nums中的元素和val的值。
   1. 如果不相等，写入nums中本次对应的k index位。k自加
   2. 如果相等，跳过

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for item in nums:
            if item != val:
                nums[k] = item
                k += 1
            else:
                pass

        return k
```



## [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

给你一个 **非严格递增排列** 的数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。

考虑 `nums` 的唯一元素的数量为 `k` ，你需要做以下事情确保你的题解可以被通过：

- 更改数组 `nums` ，使 `nums` 的前 `k` 个元素包含唯一元素，并按照它们最初在 `nums` 中出现的顺序排列。`nums` 的其余元素与 `nums` 的大小不重要。
- 返回 `k` 。

**判题标准:**

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

 

**示例 1：**

```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

- `1 <= nums.length <= 3 * 104`
- `-104 <= nums[i] <= 104`
- `nums` 已按 **非严格递增** 排列

思路：

1. 不能新增一个存储，不在意非重复项之后的数值是什么
2. 创建两个指针。第一个指针用作存储位，第二个指针用作比较位（持续后移）
3. 如果两个指针对应的值相同，将第二个指针的值写到第一个指针所在位置，第一个指针保存不变
4. 如果值不同，第一个指针后移一位，将第二个指针的值写到第一个指针所在处
5. 返回第一个指针的值+1 （因为第一个指针是从0开始计数的，如果是反映不用值的数量，需要+1）

```PYTHON
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ft_pointer = 0
        sc_pointer = 1

        while sc_pointer < len(nums):

            if nums[ft_pointer] == nums[sc_pointer]:
                nums[ft_pointer] = nums[sc_pointer]
            else:
                ft_pointer += 1
                nums[ft_pointer] = nums[sc_pointer]
            
            sc_pointer += 1

        return ft_pointer+1
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ft_pointer = 0
        
        for sc_pointer in range(1,len(nums)):

            if nums[ft_pointer] == nums[sc_pointer]:
                nums[ft_pointer] = nums[sc_pointer]
            else:
                ft_pointer += 1
                nums[ft_pointer] = nums[sc_pointer]
                

        return ft_pointer+1
```



```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ft_pointer = 1

        for sc_pointer in range(1,len(nums)):

            if nums[sc_pointer-1] != nums[sc_pointer]:
                nums[ft_pointer] = nums[sc_pointer]
                ft_pointer += 1
                
        return ft_pointer
```



## [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)

给你一个有序数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

 

**说明：**

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

 

**示例 1：**

```
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

- `1 <= nums.length <= 3 * 104`
- `-104 <= nums[i] <= 104`
- `nums` 已按升序排列



思路：

1. 要求：原地删除，同一数只保留两个
2. 如果nums小于等于2， 返回整个数组的长度
3. 设置向左偏移的存储point l，起始位2
4. 从nums的第三位开始向左进行比较。如果不等于第一位，则存储在 l 位。（这样可以保证不会出现连续三个一样的数值。）

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)
        
        l = 2
        for k,v in enumerate(nums[2:]):
            if nums[l - 2] != v:
                nums[l] = v
                l += 1
            
        return l
```



## [169. 多数元素](https://leetcode.cn/problems/majority-element/)

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

**提示：**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

```python
# 时间复杂度为 O(n)、空间复杂度为 O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        target = len(nums)/2
        items_nums = dict()
        for i in nums:
            items_nums[i] = items_nums.get(i,0) + 1
        
        for k,v in items_nums.items():
            if v > target:
                return k
```

### 摩尔投票

推论一： 若记 众数 的票数为 +1 ，非众数 的票数为 −1 ，则一定有所有数字的 票数和 >0 。

推论二： 若数组的前 a 个数字的 票数和 =0 ，则 数组剩余 (n−a) 个数字的 票数和一定仍 >0 ，即后 (n−a) 个数字的 众数仍为 x 。

根据以上推论，记数组首个元素为 n1 ，众数为 x ，遍历并统计票数。当发生 票数和 =0 时，剩余数组的众数一定不变 ，这是由于：

- 当 n 1 =x ： 抵消的所有数字中，有一半是众数 x 。
- 当 n 1！=x ： 抵消的所有数字中，众数 x 的数量最少为 0 个，最多为一半。

利用此特性，每轮假设发生 票数和 =0 都可以 缩小剩余数组区间 。当遍历完成时，最后一轮假设的数字即为众数。

算法流程:

- 初始化： 票数统计 votes = 0 ， 众数 x。
- 循环： 遍历数组 nums 中的每个数字 num 。
  - 票数 votes 等于 0 ，则假设当前数字 num 是众数。
  - 当 num = x 时，票数 votes 自增 1 ；当 num != x 时，票数 votes 自减 1 。

- 返回值： 返回 x 即可。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        votes, count = 0,0
        
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        
        for num in nums:
            if num == x:
                count += 1
        
        return x if count > len(nums)/2 else 0
```

| items | votes | x     | count |
| ----- | ----- | ----- | ----- |
| 2     | 1     | 2     | 1     |
| 2     | 2     | 2     | 2     |
| 1     | 1     | 2     | 2     |
| 1     | 0     | 2     | 2     |
| 1     | 1     | 1     | 3     |
| 2     | 0     | 1     | 3     |
| 2     | 1     | **2** | 4     |

