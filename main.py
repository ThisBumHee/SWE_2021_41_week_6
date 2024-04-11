from typing import List

def twoSum(nums: List[int], target: int)->List[int]:
    number = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in number:
            return [number[complement],i]
        number[num] = i

    return []

nums_input = input("Enter the list of numbers separated by spaces: ")
target_input = int(input("Enter the target number: "))

nums = list(map(int, nums_input.split()))

result = twoSum(nums, target_input)

if result:
    print("Indices of the two numbers:", result)
else:
    print("No solution found.")