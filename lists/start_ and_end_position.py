def find_start_end(nums, target):
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    start = binary_search_left(nums, target)
    end = binary_search_right(nums, target)

    # Check if the target is not within the range of the array
    if start >= len(nums) or nums[start] != target:
        return [-1, -1]

    return [start, end]

# Example usage:
nums1 = [5,7,7,8,8,10]
target1 = 8
print(find_start_end(nums1, target1))  # Output: [3,4]

nums2 = [5,7,7,8,8,10]
target2 = 6
print(find_start_end(nums2, target2))  # Output: [-1,-1]

nums3 = []
target3 = 0
print(find_start_end(nums3, target3))  # Output: [-1,-1]
