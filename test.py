def maxSubarray(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    cur_max = float("-inf")  # max sum ending at current position
    global_max = float("-inf")  # max sum over the entire array
    for num in nums:
        cur_max = max(cur_max+num, num)
        global_max = max(global_max, cur_max)
    return global_max


def isValid(s: str) -> bool:
    left2right = {"(":")", "{":"}", "[":"]"}
    stack = []  # stack to store unmatched left brackets
    for s_i in s:
        if s_i in left2right:
            stack.append(s_i)
        elif len(stack) == 0 or s_i != left2right[stack.pop()]:
            return False
    return False if len(stack) > 0 else True


if __name__ == "__main__":
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    # nums = [5,4,-1,7,8]
    # print(maxSubarray(nums))

    # s = "()"
    # s = "()[]{}"
    # s = "(]"
    s = "([)]"
    print(isValid(s))

