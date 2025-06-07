# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start_range = int(input("Enter a start range: ")) # start range
end_range = int(input("Enter a end range: "))  # end range

for i in range(start_range, end_range):
    if i % 7 == 0 and i % 5 == 0:
        print(i, ": is divisible by 7 and 5")