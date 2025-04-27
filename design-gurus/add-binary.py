def sum_binary(str1, str2):
    carry = 0
    summ = ""
    biggest_str, smallest_str = str1, str2
    if len(str1) < len(str2):
        biggest_str = str2
        smallest_str = str1

    biggest_str = list(biggest_str)
    smallest_str = list(smallest_str)

    for i in range(len(biggest_str) - 1, -1, -1):
        first = biggest_str[i]
        second = 0 if len(smallest_str) == 0 else smallest_str.pop()
        local_sum = int(first) + int(second) + int(carry)
        if local_sum <= 1:
            carry = 0
            summ = str(local_sum) + summ
        else:
            num_to_add = "0"
            if local_sum > 2:
                num_to_add = "1"

            summ = num_to_add + summ
            carry = 1

    for i in range(carry):
        summ = "1" + summ

    return summ


# print(sum_binary("10110", "10101"))
print(sum_binary("111", "1"))
