from bmi import calculate_bmi, classify_bmi

def main():
    while True:
        print_menu()
        choice = input("Enter your choice:\t")
        if (choice == '1'):
            try:
                feet = float(input("Enter height in feet:\t"))
                inches = float(input("Enter height in inches:\t"))
                pounds = float(input("Enter weight in pounds:\t"))

                bmi = calculate_bmi(feet, inches, pounds)

                if bmi is not None:
                    category = classify_bmi(bmi)
                    print(f"\n--- Results ---")
                    print(f"Your BMI is: {bmi:.1f}")
                    print(f"Category: {category}")
                    print(f"---------------\n")
                else:
                    print("\n[Error] Invalid input. Height and weight must result in positive numbers.\n")
            except ValueError:
                print("\n[Error] Invalid input. Please enter valid numerical values.\n")
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("\n[Error] Invalid choice. Please select 1 or 0.\n")

def print_menu():
    print("BMI Calculator")
    print("\t(1) Calculate BMI")
    print("\t(0) Exit")

if __name__ == "__main__":
    main()