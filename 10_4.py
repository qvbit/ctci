def search_infinite(arr, target):
    l, r = 0, 1
    
    while arr[r] != -1 and arr[r] < target:
        l, r = r, r << 1
    
    return binary_search(arr, l, r, target)


def binary_search(arr, l, r, target):
    while l <= r:
        m = (l+r)//2

        if arr[m] < target:
            l = m+1
        elif arr[m] > target:
            r = m-1
        else:
            return m
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 7, 8, 9, 10, 12, 14] + [-1]*1000
    print(search_infinite(arr, 1))

