"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    result = "Invalid score"
elif score > 90:
    result = "Excellent"
elif score > 50:
    result = "Passable"
else:
    result = "Bad"
print(result)
