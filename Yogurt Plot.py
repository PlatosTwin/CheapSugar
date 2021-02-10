import csv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Columns available in the CSV
headers = ['UnitPrice', 'FinalPrice', 'Discount', 'AltUnit', 'AltPrice', 'StrikePrice', \
		'ListPrice', 'ProductName', 'gSugar', 'gProtein', 'gFat', 'Calories', \
		'ContainerNum', 'Ounces']

# Import 
data = pd.read_csv("Yogurt Data CSV.csv", names = headers, skiprows = 1)

# Extract columns from import
UnitPrice = data.UnitPrice
FinalPrice = data.FinalPrice
Discount = data.Discount
AltUnit = data.AltUnit
AltPrice = data.AltPrice
StrikePrice = data.StrikePrice
ListPrice = data.ListPrice
Sugar = data.gSugar
Protein = data.gProtein
Fat = data.gFat
Calories = data.Calories
Ounces = data.Ounces

#
# Run regressions
#

UP_S_stats = linregress(UnitPrice, Sugar)
UP_S_m, UP_S_b, UP_S_r, UP_S_p = UP_S_stats[0], UP_S_stats[1], UP_S_stats[2], UP_S_stats[3]
print "UP v S: " + str(UP_S_r) + ", p: " + str(UP_S_p)

UP_F_stats = linregress(UnitPrice, Fat)
UP_F_m, UP_F_b, UP_F_r, UP_F_p = UP_F_stats[0], UP_F_stats[1], UP_F_stats[2], UP_F_stats[3]
print "UP v F: " + str(UP_F_r) + ", p: " + str(UP_F_p)

UP_P_stats = linregress(UnitPrice, Protein)
UP_P_m, UP_P_b, UP_P_r, UP_P_p = UP_P_stats[0], UP_P_stats[1], UP_P_stats[2], UP_P_stats[3]
print "UP v P: " + str(UP_P_r) + ", p: " + str(UP_P_p)

O_S_stats = linregress(Ounces, Sugar)
O_S_m, O_S_b, O_S_r, O_S_p = O_S_stats[0], O_S_stats[1], O_S_stats[2], O_S_stats[3]
print "O v S: " + str(O_S_r) + ", p: " + str(O_S_p)

UP_C_stats = linregress(UnitPrice, Calories)
UP_C_m, UP_C_b, UP_C_r, UP_C_p = UP_C_stats[0], UP_C_stats[1], UP_C_stats[2], UP_C_stats[3]
print "UP v C: " + str(UP_C_r) + ", p: " + str(UP_C_p)

D_S_stats = linregress(Sugar, Discount)
D_S_m, D_S_b, D_S_r, D_S_p = D_S_stats[0], D_S_stats[1], D_S_stats[2], D_S_stats[3]
print "S v D: " + str(D_S_r) + ", p: " + str(D_S_p)

# Additional regression (not plotted) to test for importance of sale prices

AltUP_S_stats = linregress(AltUnit, Sugar)
AltUP_S_m, AltUP_S_b, AltUP_S_r = AltUP_S_stats[0], AltUP_S_stats[1], AltUP_S_stats[2]
print "AltUP v S: " + str(AltUP_S_r)

#
#
#

# Plot

plt.subplot(321)
plt.scatter(UnitPrice, Sugar, marker='x')
plt.plot(UnitPrice, UP_S_m*UnitPrice + UP_S_b, color="red", linewidth=2)
plt.xlabel("Unit Price (c/oz)", fontsize=15)
plt.ylabel("Grams of Sugar", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(UnitPrice)*1.1])
plt.ylim([0, max(Sugar)*1.1])
plt.title("Figure 1: Grams of Sugar by Unit Price")

plt.subplot(322)
plt.scatter(UnitPrice, Fat, marker='x')
plt.plot(UnitPrice, UP_F_m*UnitPrice + UP_F_b, color="red", linewidth=2)
plt.xlabel("Unit Price (c/oz)", fontsize=15)
plt.ylabel("Grams of Fat", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(UnitPrice)*1.1])
plt.ylim([0, max(Fat)*1.1])
plt.title("Figure 2: Grams of Fat by Unit Price")

plt.subplot(323)
plt.scatter(UnitPrice, Protein, marker='x')
plt.plot(UnitPrice, UP_P_m*UnitPrice + UP_P_b, color="red", linewidth=2)
plt.xlabel("Unit Price (c/oz)", fontsize=15)
plt.ylabel("Grams of Protein", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(UnitPrice)*1.1])
plt.ylim([0, max(Protein)*1.1])
plt.title("Figure 3: Grams of Protein by Unit Price")

plt.subplot(324)
plt.scatter(Ounces, Sugar, marker='x')
plt.plot(Ounces, O_S_m*UnitPrice + O_S_b, color="red", linewidth=2)
plt.xlabel("Container Size (oz)", fontsize=15)
plt.ylabel("Grams of Sugar", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(Ounces)*1.1])
plt.ylim([0, max(Sugar)*1.1])
plt.title("Figure 4: Grams of Sugar by Container Size")

plt.subplot(325)
plt.scatter(UnitPrice, Calories, marker='x')
plt.plot(UnitPrice, UP_C_m*UnitPrice + UP_C_b, color="red", linewidth=2)
plt.xlabel("Unit Price (c/oz)", fontsize=15)
plt.ylabel("Calories", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(UnitPrice)*1.1])
plt.ylim([0, max(Calories)*1.1])
plt.title("Figure 5: Calories by Unit Price")

plt.subplot(326)
plt.scatter(Sugar, Discount, marker='x')
plt.plot(Sugar, D_S_m*Sugar + D_S_b, color="red", linewidth=2)
plt.xlabel("Grams of Sugar", fontsize=15)
plt.ylabel("Discount (dollars)", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([0, max(Sugar)*1.1])
plt.ylim([0, max(Discount)*1.1])
plt.title("Figure 6: Discount by Grams of Sugar")

plt.tight_layout()
plt.show()

# End