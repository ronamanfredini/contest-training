def is_substring(search_term, base):
    i = j = 0
    if len(base) < len(search_term):
        return False

    while i < len(base):
        if base[i] == search_term[j]:
            i += 1
            j += 1
            if j == len(search_term):
                return True
        else:
            i += 1
    return False
