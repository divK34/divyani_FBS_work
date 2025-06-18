#  Write a Python program to find all the anagrams and group them together from a given list of strings. 

def sort_letters(word):
    letters = list(word)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[i] > letters[j]:
                letters[i], letters[j] = letters[j], letters[i]
    return letters

def group_anagrams(words):
    groups = []
    sorted_groups = []

    for w in words:
        sorted_w = sort_letters(w)
        found = False
        for i in range(len(sorted_groups)):
            if sorted_groups[i] == sorted_w:
                groups[i].append(w)
                found = True
                break
        if not found:
            groups.append([w])
            sorted_groups.append(sorted_w)

    return groups

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
