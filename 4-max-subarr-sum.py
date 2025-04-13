def max_subarray_sum_sliding_window(arr, k):
    n = len(arr)

    window_sum = sum(arr[:k])

    max_sum = window_sum
    max_start_index = 0

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        if (window_sum > max_sum):
            max_sum = window_sum
            max_start_index = i + 1
    return arr[max_start_index:max_start_index + k], max_sum

print(max_subarray_sum_sliding_window([3,2,7,5,9,6,2],3))

