def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while ...:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ...
        elif nums[mid] < target:
            left = ...
        elif nums[mid] > target:
            right = ...
    return ...

# Find a num:寻找一个数（基本的二分搜索）

class Solution:
    # 标准的二分搜索框架，搜索目标元素的索引，若不存在则返回 -1
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # 注意
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 注意
                left = mid + 1
            elif nums[mid] > target:
                # 注意
                right = mid - 1
        return -1
    


def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)
    
    # 注意
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid

    return left
