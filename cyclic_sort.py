def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]-1 # index that nums[i] should be at
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


if __name__ == "__main__":
    nums = [2, 6, 4, 3, 1, 5]
    cyclic_sort(nums)
    print(nums)