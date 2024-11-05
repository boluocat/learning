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
