def merge(s1, s2):
	new = ''
	for i in range(len(s1)):
		new += s1[i]
		if i < len(s2):
			new += s2[i]

	if len(s2) > len(s1):
		new += s2[len(s1):]
	
	return new
