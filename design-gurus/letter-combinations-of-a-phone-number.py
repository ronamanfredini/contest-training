def solution(digits):
    str_len = len(digits)
    if str_len == 0:
        return []
    unique = set()
    digits = list(digits)
    number_pad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def dfs(i, curr_str):
        if len(curr_str) == str_len:
            unique.add(curr_str)
            return
        if i >= str_len:
            return
        available_digits = number_pad.get(digits[i])
        for char in available_digits:
            dfs(i + 1, curr_str + char)

    dfs(0, '')
    return list(unique)


print(solution("47"))
# print(solution("234"))
# print(solution("2345"))
# print(solution("23456"))