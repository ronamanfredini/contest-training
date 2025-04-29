def repeated_substring(str):
	left = 0
	for right in range(len(str)):
		pattern = str[left:right + 1]
		pattern_iterator = len(pattern)
		while pattern_iterator < len(str):
			if pattern == str[pattern_iterator - len(pattern): pattern_iterator]:
				pattern_iterator += len(pattern)
				continue
			else:
				break
		else:
			if pattern_iterator == len(str) and len(pattern) != len(str):
				return True
	return False


# print(repeated_substring('bcdbcdbcdbcd'))
# print(repeated_substring('aabaaba'))
print(repeated_substring('abac'))