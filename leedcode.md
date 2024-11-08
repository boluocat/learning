# [3200. 三角形的最大高度](https://leetcode.cn/problems/maximum-height-of-a-triangle/)

给你两个整数 `red` 和 `blue`，分别表示红色球和蓝色球的数量。你需要使用这些球来组成一个三角形，满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。

每一行的球必须是 **相同** 颜色，且相邻行的颜色必须 **不同**。

返回可以实现的三角形的 **最大** 高度。

 

**示例 1：**

**输入：** red = 2, blue = 4

**输出：** 3

**解释：**

![img](https://assets.leetcode.com/uploads/2024/06/16/brb.png)

上图显示了唯一可能的排列方式。

**示例 2：**

**输入：** red = 2, blue = 1

**输出：** 2

**解释：**

![img](https://assets.leetcode.com/uploads/2024/06/16/br.png)
上图显示了唯一可能的排列方式。

**示例 3：**

**输入：** red = 1, blue = 1

**输出：** 1

**示例 4：**

**输入：** red = 10, blue = 1

**输出：** 2

**解释：**

![img](https://assets.leetcode.com/uploads/2024/06/16/br.png)
上图显示了唯一可能的排列方式。

```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        less = min(red, blue)
        more = max(red, blue)
        layer = 1
        odd = 0
        event = 0
        while True:
            if layer % 2 == 1:
                odd += layer
            else:
                event += layer
            if max(odd, event) > more or min(odd, event) > less:
                return layer-1
            layer += 1
```

# [1. 两数之和](https://leetcode.cn/problems/two-sum/)

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

 

**提示：**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **只会存在一个有效答案**



运用字典进行nums的存储，key值为item，value为index。

遍历nums，如果target - value 在字典中存在，且不是同一个item。则输出index

 ```python
 class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         nums_dict = dict(zip(nums,range(len(nums))))
         
         for k, i in enumerate(nums):
             minus_value = target-i
             if nums_dict.get(minus_value, 0) and k != nums_dict[minus_value]:
                return [k,nums_dict[minus_value]] 
 ```

