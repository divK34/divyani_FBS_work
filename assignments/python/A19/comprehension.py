# 1. Find all of the numbers from 1–1000 that are divisible by 8
res_1 = [i for i in range(1,1001) if i%8==0]
print("Numbers divisible by 8 = ",res_1)

# 2. Find all of the numbers from 1–1000 that have a 6 in them
res2 = [i for i in range(1,1001) if "6" in str(i)]
print("Numbers that have 6 in them = ",res2)

# 3. Count the number of spaces in a string (take input from user)
s3 = input("Enter your string = ")
res3 = sum([1 for ch in s3 if ch == " "])
print("Number of spaces =", res3)

# 4.  Remove all of the vowels in a string (take input from user) 
s4 = input("Enter your string = ")
v = ["a","e","i","o","u"]
res4 = [ch for ch in s4 if ch.lower() not in v]
print("String without vowels = ","".join(res4))

# 5.  Find all of the words in a string that are less than 5 letters (take input from user) 
s5 = input("Enter your string = ")
words = s5.split()
res5 = [wd for wd in words if len(wd) < 5]
print("Words with size less than 5 =", " ".join(res5))

# 6.  Use a dictionary comprehension to count the length of each word in a sentence (take input from user) 
s6 = input("Enter your string = ")
words = s6.split()
res6 = {wd: len(wd) for wd in words}
print("Length of words = ",res6)

# 7.  Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.
res7 = [n for n in range(1, 1001) if any(n % d == 0 for d in range(2, 10))]
print("Numbers that are divisible by any single digit = ",res7)