# WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
# notes in india = 500, 200, 100, 50, 20, 10

amt = int(input("Enter the amount : "))

note_500 = amt // 500       # 5802 // 500 = 11
rem_500 = amt % 500         # 5802 % 500 = 302

note_200 = rem_500 // 200   # 302 // 200 = 1
rem_200 = rem_500 % 200     # 302 % 200 = 102

note_100 = rem_200 // 100   # 102 // 100 = 1
rem_100 = rem_200 % 100     # 102 % 100 = 2

note_50 = rem_100 // 50     # 2 // 50 = 0
rem_50 = rem_100 % 50       # 2 % 50 = 2

note_20 = rem_50 // 20      # 2 // 20 = 0
rem_20 = rem_50 % 20        # 2 % 20 = 2

note_10 = rem_20 // 10      # 2 // 10 = 0
rem_10 = rem_20 % 10        # 2 % 10 = 2

total_notes = (note_500 + note_200 + note_100 + note_50 + note_20 + note_10)

print("Minimum notes needed for amount",amt,"=",total_notes) 
                                                                       

