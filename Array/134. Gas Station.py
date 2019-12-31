"""
与求最大子串的起始位置代码几乎没有区别，只需要记录一下起始角标。

一次遍历法，车能开完全程需要满足两个条件：
1、车从i站能开到i+1；
2、所有站里的油总量要>=车子的总耗油量；
3、假设从编号为0站开始，一直到k站都正常，在开往k+1站时车子没油了。这时，应该将起点设置为k+1站。

"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
         # 将问题转化为找最大子串的起始位置。
        res = 0
        run = 0
        start = 0

        for i in range(len(gas)):
            # 记录从start位置开始到当前油箱里剩余的总油量
            run += gas[i] - cost[i]
            # 用于判断是否有跑完全程所需的油
            res += gas[i] - cost[i]

            if run < 0:
                start = i+1
                run = 0

        return start if res >=0 else -1



