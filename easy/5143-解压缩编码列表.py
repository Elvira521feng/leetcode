#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author：Elvira
"""
给你一个以行程长度编码压缩的整数列表 nums 。
考虑每相邻两个元素 [a, b] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后有 a 个值为 b 的元素。
请你返回解压后的列表。
示例：

输入：nums = [1,2,3,4]
输出：[2,4,4,4]
提示：
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decompress-run-length-encoded-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_res = list()

        for i in range(0, len(nums), 2):
            list_tmp = nums[i] * [nums[i + 1]]
            list_res.extend(list_tmp)

        return list_res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    res = s.decompressRLElist(nums)
    print(res)
