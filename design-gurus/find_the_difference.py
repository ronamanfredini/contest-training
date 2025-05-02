def find_char(s, t):
    original_str_map = {}
    for char in s:
        found_char = original_str_map.get(char, 0)
        original_str_map[char] = found_char + 1

    for char in t:
        if char not in original_str_map:
            return char
        if original_str_map.get(char) == 0:
            return char
        original_str_map[char] -= 1
