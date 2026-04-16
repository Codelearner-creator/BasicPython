def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

## Test ### 
print(twister([1, 2, 3, 4, 5], 2))
print(twister([4,2,1,-1,'a'], 4))
print(twister([] , 3))
print(twister([1], 10))
