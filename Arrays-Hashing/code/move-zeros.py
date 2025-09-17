from typing import List


def move_zeros(nums: List[int]) -> None:
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)


# Counter = 0
# Loop through our array:
# if a num equals zero:
# remove it from our array
# increment the counter

# while counter is greater than 0:
# append zero to the array
