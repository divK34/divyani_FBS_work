# Anagram : number of characters and the chararacters aare same but the word differs.
# str1 = "car" 
# str2 = "arc"

# Python Program to Detect if Two Strings are Anagrams

str1 = "listen"
str2 = "silent"
cnt = 0
if len(str1) == len(str2):
    for ele in str1:
        if str2.count(ele) == str1.count(ele):
            cnt += 1
        else:
            cnt = 0
    if cnt == len(str1):
        print("anagram")
    else:
        print("almost but nope")
else:
    print("nope")
            
