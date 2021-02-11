
# iterative
def binary_search(nums, target):
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1
    return -1
    

if __name__ == "__main__":
    nums = [1, 4, 5, 6, 7, 8, 9]
    res = binary_search(nums, 7)
    print(res)