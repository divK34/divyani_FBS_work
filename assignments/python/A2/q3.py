# Convert distance given in feet and inches into meter and centimeter.
# 1 foot = 12 inches
# 1 inch = 2.54 cm
# 1 meter = 100 cm

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distane in inches: "))

feet_to_inches = feet * 12
all_inches = feet_to_inches + inches

cm_res = all_inches * 2.54
m_res = cm_res / 100

print(feet,"'",inches,'" to centimeter =',cm_res)
print(feet,"'",inches,'" to meter =',m_res)