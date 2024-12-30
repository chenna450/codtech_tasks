class BMI:
    def __init__(self):
        self.records = []

    def calculate_bmi(self, weight, height):
        bmi = weight / (height ** 2)
        return round(bmi, 2)

    def add_record(self, name, weight, height):
        bmi = self.calculate_bmi(weight, height)
        self.records.append({'name': name, 'weight': weight, 'height': height, 'bmi': bmi})
        print(f"Record for {name} added with BMI: {bmi}")

    def view_records(self):
        if self.records:
            print("BMI Records:")
            for record in self.records:
                print(f"Name: {record['name']}, Weight: {record['weight']} kg, Height: {record['height']} m, BMI: {record['bmi']}")
        else:
            print("No records found.")

def main():
    bmi_tracker = BMI()

    while True:
        print("\n1. Add BMI Record")
        print("2. View BMI Records")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            weight = float(input("Enter your weight (in kg): "))
            height = float(input("Enter your height (in meters): "))
            bmi_tracker.add_record(name, weight, height)
        elif choice == '2':
            bmi_tracker.view_records()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
