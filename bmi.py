def calculate_bmi(feet, inches, pounds):
    if (feet < 0 or inches < 0 or pounds <= 0): return None
    weight = (pounds * 0.45)
    total_inches = ((feet * 12) + inches)
    height = (total_inches * 0.025)
    if (height <= 0): return None
    return (weight/(height ** 2))

def classify_bmi(bmi):
    if (bmi <= 0): return None
    elif (bmi < 18.5): return "Underweight"
    elif (bmi >= 18.5 and bmi <= 24.9): return "Normal weight"
    elif (bmi >= 25 and bmi <= 29.9): return "Overweight"
    elif (bmi >= 30): return "Obese"