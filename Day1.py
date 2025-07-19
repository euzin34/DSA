# Minimum Operations to Reduce X to Zero

def min_operation(arrlen: int, target_num: int, arr: list[int]):

    arr_sum = sum(arr)
    sub_array = arr_sum - target_num

    if sub_array < 0:
        return -1
    
    #use sliding window technique

    current_sum = 0
    left_ptr = 0
    return_val = -1

    for right_ptr in range(arrlen):
        current_sum += arr[right_ptr]

    while current_sum > sub_array and left_ptr <= right_ptr:
        current_sum -= arr[left_ptr]
        left_ptr +=1

        if current_sum == sub_array:
            return_val = max(return_val, right_ptr - left_ptr + 1)

    if return_val == -1:
        return -1
    else:
        return arrlen - return_val
    