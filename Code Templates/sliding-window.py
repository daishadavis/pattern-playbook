def sliding_window_fixed(input, k):
    left = 0
    window_sum = 0

    for right in range(len(input)):
        window_sum += input[right]
        if right > k - 1:
            # process the window
            window_sum -= input[left]
            left += 1


def dynmanic_sliding_window(input):
    left = ans = curr = 0

    for right in range(len(input)):
        # do logic here to add arr[right] to curr

        while Window_Conditon_Broken:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans
