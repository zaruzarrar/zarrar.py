
def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

def main():
    print("🔵 Circumference Calculator 🔵")
    
    
    radius = float(input("Enter the radius of the circle: "))
    
    
    result = calculate_circumference(radius)

    print(f"The circumference of the circle is: {result:.2f}")

main()
