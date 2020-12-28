#!/usr/bin/python3


def find_two_nums_that_add_to_N(sorted_input, N):
    i = 0
    j = len(sorted_input) - 1
    while i < j:
        my_sum = sorted_input[i] + sorted_input[j]
        if my_sum > N:
            j -= 1
        elif my_sum < N:
            i += 1
        else:
            a = sorted_input[i]
            b = sorted_input[j]
            return (a, b)
    return None


def find_invalid_number(nums, window_size):
    N = window_size
    i = 0
    while N + i < len(nums):
        magic_number = nums[N + i]
        window = nums[i : N + i]
        if not find_two_nums_that_add_to_N(sorted(window), magic_number):
            return magic_number
        i += 1
    return None


def find_encryption_weakness(nums, invalid_number):
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s > invalid_number:
                break
            elif s == invalid_number:
                _range = nums[i : j + 1]
                return max(_range) + min(_range)
    return None


if __name__ == "__main__":
    with open("input") as f:
        raw_in = f.read()
        nums = [int(i) for i in raw_in.splitlines()]

        invalid_number = find_invalid_number(nums, 25)
        print("Invalid number is {}".format(invalid_number))

        weakness = find_encryption_weakness(nums, invalid_number)
        print("Encryption weakness is {}".format(weakness))
