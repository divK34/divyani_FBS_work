# 4. WAP to enter P, T, R and calculate simple Interest. Formula := SI = PrT 
# 5. WAP to enter P, T, R and calculate Compound Interest. Formula := CI = P(1+r)^T 

principal = 4000        # $4000
time = 4                # 4 years
interest_rate = 0.025    # 2.5% in decimal

si = principal * interest_rate * time
ci = principal * ((1 + interest_rate) ** time)
amt_earned = ci - principal

print("Simple interest = ", si)
print("Compound interest = ", ci)
print("Amount earned in interest = ",amt_earned)
