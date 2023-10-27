"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or 
equal to target. If there is no such subarray, return 0 instead.
"""

def min_size_subarray_sum(nums, target):
  # Pre-condition: If `nums` is empty, do nothing.
  if not nums:
    return 0
  
  left = 0  # Left side of the sliding window.
  window_sum = 0  # Sum of the sliding window.
  min_size = float('inf')  # Size of the sliding window.

  # Right side of the sliding window.
  # The sliding window expands to the right with each iteration.
  for right in range(len(nums)):
    window_sum += nums[right]

    # If the sliding window sum satisfies the requirement
    # of being greater than or equal to the target, record the
    # size of the window if it's less than the previously
    # recorded `min_size`. At the same time, narrow the sliding
    # window by incrementing the position of the left side of the
    # sliding window until the sum of the sliding window is 
    # less than the required target sum.
    while window_sum >= target:
      min_size = min(min_size, right - left + 1)
      window_sum -= nums[left]
      left += 1

  # If the size of the sliding window is not equal to infinity (which is 
  # the initial value of `min_size`), it means we have found a subarray
  # with a sum greater than or equal to the target.
  return min_size if min_size != float('inf') else 0


assert min_size_subarray_sum([2,3,1,2,4,3], 7) == 2
assert min_size_subarray_sum([1,4,4], 4) == 1
assert min_size_subarray_sum([1,1,1,1,1,1,1,1], 11) == 0
assert min_size_subarray_sum([1,1,1,1,1,1,1,1,1,1,1], 11) == 11