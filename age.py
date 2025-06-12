def check_age_range():
    try:
        age = int(input("Enter your age: "))

        if 10 <= age <= 20:
            print("✅ Your age is between 10 and 20.")
        else:
            print("❌ Your age is not between 10 and 20.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    check_age_range()
