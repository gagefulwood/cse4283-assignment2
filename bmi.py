def classify_bmi(bmi):
    if (bmi <= 0): return None
    elif (bmi < 18.5): return "Underweight"
    elif (bmi >= 18.5 and bmi <= 24.9): return "Normal weight"
    elif (bmi >= 25 and bmi <= 29.9): return "Overweight"
    elif (bmi >= 30): return "Obese"