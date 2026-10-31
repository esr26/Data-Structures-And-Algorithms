def leaders_in_array(nums):
    max_value = float('-inf')
    result = []

    for value in reversed(nums):
        if value > max_value:
            result.append(value)
            max_value = value

    return result[::-1]
