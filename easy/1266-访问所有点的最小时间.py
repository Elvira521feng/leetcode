#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author：Elvira

"""
平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。
你可以按照下面的规则在平面上移动：
每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。

示例 1：
images/1266-1.png
输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
从 [1,1] 到 [3,4] 需要 3 秒
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒

示例 2：
输入：points = [[3,2],[-2,2]]
输出：5
 

提示：
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-time-visiting-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

知识补充：https://baike.baidu.com/item/%E5%88%87%E6%AF%94%E9%9B%AA%E5%A4%AB%E8%B7%9D%E7%A6%BB/8955729?fr=aladdin
切比雪夫距离（Chebyshev distance）或是L∞度量，是向量空间中的一种度量，二个点之间的距离定义是其各坐标数值差绝对值的最大值。以数学的观点来看，切比雪夫距离是由一致范数（uniform norm）（或称为上确界范数）所衍生的度量，也是超凸度量（injective metric space）的一种。
"""


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def dist(pt1, pt2):
            return max(abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1]))

        steps = 0
        if len(points) < 2:
            return steps
        for idx, point in enumerate(points):
            if idx == 0:
                continue
            step = dist(point, points[idx - 1])
            steps += step
        return steps