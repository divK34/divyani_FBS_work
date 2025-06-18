# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number. 

def find_triplets(nums, target):
    triplets = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
    return triplets

nums = [1, 2, 3, 4, 5, 6]
target = 10
print(find_triplets(nums, target))
