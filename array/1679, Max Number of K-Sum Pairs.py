from collections import List, defaultdict


class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            count[num] += 1

        for num in nums:
            target = k - num

            if num == target:  # k=6, num = 3, target = 3, 假设: 3 = 8个
                if count[num] >= 2:  # 这样, 起码有两个才行, 比如: 3: 1 这种就不满足条件
                    count[num] -= 2
                    res += 1
            else:
                if count[num] >= 1 and count[target] >= 1:  # 能成对
                    # k = 6, (2:5, 4:1), num = 2
                    count[num] -= 1
                    count[target] -= 1
                    res += 1

        return res


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            count[num] += 1  # 将数组转换成一个次数的哈希表

        for num in list(count.keys()):  # 只需要loop 这个哈希表就可以了
            target = k - num
            # count 中的target 够 & count 中的 num够, 这样能凑成一对
            if count[target] >= 1 and count[num] >= 1:
                if target == num:
                    # 这样, 比如: k=6, (3,3) , 3 的 出现次数为7, 那么一共 3对
                    pairs = count[target] // 2
                    res += pairs
                    count[target] -= pairs * 2
                else:
                    # (2,4), {2:5, 4: 3}, pairs = 3
                    pairs = min(count[target], count[num])
                    res += pairs
                    count[target] -= pairs
                    count[num] -= pairs

        return res


class TwoPointerSolution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1, 3,3,3,4
        nums.sort()

        left = 0
        right = len(nums) - 1

        res = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:  # 小了, 挪left, 往大 了 走
                left += 1
            elif sum > k:  # 大了, 挪right, 往小了走
                right -= 1
            else:
                left += 1
                right -= 1
                res += 1

        return res
