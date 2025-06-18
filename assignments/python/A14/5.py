#  Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""
    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        chars = set(s[i] for s in strs)
        if len(chars) == 1:
            prefix += list(chars)[0]
        else:
            break

    return prefix

strings = ["apple", "app", "application"]
print("Longest common prefix:", longest_common_prefix(strings))
